import binascii
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from buttonsSaveOpen import  buttonsSaveOpen  
from cryptograms import cipherRSA
from labelsRSA import LabelsRSA

cRSA = cipherRSA()

class FrameRSA(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.columnconfigure(1, weight=1)
        self.parent = parent
        self.widgets()
        
    def widgets(self):
        
        def open_file_dialog(widget):
            if widget == self.textBoxDecode or widget == self.textBoxEncode:
                file_types = [("Arquivos de Texto", "*.txt")]
            elif widget == self.textBoxPrivateKey or widget == self.textBoxPublicKey:
                file_types = [("Arquivos de Texto e PEM", ("*.txt", "*.pem"))]
            file_path = filedialog.askopenfilename(
                #initialdir="/",  # Diretório inicial (pode ser alterado)
                title="Selecione um arquivo de texto",
                filetypes=(file_types)
            )
            if file_path:
                # O usuário selecionou um arquivo, você pode fazer algo com o caminho do arquivo aqui
                print("Arquivo selecionado:", file_path)
                try:
                    with open(file_path, 'r') as arquivo:
                        conteudo = arquivo.read()
                        select_widget(widget)
                        set_text(widget, conteudo)
                        if widget == self.textBoxPrivateKey: 
                            result = cRSA.setPrivateKey(conteudo)
                            if result == None:
                                set_text(self.textBoxPublicKey, cRSA.getPublicKey())
                            else:
                                messagebox.showinfo("Falha ao descriptografar", f"Chave privada corrompida \n {result}")
                except FileNotFoundError:
                    print("O arquivo não foi encontrado.")
                except Exception as e:
                    print(f"Ocorreu um erro: {str(e)}")
        def saveAs(widget):
            if widget == self.textBoxDecode or widget == self.textBoxEncode:
                file_types = [("Arquivos de Texto", "*.txt")]
            elif widget == self.textBoxPrivateKey or widget == self.textBoxPublicKey:
                file_types = [("Arquivos de Texto e PEM", ("*.txt", "*.pem"))]
            file = filedialog.asksaveasfile(
                defaultextension=".pem",
                filetypes=file_types)
            if file:
                conteudo = widget.get("1.0", "end-1c")
                file.write(conteudo)
                file.close()
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

        LabelsRSA(self)

        self.textFrameDecode = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.textFrameDecode.grid(row=0, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        self.textBoxDecode = Text(self.textFrameDecode, height=10, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxDecode.pack(expand=True, fill=X,padx=10,pady=5)
        
        self.textBoxDecode.bind("<Button-1>", on_click)

        self.framePrivateKey = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.framePrivateKey.grid(row=1, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 5, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        
        self.textBoxPrivateKey = Text(self.framePrivateKey, height=10, width=100,borderwidth=0,relief=tk.FLAT)
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

        self.frameDecodeButtons = Frame(self,width=30, background='white')
        self.frameDecodeButtons.grid(row=0,column=2, padx=20)
        
        self.framePrivateKeyButtons = Frame(self,width=30, background='white')
        self.framePrivateKeyButtons.grid(row=1,column=2, padx=20)

        self.framePublicKeyButtons = Frame(self,width=30, background='white')
        self.framePublicKeyButtons.grid(row=2,column=2, padx=20)
        
        self.frameEncodeButtons = Frame(self,width=30, background='white')
        self.frameEncodeButtons.grid(row=3,column=2, padx=20)

        buttonsSaveOpen(self, open_file_dialog, saveAs, self.frameDecodeButtons, self.textBoxDecode)
        buttonsSaveOpen(self, open_file_dialog, saveAs, self.frameEncodeButtons, self.textBoxEncode)
        buttonsSaveOpen(self, open_file_dialog, saveAs, self.framePrivateKeyButtons, self.textBoxPrivateKey)
        buttonsSaveOpen(self, open_file_dialog, saveAs, self.framePublicKeyButtons, self.textBoxPublicKey)


    def encrypt_decrypt(self):
        #Se for encriptar
        global cRSA
        if self.textBoxEncode.cget("state") == tk.DISABLED:
            if self.textBoxPublicKey.get("1.0", "end-1c") != "" and self.textBoxPrivateKey.get(1.0,"end-1c") == "":
                result = cRSA.setPublicKey(self.textBoxPublicKey.get(1.0, "end-1c"))
                if result == None:
                    encodeText = cRSA.encrypt(self.textBoxDecode.get("1.0","end-1c"))
                    set_text(self.textBoxEncode, toHex(encodeText))            
            elif self.textBoxPrivateKey.get(1.0,"end-1c") == "":
                cRSA = cipherRSA()
                set_text(self.textBoxPrivateKey, cRSA.getPrivateKey())
                set_text(self.textBoxPublicKey, cRSA.getPublicKey())
                encodeText = cRSA.encrypt(self.textBoxDecode.get("1.0","end-1c"))
                set_text(self.textBoxEncode, toHex(encodeText))
            else:
                result = cRSA.setPrivateKey(self.textBoxPrivateKey.get(1.0,"end-1c"))
                if result == None:
                    set_text(self.textBoxPublicKey, cRSA.getPublicKey())
                    encodeText = cRSA.encrypt(self.textBoxDecode.get("1.0","end-1c"))
                    set_text(self.textBoxEncode, toHex(encodeText))            
                else:
                    messagebox.showinfo("Falha ao criptografar", "Chave privada corrompida")
        elif self.textBoxDecode.cget("state") == tk.DISABLED:
            if self.textBoxPrivateKey.get(1.0,"end-1c") == "":
                messagebox.showinfo("Falha ao descriptografar", "Falta a chave privada")
            else:
                encodeText = self.textBoxEncode.get("1.0","end-1c")
                bytes_data = toBytes(encodeText.replace(" ", "").replace("\n", "").replace("\t", ""))
                result = cRSA.setPrivateKey(self.textBoxPrivateKey.get(1.0, "end-1c"))
                if result == None:
                    decodeText = cRSA.decrypt(bytes_data)
                    if decodeText == None:
                        messagebox.showinfo("Falha ao descriptografar", "Chave privada corrompida")
                    else:
                        set_text(self.textBoxDecode, decodeText)
                else:
                    messagebox.showinfo("Falha ao descriptografar", "Chave privada corrompida")

def set_text(widget, text):
    if widget.cget("state") == tk.DISABLED:
        widget.config(state=tk.NORMAL)
        widget.delete("1.0", tk.END)  # Limpa qualquer texto existente
        widget.insert("1.0", text)  # Insere o texto no Entry
        widget.config(state=tk.DISABLED)
    else:
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