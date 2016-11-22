import apilib
from flask import render_template

from app import app
from api import issue
from database import db
from database import db_models
from util import crypto
from util import ids
from util import sendgrid_
from util import time_
from util import urls

I = db_models.Issue
R = db_models.Rep

class IssueServiceImpl(issue.IssueService, apilib.ServiceImplementation):
    def __init__(self, **kwargs):
        pass

    def get(self, req):
        db_issue = I.query.get(req.issue_id) if req.issue_id else None
        return issue.GetIssueResponse(
            issue=_db_issue_to_api(db_issue))

    def create(self, req):
        self._validate_issue(req.issue, req.creator_email)
        now = time_.utcnow()
        db_issue = db_models.Issue(
            creator_email=req.creator_email.strip().lower(),
            creator_name=req.issue.creator_name,
            title=req.issue.title,
            description=req.issue.description,
            rep_ids=req.issue.rep_ids,
            time_created=now,
            time_updated=now)
        db.session.add(db_issue)
        db.session.commit()
        api_issue = _db_issue_to_api(db_issue)
        try:
            _send_creation_email(req.creator_email, api_issue)
        except Exception as e:
            app.logger.error('Error sending issue creation email: %s' % e)
        return issue.CreateIssueResponse(
            issue=api_issue)

    def update(self, req):
        self._validate_issue(req.issue, creator_email=None)
        db_issue = I.query.get(req.issue.issue_id)
        if not db_issue:
            raise _invalid_issue_id_exception(req.issue.issue_id, path='issue.issue_id')
        if not _verify_issue_token(req.token, db_issue.creator_email, req.issue.issue_id):
            raise _invalid_token_exception()

        if req.issue.creator_name is not None:
            db_issue.creator_name = req.issue.creator_name
        if req.issue.title is not None:
            db_issue.title = req.issue.title
        if req.issue.description is not None:
            db_issue.description = req.issue.description
        if req.issue.rep_ids is not None:
            db_issue.rep_ids = req.issue.rep_ids
        db_issue.time_updated = time_.utcnow()
        db.session.commit()
        return issue.UpdateIssueResponse(issue=_db_issue_to_api(db_issue))

    def delete(self, req):
        db_issue = I.query.get(req.issue_id)
        if not db_issue:
            raise _invalid_issue_id_exception(req.issue_id, path='issue_id')
        if not _verify_issue_token(req.token, db_issue.creator_email, req.issue_id):
            raise _invalid_token_exception()
        db.session.delete(db_issue)
        db.session.commit()
        return issue.DeleteIssueResponse()

    def process_unhandled_exception(self, exception):
        # For debugging
        return True

    def _validate_issue(self, issue, creator_email):
        ec = apilib.ErrorContext()
        if len(issue.title) > 100:
            ec.extend('issue.title').add_error('TOO_LONG', 'Title can be at most 100 characters')
        if len(issue.description) > 10000:
            ec.extend('issue.description').add_error('TOO_LONG', 'Description can be at most 10000 characters')
        if issue.creator_name and len(issue.creator_name) > 100:
            ec.extend('issue.creator_name').add_error('TOO_LONG', 'Creator name can be at most 100 characters')
        if creator_email and len(creator_email) > 100:
            ec.extend('creator_email').add_error('TOO_LONG', 'Creator email can be at most 100 characters')
        if issue.rep_ids:
            if len(issue.rep_ids) > 100:
                ec.extend('issue.rep_ids').add_error('TOO_LONG', 'You can only add at most 100 reps to a issue')
            else:
                db_reps = R.query.filter(R.rep_id.in_(issue.rep_ids))
                db_rep_ids = set(db_rep.rep_id for db_rep in db_reps)
                for i, rep_id in enumerate(issue.rep_ids):
                    if rep_id not in db_rep_ids:
                        ec.extend('issue').extend('rep_ids').extend(index=i) \
                            .add_error('INVALID_REP_ID', 'No Rep found for id %d' % rep_id)
        if ec.has_errors():
            raise _validation_exception(ec)

def _db_issue_to_api(db_issue):
    if not db_issue:
        return None
    return issue.Issue(
        issue_id=db_issue.issue_id,
        creator_name=db_issue.creator_name,
        title=db_issue.title,
        description=db_issue.description,
        rep_ids=db_issue.rep_ids,
        url=urls.absurl('/issue/%s' % ids.public_id(db_issue.issue_id)))

def _verify_issue_token(token, email, issue_id):
    email = email.strip().lower()
    try:
        msg = crypto.decrypt_with_salt(token)
    except:
        return False
    parts = msg.split('|||')
    token_email, token_issue_id = parts[0], int(parts[1])
    return (token_email == email and token_issue_id == issue_id)

def _generate_issue_token(email, issue_id):
    email = email.strip().lower()
    # Not using the timestamp for now but creating tokens with it
    # just in case it's needed in the future.
    timestamp = time_.current_timestamp()
    msg = '%s|||%d|||%d' % (email, issue_id, timestamp)
    return crypto.encrypt_with_salt(msg)

def _make_edit_url(email, issue_id):
    token = _generate_issue_token(email, issue_id)
    path = '/issue/%s/edit' % ids.public_id(issue_id)
    return urls.absurl(urls.append_params(path, {'token': token}))

def _send_creation_email(email, api_issue):
    edit_url = _make_edit_url(email, api_issue.issue_id)
    subject = 'Your writetogov.com page "%s" has been created' % api_issue.title

    html = render_template('email/issue_created.html',
        subject=subject,
        issue=api_issue,
        edit_url=edit_url)
    text = render_template('email/issue_created.txt',
        issue=api_issue,
        edit_url=edit_url)

    sendgrid_.send_message(
        subject=subject,
        body_text=text,
        body_html=html,
        recipients=[email])

def _validation_exception(ec):
    api_errors = [apilib.ApiError(code=ve.code, path=ve.path, message=ve.msg) for ve in ec.all_errors()]
    raise apilib.ApiException.request_error(api_errors)

def _invalid_issue_id_exception(issue_id, path):
    error = apilib.ApiError(code='UNKNOWN_ISSUE', path=path,
        message='No issue with issue_id %s could be found.' % issue_id)
    return apilib.ApiException.request_error([error])

def _invalid_token_exception():
    error = apilib.ApiError(code='INVALID_TOKEN', path='token',
        message='The given token is invalid')
    return apilib.ApiException.request_error([error])
