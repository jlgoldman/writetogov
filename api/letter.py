import apilib

class GenerateLetterRequest(apilib.Request):
    rep_id = apilib.Field(apilib.Integer(), required=True)
    body = apilib.Field(apilib.String(), required=True)
    name_and_address = apilib.Field(apilib.String(), required=True)
    include_address_page = apilib.Field(apilib.Boolean())

class GenerateLetterResponse(apilib.Response):
    pdf_content = apilib.Field(apilib.Bytes())

class LetterService(apilib.Service):
    path = '/letter_service'
    methods = apilib.servicemethods(
        apilib.Meth('generate', GenerateLetterRequest, GenerateLetterResponse))
