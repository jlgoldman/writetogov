import base64

from Crypto import Random
from Crypto.Cipher import AES

from config import constants

BLOCK_SIZE = 16
PADDING_CHAR = '='

def pad(msg, block_size=BLOCK_SIZE, padding_char=PADDING_CHAR):
    return msg + ((block_size - len(msg) % block_size) * padding_char)

def unpad(msg, padding_char=PADDING_CHAR):
    return msg.rstrip(padding_char)

def encrypt(msg, key=constants.FLASK_SECRET_KEY):
    iv = Random.get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, mode=AES.MODE_CBC, IV=iv)
    ciphertext = cipher.encrypt(pad(msg))
    return base64.urlsafe_b64encode(iv + ciphertext)

def decrypt(msg, key=constants.FLASK_SECRET_KEY):
    msg_bytes = base64.urlsafe_b64decode(str(msg))
    iv, ciphertext = msg_bytes[:BLOCK_SIZE], msg_bytes[BLOCK_SIZE:]
    cipher = AES.new(key, mode=AES.MODE_CBC, IV=iv)
    return unpad(cipher.decrypt(ciphertext))
