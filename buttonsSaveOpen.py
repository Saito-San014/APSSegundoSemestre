from tkinter import *

def buttonsSaveOpen(self, open, save, frame, widget):
    self.buttonBrowser = Button(frame, text="Selecionar", command=lambda : open(widget))
    self.buttonBrowser.pack(side=TOP, pady=2)
    self.buttonSaveAs= Button(frame, text="Salvar como", command=lambda : save(widget))
    self.buttonSaveAs.pack(side=TOP, pady=2)
