print("APS Hello World!")#aoba
#pip install rsa
#Precisa excutar o comando acima no terminal para o codigo rodar
import rsa

from tkinter import *
from tkinter import ttk
#Metodo que cripitografa em RSA
def encryptRSA(text):
    #Cria as chaves publicas e privadas
    publicKey, privateKey = rsa.newkeys(512)
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
#Metodo executado ao clicar no botão enviar
def encrypt():
    entry = entryText.get()
    print(entry)
    results = encryptRSA(entry)
    labelPublicKey.configure(text=str(results[0]))
    labelPrivateKey.configure(text=str(results[1]))
    labelEncodeText.configure(text=str(results[2]))
    labelDecodeText.configure(text=str(results[3]))
#Instacia o Tkinter
root = Tk()
#Define um titulo para a janela do Tkinter
root.title("APS - Criptografia")
#Define o tamanho da janela
root.geometry('1980x1080')
#Maximiza a janela
root.state('zoomed')
#Define um estilo para o frame de entradas
s = ttk.Style()
s.configure('My.TFrame', background='red')
#Instancia o frame de entradas
frameEntry = ttk.Frame(root, style='My.TFrame',padding=20,width=600)
frameEntry.pack(side=TOP, padx=20)

#Intancia o frame principal
frm = ttk.Frame(root)
#Posicionao o frame no top com uma margin de 20 na horizontal
frm.pack(side=TOP,padx=20)

frm.columnconfigure(1, weight=1)
#Cria o label e o posiciona no grid 
labelEntry = Label(frameEntry, text= "Digite o texto que sera criptografado")
labelEntry.grid(column=0,row=0, padx=10, ipadx=20,ipady=10)
#Cria o input de entrada para o usuairo digitar
entryText = Entry(frameEntry, width=30)
#Posiciona no grid
#PS. não pode ser como no label, pois quando for utilizar get() ira return null
entryText.grid(column=1,row=0,padx=10)
#Cria  a instacia do botão e define o onClick na função encrypt
botao = Button(frameEntry, text="Clica aqui",command = encrypt)
#define aonde o botão vai ficar no grid
botao.grid(column=2, row=0,ipadx=20,padx=20) 
#Labels para nomear a informações
labelTextPublicKey = Label(frm, text= "Chave publica",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
labelTextPublicKey.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

labelTextPrivateKey = Label(frm, text= "Chave privada",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
labelTextPrivateKey.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

labelTextEncodeText = Label(frm, text= "Texto Criptogafado",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
labelTextEncodeText.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

labelTextDecodeText = Label(frm, text= "Texto original",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
labelTextDecodeText.grid(row = 3, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

#Tamanho da Fonte dos label de exibição
fontSizeLabels = 16
wrapLength = 800

labelPublicKey = Label(frm, wraplength=wrapLength,text="", background="green", font=("Arial", fontSizeLabels),borderwidth=2,height=5,width=900, relief="groove")
labelPublicKey.grid(row = 0, column = 1, padx = 5, pady = 5, ipadx = 20, ipady = 20, rowspan = 1, columnspan = 1, sticky = 'NSEW')

labelPrivateKey = Label(frm, wraplength=wrapLength,text="", background="green", font=("Arial", fontSizeLabels),borderwidth=2,height=10,width=20, relief="groove", anchor="center")
labelPrivateKey.grid(row = 1, column = 1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

labelEncodeText = Label(frm, wraplength=wrapLength,text="", background="green", font=("Arial", fontSizeLabels),borderwidth=2,height=5,width=20, relief="groove", anchor="center")
labelEncodeText.grid(row = 2, column = 1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

labelDecodeText = Label(frm, wraplength=wrapLength,text="", background="green", font=("Arial",fontSizeLabels),borderwidth=2,height=5,width=20, relief="groove",)
labelDecodeText.grid(row = 3, column = 1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

root.mainloop()