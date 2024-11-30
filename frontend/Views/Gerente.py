from tkinter import ttk
import tkinter as tk
from .baseTelas import baseTelas
from .Abas.moto import AbaMotos
from .Abas.cliente import AbaClientes
from .Abas.venda import AbaVendas
from .Abas.revisao import AbaAgenda
from .Abas.funcionario import AbaFuncionarios

class GerenteApp(baseTelas):
    def __init__(self, root):
        super().__init__(root,"gerente")

        # Métodos de manipulação
        self.aba_motos = AbaMotos(root,self.notebook,"gerente")
        self.aba_clientes = AbaClientes(root,self.notebook,"gerente")
        self.aba_vendas = AbaVendas(root,self.notebook,"gerente")
        self.aba_agenda = AbaAgenda(root,self.notebook,"gerente")
        self.aba_funcionario = AbaFuncionarios(root,self.notebook,"gerente")
        

