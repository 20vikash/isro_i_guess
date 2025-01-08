from Crypto.Hash import CMAC # type: ignore
from Crypto.Cipher import AES # type: ignore

def getCmac(message):
    secret = b'Sixteen byte key'
    cobj = CMAC.new(secret, ciphermod=AES)
    cobj.update(message)

    cobj.hexdigest()
