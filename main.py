print("APS Hello World!")#aoba
#pip install rsa
#Precisa excutar o comando acima no terminal para o codigo rodar
import rsa

from tkinter import *
from tkinter import ttk
#Instacia o Tkinter
root = Tk()
#Define um titulo para a janela do Tkinter
root.title("APS - Criptografia")

frm = ttk.Frame(root, padding=50)
frm.grid()
def encryptRSA(text):
    #Cria as chaves publicas e privadas
    publicKey, privateKey = rsa.newkeys(128)
    #Texto sendo criptografado com a chave publica
    encodeText = rsa.encrypt(text.encode(), publicKey)          
    #Desncripta o texto
    decodeText = rsa.decrypt(encodeText, privateKey).decode()

    print(f" Texto original: {text} Tamanho: {len(text)}")
    print(f" Chave publica: {publicKey} \n Tamanho: {len(str(publicKey))}")
    print(f" Chave privada: {privateKey} \n Tamanho: {len(str(privateKey))}")
    print(f" Texto Criptogafado: {encodeText} Tamanho: {len(encodeText)}")
    print(f" Texto original: {decodeText} Tamanho: {len(decodeText)}")
    return [publicKey, privateKey, encodeText, decodeText]
def encrypt():
    entry = entryText.get()
    print(entry)
    results = encryptRSA(entry)
    labelPublicKey = Label(root, text=str(results[0])).grid(column=1,row=2)
    labelPrivateKey = Label(root, text=str(results[1])).grid(column=1,row=3)
    labelEncodeText = Label(root, text=str(results[2])).grid(column=1,row=4)
    labelDecodeText = Label(root, text=str(results[3])).grid(column=1,row=5)
#Cria o label e o posiciona no grid 
labelEntry = Label(root, text= "Digite o texto que sera criptografado").grid(column=0,row=0)
entryText = Entry(root, width=30)
entryText.grid(column=1,row=0)
botao = Button(root, text="Clica aqui",command = encrypt)
botao.grid(column=2, row=0, padx=5, pady=15)

labelTextPublicKey = Label(root, text= "Chave publica").grid(column=0, row=2)
labelTextPrivateKey = Label(root, text= "Chave privada").grid(column=0, row=3)
labelTextEncodeText = Label(root, text= "Texto Criptogafado").grid(column=0, row=4)
labelTextDecodeText = Label(root, text= "Texto original").grid(column=0, row=5)




root.mainloop()