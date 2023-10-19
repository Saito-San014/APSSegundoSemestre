from tkinter import *
from tkinter import font
        
def LabelsRSA(self):
    #Labels para nomear a informações
    fontLabel = font.Font(family="Arial", size=16)
    #Largura do label em quantidade de caracteresfontLabelText   
    
    self.labelTextDecodeText = Label(self, text= "Texto original", background='cyan', font=fontLabel,borderwidth=0,  relief="groove", anchor="center")
    self.labelTextDecodeText.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
    
    self.labelTextPrivateKey = Label(self, text= "Chave privada",background='cyan', font=fontLabel,borderwidth=0, relief="groove", anchor="center")
    self.labelTextPrivateKey.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

    self.labelTextPublicKey = Label(self, text= "Chave publica",background='cyan', font=fontLabel, borderwidth=0, relief="groove", anchor="center")
    self.labelTextPublicKey.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

    self.labelTextEncodeText = Label(self, text= "Texto Criptogafado",background='cyan', font=fontLabel,borderwidth=0, relief="groove", anchor="center")
    self.labelTextEncodeText.grid(row = 3, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
