from tkinter import ttk, Label
from abc import ABC

class baseTelas(ABC):
    def __init__(self,root,cargo):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        if cargo == "Login":
            pass
        else:
            self.titulo = Label(
                self.root,
                text=f"Sistema de Controle de Motos - Cargo: {cargo.capitalize()}",
                font=("Arial", 16, "bold"),
                bg="#4CAF50",
                fg="white"
            )
            self.titulo.pack(side="top", fill="x")

            if cargo == "gerente":
                abas = self.root.winfo_screenwidth() // len(["Motos", "Clientes", "Vendas", "Agenda de Revisões", "Funcionários"])
            elif cargo == "mecânico":
                abas =  self.root.winfo_screenwidth() // len(["Agenda de Revisões"])
            elif cargo == "secretária":
                abas = self.root.winfo_screenwidth() // len(["Motos", "Vendas", "Agenda de Revisões"])
            elif cargo == "vendedor":
                abas = self.root.winfo_screenwidth() // len(["Motos", "Clientes", "Vendas"])
                

            self.style = ttk.Style()

            self.style.configure("TNotebook.Tab",
                font=("Arial", 500, "bold"),
                width = abas
            )

            # Criando o notebook (abas)
            self.notebook = ttk.Notebook(self.root)
            self.notebook.pack(fill="both", expand=True)


