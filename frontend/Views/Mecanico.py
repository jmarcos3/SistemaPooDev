from tkinter import ttk
from .estilos2 import estilos2
from .Abas.revisao import AbaAgenda

class MecanicoApp(estilos2):
    def __init__(self, root):
        super().__init__(root,"mecanico")

        self.aba_agenda = AbaAgenda(root,self.notebook,"mecanico")
        