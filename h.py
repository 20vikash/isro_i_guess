import hmac
import hashlib

key = b"mysecretkey"

def getHmac(message):
    h = hmac.new(key, message, hashlib.sha256)
    h.hexdigest()
