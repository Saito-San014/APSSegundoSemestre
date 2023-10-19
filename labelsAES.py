from tkinter import *
from tkinter import font
        
def LabelsAES(self):
    #Labels para nomear a informações
    self.labelTextDecodeText = Label(self, text= "Texto original",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
    self.labelTextDecodeText.grid(row = 0, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
        
    self.labelTextPublicKey = Label(self, text= "Chave publica",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
    self.labelTextPublicKey.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')

    self.labelTextEncodeText = Label(self, text= "Texto Criptogafado",background='cyan', font=("Arial", 16),borderwidth=2, relief="groove", anchor="center")
    self.labelTextEncodeText.grid(row = 2, column = 0, padx = 5, pady = 5, ipadx = 0, ipady = 0, rowspan = 1, columnspan = 1, sticky = 'NSEW')
