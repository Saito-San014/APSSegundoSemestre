from config import config
try:
    import rsa
    import cryptography
    print("As bibliotecas estao ok!")
except ImportError as e :
    print(e)
    print(str(e)[16:].replace("'", "")," install start")
    config(str(e)[16:].replace("'", ""))

from frameAES import FrameAES
from frameEntry import FrameEntry
from cryptograms import *
from frameRSA import FrameRSA


from tkinter import *
from tkinter import ttk

cryptType = "RSA"

class MainW(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.mainWidgets()
        #Define um titulo para a janela do Tkinter
        self.title("APS - Criptografia")
        #Define o tamanho da janela
        self.geometry('1980x1080')
        #Maximiza a janela
        self.state('zoomed')
        self.configure(background='white')
    def mainWidgets(self):
        #Metodo executado ao clicar no botão enviar
        def encrypt():
            global cryptType
            if cryptType == "RSA":
                self.frameRSA.encrypt_decrypt()
            elif cryptType == "AES":
                self.frameAES.encrypt_decrypt()
        def selectCipher(event):
            global cryptType
            opcao = self.frameEntry.combo.get()
            print(opcao)
            match(opcao):
                case "RSA":
                    cryptType = opcao
                case "AES":
                    cryptType = opcao
                case _:
                    pass
            updateState(self)
        
        def updateState(self):
            global cryptType
            if(cryptType == "RSA"):
                self.frameRSA.pack(side=TOP, padx=20, pady=20, before=self.frameEntry)
                self.frameAES.pack_forget()
            elif(cryptType == "AES"):
                self.frameAES.pack(side=TOP, padx=20, pady=20, before=self.frameEntry)
                self.frameRSA.pack_forget()

        self.frameEntry = FrameEntry(self, encrypt,selectCipher, style='My.TFrame')
        self.frameEntry.pack(side=TOP, pady=0)
        
        self.frameRSA = FrameRSA(self)
        
        self.frameAES = FrameAES(self)

        updateState(self)
        

if __name__=="__main__":
    app = MainW(None)
    s = ttk.Style()
    s.configure('My.TFrame', background='red')
    app.mainloop()