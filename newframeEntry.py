from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk

class FrameEntry(ttk.Frame):
    def __init__(self, parent, encrypt, selectCipher, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.widgets(encrypt, selectCipher)
    def widgets(self, encrypt, selectCipher):
        #Cria  a instacia do botão e define o onClick na função encrypt
        self.botao = Button(self, text="Clique aqui",command = encrypt)
        #define aonde o botão vai ficar no grid
        self.botao.grid(column=0, row=0,ipadx=20,padx=20) 



        opcoes = ["RSA", "AES", "AES RSA"]

        self.combo = ttk.Combobox(self, values=opcoes)
        self.combo.set(opcoes[0])
        self.combo.grid(row=1, column=0)
        self.combo.bind("<<ComboboxSelected>>", selectCipher)  # Associa o evento à função
        
    
    def getEntryText(self):
        return self.entryText.get()