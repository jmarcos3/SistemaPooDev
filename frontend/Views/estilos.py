import tkinter as tk
from tkinter import ttk

from abc import ABC

class estilos(ABC):
    def __init__(self,root):

        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        # # Definindo o cargo
        # cargos = {
        #     "gerente": "Gerente",
        #     "vendedor": "Vendedor",
        #     "mecanico": "Mecânico",
        #     "secretaria": "Secretária"
        # }

        # cargo_nome = cargos.get(cargo, "Cargo não encontrado")

        # # Adicionando título com o cargo
        # self.title_label = tk.Label(
        #     root,
        #     text=f"Concessionária de motos - Cargo: {cargo_nome}",
        #     font=("Arial", 18, "bold"),
        #     bg="#4CAF50",
        #     fg="white",
        #     pady=0
        # )

        #self.title_label.pack(fill="x")
        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="none", expand=False)

        # Estilos personalizados
        self.estilo_label = {"font": ("Arial", 16, "bold"), "foreground": "#333"}
        self.estilo_entrada = {"width": 25, "font": ("Arial", 14)}

        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=("Arial", 14))

        # Estilo para o botão de deslogar
        self.style.configure("TButton", font=("Arial", 12), padding=5)

        # No construtor da classe AbaMotos, configure o estilo
        self.style.configure("TCombobox", selectbackground="white", selectforeground="black")

# 