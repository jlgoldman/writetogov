from api import rep
from logic import rep_service

def get_rep_by_id(rep_id):
    service = rep_service.RepServiceImpl()
    req = rep.GetRepsRequest(rep_ids=[rep_id])
    resp = service.invoke('get', req)
    return resp.reps[0] if resp.reps else None

def lookup_reps_by_district_code(district_code):
    service = rep_service.RepServiceImpl()
    req = rep.LookupRepsRequest(district_code=district_code)
    resp = service.invoke('lookup', req)
    return resp
