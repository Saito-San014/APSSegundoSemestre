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


#Metodo que cripitografa em RSA
'''def encryptRSA(text):
    #Cria as chaves publicas e privadas
    publicKey, privateKey = rsa.newkeys(512)
    #Texto sendo criptografado com a chave publica
    encodeText = rsa.encrypt(text.encode(), publicKey)          
    #Desencripta o texto
    decodeText = rsa.decrypt(encodeText, privateKey).decode()
    return [publicKey, privateKey, encodeText, decodeText]'''
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
        print(str(self.publicKey))
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
    
crsa = cipherRSA()
encode = crsa.encrypt("Teste")
texto = encode.decode('latin-1')
decode = texto.encode('latin-1')



# Representação hexadecimal dos dados criptografados
hex_data = binascii.hexlify(encode).decode('utf-8')
bytes_data = binascii.unhexlify(hex_data)
