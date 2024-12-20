import tkinter as tk
from frontend.Views.Gerente import GerenteApp
from frontend.Views.Vendedor import VendedorApp
from frontend.Views.Mecanico import MecanicoApp
from frontend.Views.Secretaria import SecretariaApp
from frontend.Views.Login import LoginApp

# Função para abrir a view correta com base no cargo do usuário
def open_view(root, role):
    if role == "Gerente":
        GerenteApp(root)
    elif role == "Vendedor":
        VendedorApp(root)
    elif role == "Mecanico":
        MecanicoApp(root)
    elif role == "Secretaria":
        SecretariaApp(root)

def main():
    root = tk.Tk()
    LoginApp(root, open_view)
    root.mainloop()


if __name__ == "__main__":
    main()


