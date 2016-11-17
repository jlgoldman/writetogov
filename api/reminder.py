import apilib

class Frequency(apilib.EnumValues):
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'

class Status(apilib.EnumValues):
    ACTIVE = 'ACTIVE'
    UNSUBSCRIBED = 'UNSUBSCRIBED'

class CreateReminderRequest(apilib.Request):
    email = apilib.Field(apilib.String(), required=True)
    frequency = apilib.Field(apilib.Enum(Frequency.values()), required=True)

class CreateReminderResponse(apilib.Response):
    pass

class UpdateReminderRequest(apilib.Request):
    email = apilib.Field(apilib.String(), required=True)
    token = apilib.Field(apilib.String(), required=True)
    status = apilib.Field(apilib.Enum(Status.values()), required=True)

class UpdateReminderResponse(apilib.Response):
    pass

class ReminderService(apilib.Service):
    path = '/reminder_service'
    methods = apilib.servicemethods(
        apilib.Meth('create', CreateReminderRequest, CreateReminderResponse),
        apilib.Meth('update', UpdateReminderRequest, UpdateReminderResponse))
