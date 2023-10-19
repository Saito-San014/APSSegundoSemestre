from tkinter import *
from tkinter import font

class FrameAES(Frame):
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
        self.labelTextPublicKey = Label(self, text= "Chave publica",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
        self.labelTextPublicKey.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelTextEncodeText = Label(self, text= "Texto Criptogafado",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
        self.labelTextEncodeText.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelTextDecodeText = Label(self, text= "Texto original",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
        self.labelTextDecodeText.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        
        textTeste = """inicio: idfhsaduifhuishh8asgfgv78sehy89vehy78tvr7hyew89hreytv78hy98j0y78y8aucwhtrv78yhqqwtyhrv6wh64rvw6b64r6vw46rw64h6rvhw46ht6wt8w7tv6wvt6hw48t6hw486thvw46vtw46htw46hvtvehtrv9w47thv98t98qwv0b98bqy04tvb8w4vt0vt4w4tvyvq9y08bwtv890bqwytvb80wybqrbbyvwq4ty4vttttttqw4tvbwt0tq4vbvyw4tby8"""

        self.labelPublicKey = Label(self, wraplength=wrapLength,text=textTeste, background="green", font=fontLabel,height=5,width=widthLabel, anchor="center",justify=LEFT)
        self.labelPublicKey.grid(row = 0, column = 1, padx = 5, pady = 5, ipadx = 20, ipady = 20, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelEncodeText = Label(self, wraplength=wrapLength,text="", background="green", font=("Arial", fontSizeLabels),borderwidth=2,height=5,width=20, relief="groove", anchor="center")
        self.labelEncodeText.grid(row = 1, column = 1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

        self.labelDecodeText = Label(self, wraplength=wrapLength,text="", background="green", font=("Arial",fontSizeLabels),borderwidth=2,height=5,width=20, relief="groove",)
        self.labelDecodeText.grid(row = 2, column = 1, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
    
    def setLabels(self, texts):
        self.labelPublicKey.configure(text=str(texts[0]))
        self.labelEncodeText.configure(text=str(texts[1]))
        self.labelDecodeText.configure(text=str(texts[2]))