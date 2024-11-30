from tkinter import ttk
from tkinter import messagebox
from abc import ABC
import subprocess



class estilos(ABC):
    def __init__(self):

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



    def sair(self):
        resposta = messagebox.askyesno("Sair", "Você tem certeza que deseja sair?")
        if resposta:
            # Fechar a janela principal ou redirecionar para a tela de login
            self.root.destroy()
            subprocess.Popen(["python","main.py"])
