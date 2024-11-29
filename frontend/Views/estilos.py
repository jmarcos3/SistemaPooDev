import tkinter as tk
from tkinter import ttk

from abc import ABC

class estilos(ABC):
    def __init__(self,root):

        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

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

        self.style.configure("Custom.TButton", font=("Arial", 12))

        self.style.theme_use("default")