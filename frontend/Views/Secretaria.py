from tkinter import ttk
from .estilos import estilos
from .Abas.moto import AbaMotos
from .Abas.venda import AbaVendas
from .Abas.revisao import AbaAgenda

class SecretariaApp(estilos):
    def __init__(self, root):
        super().__init__(root)

        self.style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Motos", "Vendas", "Agenda de Revisões"]))
        
        
        self.aba_motos = AbaMotos(root,self.notebook,"secretaria")
        self.aba_vendas = AbaVendas(root,self.notebook,"secretaria")
        self.aba_agenda = AbaAgenda(root,self.notebook,"secretaria")
