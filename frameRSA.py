from tkinter import *
from tkinter import font
class FrameRSA(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.columnconfigure(1, weight=1)
        self.parent = parent
        self.widgets()
        
    def widgets(self):
        #Labels para nomear a informações
        fontLabelText = font.Font(family="Arial", size=12)
        fontLabel = font.Font(family="Arial", size=12)
        #Largura do label em quantidade de caracteresfontLabelText
        widthLabel = 150
        largura_caractere = fontLabel.measure("A") 
        fontSizeLabels = 8
        wrapLength = largura_caractere * (widthLabel-40)     
        self.labelTextPublicKey = Label(self, text= "Chave publica",background='cyan', font=fontLabel , relief="groove", anchor="center")
        self.labelTextPublicKey.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelTextPrivateKey = Label(self, text= "Chave privada",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
        self.labelTextPrivateKey.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelTextEncodeText = Label(self, text= "Texto Criptogafado",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
        self.labelTextEncodeText.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelTextDecodeText = Label(self, text= "Texto original",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
        self.labelTextDecodeText.grid(row = 3, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelPublicKey = Label(self, wraplength=wrapLength,text="" , background="green", font=fontLabel,height=5,width=widthLabel, anchor="center",justify=LEFT)
        self.labelPublicKey.grid(row = 0, column = 1, padx = 0, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        
        self.labelPrivateKey = Label(self, wraplength=wrapLength,text="", background="green", font=fontLabel,height=10,width=widthLabel, anchor="center",justify=LEFT)
        self.labelPrivateKey.grid(row = 1, column = 1, padx = 0, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelEncodeText = Label(self, wraplength=wrapLength,text="", background="green", font=fontLabel,height=5,width=widthLabel, anchor="center",justify=LEFT)
        self.labelEncodeText.grid(row = 2, column = 1, padx = 0, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelDecodeText = Label(self, wraplength=wrapLength,text="", background="green", font=fontLabel,height=5,width=widthLabel, anchor="center",justify=LEFT)
        self.labelDecodeText.grid(row = 3, column = 1, padx = 0, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
    def setLabels(self, texts):
        self.labelPublicKey.configure(text=str(texts[0]))
        self.labelPrivateKey.configure(text=str(texts[1]))
        self.labelEncodeText.configure(text=str(texts[2]))
        self.labelDecodeText.configure(text=str(texts[3]))