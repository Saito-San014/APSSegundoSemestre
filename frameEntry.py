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

        
        def set_text(text):
            self.entryText.delete(0, tk.END)  # Limpa qualquer texto existente
            self.entryText.insert(0, text)  # Insere o texto no Entry
            encrypt()
        #Cria o label e o posiciona no grid 
        self.labelEntry = Label(self, text= "Digite o texto que sera criptografado")
        self.labelEntry.grid(column=0, row=0, pady=20, padx=10, ipadx=20, ipady=10)
        #Cria o input de entrada para o usuairo digitar
        self.entryText = Entry(self, width=30)
        #Posiciona no grid
        #PS. não pode ser como no label, pois quando for utilizar get() ira return null
        self.entryText.grid(column=1,row=0,padx=10)


        #Cria  a instacia do botão e define o onClick na função encrypt
        self.botao = Button(self, text="Clique aqui",command = encrypt)
        #define aonde o botão vai ficar no grid
        self.botao.grid(column=2, row=0,ipadx=20,padx=20) 

        self.buttonBrowser = Button(self, text="Selecionar", command=open_file_dialog)
        self.buttonBrowser.grid(row=1,column=1)

        opcoes = ["RSA", "AES", "AES RSA"]

        self.combo = ttk.Combobox(self, values=opcoes)
        self.combo.set(opcoes[0])
        self.combo.grid(row=1, column=0)
        self.combo.bind("<<ComboboxSelected>>", selectCipher)  # Associa o evento à função
        
    
    def getEntryText(self):
        return self.entryText.get()