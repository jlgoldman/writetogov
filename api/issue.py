import apilib

class Issue(apilib.Model):
    issue_id = apilib.Field(apilib.EncryptedId(), required='update')
    creator_name = apilib.Field(apilib.String(), readonly='update')
    title = apilib.Field(apilib.String(), required='create')
    description = apilib.Field(apilib.String(), required='create')
    rep_ids = apilib.Field(apilib.ListType(apilib.Integer()), validators=[apilib.Unique()])

class GetIssueRequest(apilib.Request):
    issue_id = apilib.Field(apilib.EncryptedId(), required=True)

class GetIssueResponse(apilib.Response):
    issue = apilib.Field(apilib.ModelType(Issue))

class CreateIssueRequest(apilib.Request):
    creator_email = apilib.Field(apilib.String(), required=True)
    issue = apilib.Field(apilib.ModelType(Issue), required=True)

class CreateIssueResponse(apilib.Response):
    issue = apilib.Field(apilib.ModelType(Issue))

class UpdateIssueRequest(apilib.Request):
    token = apilib.Field(apilib.String(), required=True)
    issue = apilib.Field(apilib.ModelType(Issue), required=True)

class UpdateIssueResponse(apilib.Response):
    issue = apilib.Field(apilib.ModelType(Issue))

class DeleteIssueRequest(apilib.Request):
    token = apilib.Field(apilib.String(), required=True)
    issue_id = apilib.Field(apilib.EncryptedId(), required=True)

class DeleteIssueResponse(apilib.Response):
    pass

class IssueService(apilib.Service):
    path = '/issue_service'
    methods = apilib.servicemethods(
        apilib.Meth('get', GetIssueRequest, GetIssueResponse),
        apilib.Meth('create', CreateIssueRequest, CreateIssueResponse),
        apilib.Meth('update', UpdateIssueRequest, UpdateIssueResponse),
        apilib.Meth('delete', DeleteIssueRequest, DeleteIssueResponse))
