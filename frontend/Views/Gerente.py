from tkinter import ttk
import tkinter as tk
from .estilos import estilos
from .Abas.moto import AbaMotos
from .Abas.cliente import AbaClientes
from .Abas.venda import AbaVendas
from .Abas.revisao import AbaAgenda
from .Abas.funcionario import AbaFuncionarios

class GerenteApp(estilos):
    def __init__(self, root):
        super().__init__(root)
        
        self.style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Motos", "Clientes", "Vendas", "Agenda de Revisões", "Funcionários"])
        )

        # Métodos de manipulação
        self.aba_motos = AbaMotos(root,self.notebook,"gerente")
        self.aba_clientes = AbaClientes(root,self.notebook)
        self.aba_vendas = AbaVendas(root,self.notebook,"gerente")
        self.aba_agenda = AbaAgenda(root,self.notebook,"gerente")
        self.aba_funcionario = AbaFuncionarios(root,self.notebook)
        

