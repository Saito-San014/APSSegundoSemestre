from tkinter import *

def buttonsSaveAsOpenFile(self, open_file_dialog, saveAs):
    self.buttonBrowserPrivateKey = Button(self.framePrivateKeyButtons, text="Selecionar", command=lambda widget = self.textBoxPrivateKey : open_file_dialog(widget))
    self.buttonBrowserPrivateKey.pack(side=TOP, pady=2)
    self.buttonSaveAsPrivateKey = Button(self.framePrivateKeyButtons, text="Salvar como", command=lambda widget = self.textBoxPrivateKey : saveAs(widget))
    self.buttonSaveAsPrivateKey.pack(side=TOP, pady=2)
    
    self.buttonBrowserPublicKey = Button(self.framePublicKeyButtons, text="Selecionar", command=lambda widget = self.textBoxPublicKey : open_file_dialog(widget))
    self.buttonBrowserPublicKey.pack(side=TOP, pady=2)
    self.buttonSaveAsPublicKey = Button(self.framePublicKeyButtons, text="Salvar como", command=lambda widget = self.textBoxPublicKey : saveAs(widget))
    self.buttonSaveAsPublicKey.pack(side=TOP, pady=2)

    self.buttonBrowserDecode = Button(self.frameDecodeButtons, text="Selecionar", command=lambda widget=self.textBoxDecode : open_file_dialog(widget))
    self.buttonBrowserDecode.pack(side=TOP, pady=2)
    self.buttonSaveAsDecode = Button(self.frameDecodeButtons, text="Salvar como", command=lambda widget = self.textBoxDecode : saveAs(widget))
    self.buttonSaveAsDecode.pack(side=TOP, pady=2)

    self.buttonBrowserEncodeText = Button(self.frameEncodeButtons, text="Selecionar", command=lambda widget=self.textBoxEncode : open_file_dialog(widget))
    self.buttonBrowserEncodeText.pack(side=TOP, pady=2)
    self.buttonSaveAsEncode = Button(self.frameEncodeButtons, text="Salvar como", command=lambda widget = self.textBoxEncode : saveAs(widget))
    self.buttonSaveAsEncode.pack(side=TOP, pady=2)