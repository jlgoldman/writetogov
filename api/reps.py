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
    district_number = apilib.Field(apilib.Integer)
    district_code = apilib.Field(apilib.String())
    party_code = apilib.Field(apilib.Enum(Party.values()))
    chamber = apilib.Field(apilib.Enum(Chamber.values()))
    email = apilib.Field(apilib.String())
    website = apilib.Field(apilib.String())
    address_dc = apilib.Field(apilib.String())
    phone_dc = apilib.Field(apilib.String())


<member-info>
<namelist>Salmon, Matt</namelist>
<bioguideID>S000018</bioguideID>
<lastname>Salmon</lastname>
<firstname>Matt</firstname>
<middlename/>
<sort-name>SALMON,MATT</sort-name>
<suffix/>
<courtesy>Mr.</courtesy>
<prior-congress>113</prior-congress>
<official-name>Matt Salmon</official-name>
<formal-name>Mr. Salmon</formal-name>
<party>R</party>
<caucus>R</caucus>
<state postal-code="AZ">
<state-fullname>Arizona</state-fullname>
</state>
<district>5th</district>
<townname>Mesa</townname>
<office-building>RHOB</office-building>
<office-room>2349</office-room>
<office-zip>20515</office-zip>
<office-zip-suffix>0305</office-zip-suffix>
<phone>(202) 225-2635</phone>
<elected-date date="20141104">November 4, 2014</elected-date>
<sworn-date date="20150106">January 6, 2015</sworn-date>
</member-info>
<committee-assignments>
<committee comcode="ED00" rank="8"/>
<committee comcode="FA00" rank="9"/>
<subcommittee subcomcode="ED02" rank="5"/>
<subcommittee subcomcode="ED13" rank="3"/>
<subcommittee subcomcode="FA05" rank="1" leadership="Chair"/>
<subcommittee subcomcode="FA07" rank="5"/>
</committee-assignments>
</member>

<member>
<member_full>Alexander (R-TN)</member_full>
<last_name>Alexander</last_name>
<first_name>Lamar</first_name>
<party>R</party>
<state>TN</state>
<address>
455 Dirksen Senate Office Building Washington DC 20510
</address>
<phone>(202) 224-4944</phone>
<email>
http://www.alexander.senate.gov/public/index.cfm?p=Email
</email>
<website>http://www.alexander.senate.gov/</website>
<class>Class II</class>
<bioguide_id>A000360</bioguide_id>
</member>

class GetRepsRequest(apilib.Request):
    latlng = apilib.Field(apilib.ModelType(LatLng), required=True)

class GetRepsResponse(apilib.Response):
    resp = apilib.Field(apilib.ListType(Rep))

class RepService(apilib.Service):
    path = '/rep_service'
    methods = apilib.servicemethods(
        apilib.Meth('get', GetRepsRequest, GetRepsResponse))
