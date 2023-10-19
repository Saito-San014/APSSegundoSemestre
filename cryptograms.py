import rsa
from cryptography.fernet import Fernet
import binascii
from rsa.pkcs1 import DecryptionError
def encryptAES(text):
    #Cria a chave
    key = Fernet.generate_key()
    #Cria a cifra
    cipher = Fernet(key)
    #Encripta o texto
    encodeText = cipher.encrypt(text.encode())
    #Desencripta o texto
    decodeText = cipher.decrypt(encodeText).decode()
    print(cipher)
    return [key, encodeText, decodeText]
class cipherAES():
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
    def getKey(self):
        return self.key
    def setKey(self, key):
        self.key = key
        self.cipher = Fernet(self.key)
    def encrypt(self, text):
        return self.cipher.encrypt(text.encode('utf-8'))
    def decrypt(self, encodeText):
        return self.cipher.decrypt(encodeText).decode('utf-8')
    
#Criptografia RSA
class cipherRSA():
    def __init__(self):
        self.publicKey, self.privateKey = rsa.newkeys(512)
        
    def getPrivateKey(self):
        return self.privateKey.save_pkcs1().decode('utf-8')
    
    def getPublicKey(self):
        return self.publicKey.save_pkcs1().decode('utf-8')
    
    def setPrivateKey(self, privateKeyPEM):
        try:
            self.privateKey = rsa.PrivateKey.load_pkcs1(privateKeyPEM.encode('utf-8'))
            self.publicKey = rsa.PublicKey(self.privateKey.n, self.privateKey.e)
            return None
        except ValueError:
            return ValueError
        except Exception as e:
            return e
    def setPublicKey(self, publicKeyPEM):
        try:
            self.publicKey = rsa.PublicKey.load_pkcs1(publicKeyPEM.encode('utf-8'))
            return None
        except ValueError:
            return ValueError
        except Exception as e:
            return e
    def encrypt(self, text):
        return rsa.encrypt(text.encode('utf-8'), self.publicKey)
    def decrypt(self, encodeText):
        print(encodeText)
        try:
            decode = rsa.decrypt(encodeText, self.privateKey).decode('utf-8')
            return decode
        except DecryptionError:
            return None
        except Exception as e:
            return e