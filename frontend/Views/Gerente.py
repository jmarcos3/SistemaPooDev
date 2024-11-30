from tkinter import ttk
import tkinter as tk
from .estilos2 import estilos2
from .Abas.moto import AbaMotos
from .Abas.cliente import AbaClientes
from .Abas.venda import AbaVendas
from .Abas.revisao import AbaAgenda
from .Abas.funcionario import AbaFuncionarios

class GerenteApp(estilos2):
    def __init__(self, root):
        super().__init__(root,"gerente")

        # Métodos de manipulação
        self.aba_motos = AbaMotos(root,self.notebook,"gerente")
        self.aba_clientes = AbaClientes(root,self.notebook,"gerente")
        self.aba_vendas = AbaVendas(root,self.notebook,"gerente")
        self.aba_agenda = AbaAgenda(root,self.notebook,"gerente")
        self.aba_funcionario = AbaFuncionarios(root,self.notebook,"gerente")
        

