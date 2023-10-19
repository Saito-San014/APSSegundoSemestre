from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from buttonsSaveOpen import buttonsSaveOpen
from cryptograms import cipherAES
from labelsAES import LabelsAES

cAES = cipherAES()

class FrameAES(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.columnconfigure(1, weight=1)
        self.parent = parent
        self.widgets()
        
    def widgets(self):
        def open_file_dialog(widget):
            file_types = [("Arquivos de Texto", "*.txt")]
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
                        if widget == self.textBoxPublicKey:
                            cAES.setKey(conteudo.encode('utf-8'))
                except FileNotFoundError:            
                    print("O arquivo não foi encontrado.")
                except Exception as e:
                    print(f"Ocorreu um erro: {str(e)}")
        def saveAs(widget):
            file_types = [("Arquivos de Texto", "*.txt")]
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
        LabelsAES(self)
        textTeste = """inicio: idfhsaduifhuishh8asgfgv78sehy89vehy78tvr7hyew89hreytv78hy98j0y78y8aucwhtrv78yhqqwtyhrv6wh64rvw6b64r6vw46rw64h6rvhw46ht6wt8w7tv6wvt6hw48t6hw486thvw46vtw46htw46hvtvehtrv9w47thv98t98qwv0b98bqy04tvb8w4vt0vt4w4tvyvq9y08bwtv890bqwytvb80wybqrbbyvwq4ty4vttttttqw4tvbwt0tq4vbvyw4tby8"""

        self.textFrameDecode = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.textFrameDecode.grid(row=0, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        self.textBoxDecode = Text(self.textFrameDecode, height=10, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxDecode.pack(expand=True, fill=X,padx=10,pady=5)

        self.textBoxDecode.bind("<Button-1>", on_click)

        self.framePublicKey = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.framePublicKey.grid(row=1, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 5, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.textBoxPublicKey = Text(self.framePublicKey, height=5, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxPublicKey.pack(expand=True, fill=X,padx=10,pady=5)

        self.textFrameEncode = Frame(self, borderwidth=1, relief=tk.SOLID, background='white')
        self.textFrameEncode.grid(row=2, column=1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        self.textBoxEncode = Text(self.textFrameEncode, height=5, width=100,borderwidth=0,relief=tk.FLAT)
        self.textBoxEncode.pack(expand=True, fill=X,padx=10,pady=5)

        self.textBoxEncode.bind("<Button-1>", on_click)

        self.frameDecodeButtons = Frame(self,width=30, background="black")
        self.frameDecodeButtons.grid(row=0,column=2, padx=20)

        self.framePublicKeyButtons = Frame(self,width=30, background="black")
        self.framePublicKeyButtons.grid(row=1,column=2, padx=20)
        
        self.frameEncodeButtons = Frame(self,width=30, background="black")
        self.frameEncodeButtons.grid(row=2,column=2, padx=20)

        buttonsSaveOpen(self, open_file_dialog, saveAs, self.frameDecodeButtons, self.textBoxDecode)
        buttonsSaveOpen(self, open_file_dialog, saveAs, self.frameEncodeButtons, self.textBoxEncode)
        buttonsSaveOpen(self, open_file_dialog, saveAs, self.framePublicKeyButtons, self.textBoxPublicKey)
    def encrypt_decrypt(self):
        global cAES
        if self.textBoxEncode.cget("state") == tk.DISABLED:
            if self.textBoxPublicKey.get("1.0", "end-1c") == "":
                cAES = cipherAES()
                set_text(self.textBoxPublicKey, cAES.key)
                encodeText = cAES.encrypt(self.textBoxDecode.get("1.0","end-1c"))
                set_text(self.textBoxEncode, encodeText)
            else:
                encodeText = cAES.encrypt(self.textBoxDecode.get("1.0","end-1c"))
                set_text(self.textBoxEncode, encodeText)
        elif self.textBoxDecode.cget("state") == tk.DISABLED:
            if self.textBoxPublicKey.get("1.0", "end-1c") != "":
                encodeText = self.textBoxEncode.get("1.0","end-1c")
                decodeText = cAES.decrypt(encodeText.encode('utf-8'))
                set_text(self.textBoxDecode, decodeText)

def set_text(widget, text):
    if widget.cget("state") == tk.DISABLED:
        widget.config(state=tk.NORMAL)
        widget.delete("1.0", tk.END)  # Limpa qualquer texto existente
        widget.insert("1.0", text)  # Insere o texto no Entry
        widget.config(state=tk.DISABLED)
    else:
        widget.delete("1.0", tk.END)  # Limpa qualquer texto existente
        widget.insert("1.0", text)  # Insere o texto no Entry