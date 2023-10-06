print("APS Hello World!")#aoba
#pip install rsa
#Precisa excutar o comando acima no terminal para o codigo rodar
import rsa

#Cria as chaves publicas e privadas
publicKey, privateKey = rsa.newkeys(512)
text = input("Digite o texto: \n")

#Texto sendo criptografado com a chave publica
encodeText = rsa.encrypt(text.encode(), publicKey)          
#Desncripta o texto
decodeText = rsa.decrypt(encodeText, privateKey).decode()

print(f" Texto original: {text} Tamanho: {len(text)}")
print(f" Chave publica: {publicKey} \n Tamanho: {len(str(publicKey))}")
print(f" Chave privada: {privateKey} \n Tamanho: {len(str(privateKey))}")
print(f" Texto Criptogafado: {encodeText} Tamanho: {len(encodeText)}")
print(f" Texto original: {decodeText} Tamanho: {len(decodeText)}")
