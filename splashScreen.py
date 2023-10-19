from tkinter import *
import time
from tkinter import ttk

def splashScreen():
    root = Tk()
    root.geometry("600x300")
    largura_janela = 600
    altura_janela = 300
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    root.overrideredirect(True)
    slapshLabel = Label(root, text="APS\nAlgoritimos de criptogafia", font=("Arial", 30))
    slapshLabel.pack(side= TOP, pady=30)
    progresso = ttk.Progressbar(root, length=600, mode="determinate")
    progresso.pack(side=TOP, pady=20)
    for i in range(101):
        progresso['value'] = i
        root.update()
        # Simule algum trabalho
        root.after(25)


    root.destroy()

    root.mainloop()