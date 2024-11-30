from tkinter import ttk
from .estilos2 import estilos2
from .Abas.moto import AbaMotos
from .Abas.venda import AbaVendas
from .Abas.revisao import AbaAgenda

class SecretariaApp(estilos2):
    def __init__(self, root):
        super().__init__(root,"secretaria")
    
        self.aba_motos = AbaMotos(root,self.notebook,"secretaria")
        self.aba_vendas = AbaVendas(root,self.notebook,"secretaria")
        self.aba_agenda = AbaAgenda(root,self.notebook,"secretaria")
