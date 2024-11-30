from tkinter import ttk
from tkinter import messagebox
from abc import ABC
import subprocess



class estilos2(ABC):
    def __init__(self,root,cargo):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        if cargo == "gerente":
            abas =  len(["Motos", "Clientes", "Vendas", "Agenda de Revisões", "Funcionários"])
        elif cargo == "mecanico":
            abas =  len(["Agenda de Revisões"])
        elif cargo == "secretaria":
            abas = len(["Motos", "Vendas", "Agenda de Revisões"])
        elif cargo == "vendedor":
            abas = len(["Motos", "Clientes", "Vendas"])
            

        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)


        self.style = ttk.Style()


        self.style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // abas
        )
