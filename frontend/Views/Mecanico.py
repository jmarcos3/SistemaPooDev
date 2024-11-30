from tkinter import ttk
from .baseTelas import baseTelas
from .Abas.revisao import AbaAgenda

class MecanicoApp(baseTelas):
    def __init__(self, root):
        super().__init__(root,"mecanico")

        self.aba_agenda = AbaAgenda(root,self.notebook,"mecanico")
        