from tkinter import ttk
from .baseTelas import baseTelas
from .Abas.venda import AbaVendas
from .Abas.cliente import AbaClientes
from .Abas.moto import AbaMotos

class VendedorApp(baseTelas):
    def __init__(self, root):
        super().__init__(root,"vendedor")

        self.aba_motos = AbaMotos(root,self.notebook,"vendedor")
        self.aba_cliente = AbaClientes(root,self.notebook, "vendedor")
        self.aba_venda = AbaVendas(root,self.notebook,"vendedor")
