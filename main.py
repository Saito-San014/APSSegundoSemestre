print("APS Hello World!")#aoba
#pip install rsa
#Precisa excutar o comando acima no terminal para o codigo rodar
from tkinter import filedialog
import rsa

from tkinter import *
import tkinter as tk
from tkinter import ttk
cryptType = "RSA"
def open_file_dialog():
    file_path = filedialog.askopenfilename(
        #initialdir="/",  # Diretório inicial (pode ser alterado)
        title="Selecione um arquivo de texto",
        filetypes=(("Arquivos de Texto", "*.txt"),)
    )
    if file_path:
        # O usuário selecionou um arquivo, você pode fazer algo com o caminho do arquivo aqui
        print("Arquivo selecionado:", file_path)
        try:
            with open(file_path, 'r') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
                set_text(conteudo)
        except FileNotFoundError:
            print("O arquivo não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")

#Metodo que cripitografa em RSA
def encryptRSA(text):
    #Cria as chaves publicas e privadas
    publicKey, privateKey = rsa.newkeys(512)
    #Texto sendo criptografado com a chave publica
    encodeText = rsa.encrypt(text.encode(), publicKey)          
    #Desncripta o texto
    decodeText = rsa.decrypt(encodeText, privateKey).decode()
    return [publicKey, privateKey, encodeText, decodeText]

    print(f" Texto original: {text} Tamanho: {len(text)}")
    print(f" Chave publica: {publicKey} \n Tamanho: {len(str(publicKey))}")
    print(f" Chave privada: {privateKey} \n Tamanho: {len(str(privateKey))}")
    print(f" Texto Criptogafado: {encodeText} Tamanho: {len(encodeText)}")
    print(f" Texto original: {decodeText} Tamanho: {len(decodeText)}")
#Metodo executado ao clicar no botão enviar
def encrypt():
    entry = entryText.get()
    results = 0 
    if cryptType == "RSA":
        results = encryptRSA(entry)
        setLabels(results)
    elif cryptType == "AES":
        print("aes")
        clearLabels()
    elif cryptType == "Ambas":
        pass
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
def set_text(text):
    entryText.delete(0, tk.END)  # Limpa qualquer texto existente
    texto = "Texto predefinido"
    entryText.insert(0, text)  # Insere o texto no Entry
    encrypt()


#Cria  a instacia do botão e define o onClick na função encrypt
botao = Button(frameEntry, text="Clique aqui",command = encrypt)
#define aonde o botão vai ficar no grid
botao.grid(column=2, row=0,ipadx=20,padx=20) 

buttonBrowser = Button(frameEntry, text="Selecionar", command=open_file_dialog)
buttonBrowser.grid(row=1,column=1)

opcoes = ["RSA", "AES", "Ambas"]

combo = ttk.Combobox(frameEntry, values=opcoes)
combo.set(opcoes[0])
combo.grid(row=1, column=0)

def selecionarOpcao(event):
    global cryptType
    opcao = combo.get()
    print(opcao)
    match(opcao):
        case "RSA":
            cryptType = opcao
        case "AES":
            cryptType = opcao
        case _:
            pass

combo.bind("<<ComboboxSelected>>", selecionarOpcao)  # Associa o evento à função
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
def setLabels(texts):
    labelPublicKey.configure(text=str(texts[0]))
    labelPrivateKey.configure(text=str(texts[1]))
    labelEncodeText.configure(text=str(texts[2]))
    labelDecodeText.configure(text=str(texts[3]))
def clearLabels():
    labelPublicKey.configure(text="")
    labelPrivateKey.configure(text="")
    labelEncodeText.configure(text="")
    labelDecodeText.configure(text="")

root.mainloop()