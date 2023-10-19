import binascii
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import filedialog
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import rsa  
from cryptograms import cipherRSA
class FrameRSA(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.columnconfigure(1, weight=1)
        self.parent = parent
        self.widgets()
        
    def widgets(self):
        def set_text(text, widget):
            if widget.cget("state") == "disable":
                widget.config(state=tk.NORMAL)
                widget.delete("1.0", tk.END)  # Limpa qualquer texto existente
                widget.insert("1.0", text)  # Insere o texto no Entry
                widget.config(state=tk.DISABLED)
            else:
                widget.delete("1.0", tk.END)  # Limpa qualquer texto existente
                widget.insert("1.0", text)  # Insere o texto no Entry

        def open_file_dialog(widget):
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
                        select_widget(widget)
                        set_text(conteudo, widget)
                except FileNotFoundError:
                    print("O arquivo não foi encontrado.")
                except Exception as e:
                    print(f"Ocorreu um erro: {str(e)}")
        def save(widget):
            if widget == self.textBoxPrivateKey:
                private_key = rsa.PrivateKey.load_pkcs1(widget.cget("text").encode())
                private_key_pem = private_key.save_pkcs1(format='PEM')
                print(private_key_pem)
        def select_widget(widget):
            if widget == self.textBoxDecode:
                self.textBoxEncode.delete("1.0", tk.END)  # Limpa qualquer texto existente
                self.textBoxDecode.config(state=tk.NORMAL)
                self.textBoxEncode.config(state=tk.DISABLED)
            elif widget == self.textBoxEncode:
                self.textBoxDecode.delete("1.0", tk.END)  # Limpa qualquer texto existente
                self.textBoxEncode.config(state=tk.NORMAL)
                self.textBoxDecode.config(state=tk.DISABLED)

        def on_click(event):
            if event.widget == self.textBoxDecode:
                self.textBoxDecode.config(state=tk.NORMAL)
                self.textBoxEncode.config(state=tk.DISABLED)
            elif event.widget == self.textBoxEncode:
                self.textBoxEncode.config(state=tk.NORMAL)
                self.textBoxDecode.config(state=tk.DISABLED)

        def on_key(event):
            if event.widget == self.textBoxDecode:
                self.textBoxEncode.delete("1.0", tk.END)  # Limpa qualquer texto existente
            elif event.widget == self.textBoxEncode:
                self.textBoxDecode.delete("1.0", tk.END)  # Limpa qualquer texto existente

        #Labels para nomear a informações
        fontLabelText = font.Font(family="Arial", size=12)
        fontLabel = font.Font(family="Arial", size=12)
        #Largura do label em quantidade de caracteresfontLabelText
        widthLabel = 150
        largura_caractere = fontLabel.measure("A") 
        fontSizeLabels = 8
        wrapLength = largura_caractere * (widthLabel-80)     
        
        self.labelTextDecodeText = Label(self, text= "Texto original", background='cyan', font=("Arial", 16),borderwidth=0,  relief="groove", anchor="center")
        self.labelTextDecodeText.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        
        self.labelTextPrivateKey = Label(self, text= "Chave privada",background='cyan', font=("Arial", 16),borderwidth=0, relief="groove", anchor="center")
        self.labelTextPrivateKey.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelTextPublicKey = Label(self, text= "Chave publica",background='cyan', font=fontLabel, borderwidth=0, relief="groove", anchor="center")
        self.labelTextPublicKey.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelTextEncodeText = Label(self, text= "Texto Criptogafado",background='cyan', font=("Arial", 16),borderwidth=0, relief="groove", anchor="center")
        self.labelTextEncodeText.grid(row = 3, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.textFrameDecode = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.textFrameDecode.grid(row=0, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        self.textBoxDecode = Text(self.textFrameDecode, height=10, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxDecode.pack(expand=True, fill=X,padx=10,pady=5)
        
        self.textBoxDecode.bind("<Button-1>", on_click)

        self.framePrivateKey = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.framePrivateKey.grid(row=1, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 5, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        
        self.textBoxPrivateKey = Text(self.framePrivateKey, height=5, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxPrivateKey.pack(expand=True, fill=X,padx=10,pady=5)
        
        self.framePublicKey = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.framePublicKey.grid(row=2, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 5, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        
        self.textBoxPublicKey = Text(self.framePublicKey, height=5, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxPublicKey.pack(expand=True, fill=X,padx=10,pady=5)

        self.textFrameEncode = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.textFrameEncode.grid(row=3, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        self.textBoxEncode = Text(self.textFrameEncode, height=5, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxEncode.pack(expand=True, fill=X,padx=10,pady=5)

        self.textBoxEncode.bind("<Button-1>", on_click)
        
        self.buttonBrowserDecodeText = Button(self, text="Selecionar", command=lambda widget=self.textBoxDecode : open_file_dialog(widget))
        self.buttonBrowserDecodeText.grid(row=0,column=2, padx=20)

        self.framePrivateKeyButtons = Frame(self,width=30, background="black")
        self.framePrivateKeyButtons.grid(row=1,column=2, padx=20)

        self.buttonBrowserPrivateKey = Button(self.framePrivateKeyButtons, text="Selecionar", command=lambda widget=self.textBoxDecode : open_file_dialog(widget))
        self.buttonBrowserPrivateKey.pack(side=TOP, pady=2)
        self.buttonPastePrivateKey = Button(self.framePrivateKeyButtons, text="Salvar", command=lambda widget = self.textBoxPrivateKey : save(widget))
        self.buttonPastePrivateKey.pack(side=TOP, pady=2)

        self.buttonBrowserPublicKey = Button(self, text="Selecionar", command=lambda widget=self.textBoxDecode : open_file_dialog(widget))
        self.buttonBrowserPublicKey.grid(row=0,column=2, padx=20)

        self.buttonBrowserEncodeText = Button(self, text="Selecionar", command=lambda widget=self.textBoxEncode : open_file_dialog(widget))
        self.buttonBrowserEncodeText.grid(row=3,column=2, padx=20)

        

    def encrypt_decrypt(self, cRSA: cipherRSA):
        #Se for encriptar
        if self.textBoxEncode.cget("state") == tk.DISABLED:
            if self.textBoxPrivateKey.get(1.0,"end-1c") == "":
                setNormalWidget(self.textBoxPrivateKey, cRSA.getPrivateKey())
                setNormalWidget(self.textBoxPublicKey, cRSA.getPublicKey())
                encodeText = cRSA.encrypt(self.textBoxDecode.get("1.0","end-1c"))
                setDisableWidget(self.textBoxEncode, toHex(encodeText))
            else:
                encodeText = cRSA.encrypt(self.textBoxDecode.get("1.0","end-1c"))
                setDisableWidget(self.textBoxEncode, toHex(encodeText))            
        elif self.textBoxDecode.cget("state") == tk.DISABLED:
            if self.textBoxPrivateKey.get(1.0,"end-1c") == "":
                pass
            else:
                bytes_data = toBytes(self.textBoxEncode.get("1.0","end-1c"))
                if bytes_data == None:
                    pass
                else:
                    setDisableWidget(self.textBoxDecode,cRSA.decrypt(bytes_data))

    
def setDisableWidget(widget, text):
    widget.config(state=tk.NORMAL)
    widget.delete("1.0", tk.END)  # Limpa qualquer texto existente
    widget.insert("1.0", text)  # Insere o texto no Entry
    widget.config(state=tk.DISABLED)
def setNormalWidget(widget, text):
    widget.delete("1.0", tk.END)  # Limpa qualquer texto existente
    widget.insert("1.0", text)  # Insere o texto no Entry
def toBytes(hex_data):
    try:
        bytes_data = binascii.unhexlify(hex_data)
        return bytes_data
    except binascii.Error as e:
        return None
def toHex(bytes_data):
   return binascii.hexlify(bytes_data).decode('utf-8')