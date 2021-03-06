import apilib

class GenerateLetterRequest(apilib.Request):
    rep_id = apilib.Field(apilib.Integer(), required=True)
    body = apilib.Field(apilib.String(), required=True)
    name_and_address = apilib.Field(apilib.String(), required=True)
    include_address_page = apilib.Field(apilib.Boolean())

class GenerateLetterResponse(apilib.Response):
    pdf_content = apilib.Field(apilib.Bytes())

class GenerateAndMailLetterRequest(apilib.Request):
    stripe_token = apilib.Field(apilib.String(), required=True)
    email = apilib.Field(apilib.String(), required=True)
    rep_id = apilib.Field(apilib.Integer(), required=True)
    body = apilib.Field(apilib.String(), required=True)
    name_and_address = apilib.Field(apilib.String(), required=True)

class GenerateAndMailLetterResponse(apilib.Response):
    expected_delivery_date = apilib.Field(apilib.String())
    lob_pdf_url = apilib.Field(apilib.String())

class ParseAddressRequest(apilib.Request):
    name_and_address = apilib.Field(apilib.String(), required=True)

class ParseAddressResponse(apilib.Response):
    name = apilib.Field(apilib.String())
    line1 = apilib.Field(apilib.String())
    city = apilib.Field(apilib.String())
    state = apilib.Field(apilib.String())
    zip = apilib.Field(apilib.String())

class LetterService(apilib.Service):
    path = '/letter_service'
    methods = apilib.servicemethods(
        apilib.Meth('generate', GenerateLetterRequest, GenerateLetterResponse),
        apilib.Meth('generate_and_mail', GenerateAndMailLetterRequest, GenerateAndMailLetterResponse),
        apilib.Meth('parse_address', ParseAddressRequest, ParseAddressResponse))
