from api import issue
from api import reminder
from api import rep
from logic import issue_service
from logic import reminder_service
from logic import rep_service
from util import ids

def get_rep_by_id(rep_id):
    service = rep_service.RepServiceImpl()
    req = rep.GetRepsRequest(rep_ids=[rep_id])
    resp = service.invoke('get', req)
    return resp.reps[0] if resp.reps else None

def lookup_reps_by_district_code(district_code):
    service = rep_service.RepServiceImpl()
    req = rep.LookupRepsRequest(district_code=district_code)
    return service.invoke('lookup', req)

def unsubscribe_from_reminder(email, token):
    service = reminder_service.ReminderServiceImpl()
    req = reminder.UpdateReminderRequest(
        email=email,
        token=token,
        status=reminder.Status.UNSUBSCRIBED)
    return service.invoke('update', req)

def get_issue_by_public_id(public_issue_id):
    req = issue.GetIssueRequest(issue_id=ids.db_id(public_issue_id))
    service = issue_service.IssueServiceImpl()
    resp = service.invoke('get', req)
    return resp.issue
