from tkinter import ttk
from .estilos2 import estilos2
from .Abas.venda import AbaVendas
from .Abas.cliente import AbaClientes
from .Abas.moto import AbaMotos

class VendedorApp(estilos2):
    def __init__(self, root):
        super().__init__(root,"vendedor")

        self.aba_motos = AbaMotos(root,self.notebook,"vendedor")
        self.aba_cliente = AbaClientes(root,self.notebook, "vendedor")
        self.aba_venda = AbaVendas(root,self.notebook,"vendedor")
