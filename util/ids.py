import apilib

apilib.model._create_id_hasher()
ID_HASHER = apilib.model.ID_HASHER

def public_id(int_db_id):
    return ID_HASHER.encode(int_db_id)

def db_id(str_public_id):
    # Unclear why this doesn't work with unicode values,
    # must coerce it to be a string.
    values = ID_HASHER.decode(str(str_public_id))
    return values[0] if values else None
