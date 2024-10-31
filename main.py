import tkinter as tk
from tkinter import ttk
from frontend.Views.Gerente import GerenteApp
from frontend.Views.Vendedor import VendedorApp
from frontend.Views.Mecanico import MecanicoApp
from frontend.Views.Secretaria import SecretariaApp
from frontend.Views.Login import LoginApp  # Importa a tela de login

# Função para abrir a view correta com base na função do usuário
def open_view(root, role):
    if role == "Gerente":
        GerenteApp(root)
    elif role == "Vendedor":
        VendedorApp(root)
    elif role == "Mecanico":
        MecanicoApp(root)
    elif role == "Secretaria":
        SecretariaApp(root)

# Iniciando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    #app = GerenteApp(root)
    app = LoginApp(root, open_view)  # Passa a função para abrir a view correta
    root.mainloop()


# adicionar funções para o mecanico, ex: atualizar custo e status
# sistema de envio de email