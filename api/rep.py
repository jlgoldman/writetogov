import apilib

class LatLng(apilib.Model):
    lat = apilib.Field(apilib.Float())
    lng = apilib.Field(apilib.Float())

class ContactInfo(apilib.Model):
    class OfficeType(apilib.EnumValues):
        WASHINGTON = 'WASHINGTON'
        DISTRICT = 'DISTRICT'
    address = apilib.Field(apilib.String())
    phone = apilib.Field(apilib.String())
    email = apilib.Field(apilib.String())
    website = apilib.Field(apilib.String())

class Rep(apilib.Model):
    class Chamber(apilib.EnumValues):
        HOUSE = 'HOUSE'
        SENATE = 'SENATE'

    class Party(apilib.EnumValues):
        D = 'D'
        R = 'R'
        I = 'I'

    first_name = apilib.Field(apilib.String())
    last_name = apilib.Field(apilib.String())
    state_code = apilib.Field(apilib.String())
    district_number = apilib.Field(apilib.Integer())
    district_code = apilib.Field(apilib.String())
    party_code = apilib.Field(apilib.Enum(Party.values()))
    chamber = apilib.Field(apilib.Enum(Chamber.values()))
    email_link = apilib.Field(apilib.String())
    email = apilib.Field(apilib.String())
    website = apilib.Field(apilib.String())
    address_dc = apilib.Field(apilib.String())
    phone_dc = apilib.Field(apilib.String())

class GetRepsRequest(apilib.Request):
    latlng = apilib.Field(apilib.ModelType(LatLng), validators=[
        apilib.ExactlyOneNonempty('latlng', 'district_code')])
    district_code = apilib.Field(apilib.String(),  validators=[
        apilib.ExactlyOneNonempty('latlng', 'district_code')])

class GetRepsResponse(apilib.Response):
    house_rep = apilib.Field(apilib.ModelType(Rep))
    senators = apilib.Field(apilib.ListType(Rep))
    leadership = apilib.Field(apilib.ListType(Rep))

class RepService(apilib.Service):
    path = '/rep_service'
    methods = apilib.servicemethods(
        apilib.Meth('get', GetRepsRequest, GetRepsResponse))
