import tkinter as tk
from tkinter import ttk
from frontend.Views.Gerente import GerenteApp
from frontend.Views.Vendedor import VendedorApp
from frontend.Views.Mecanico import MecanicoApp
from frontend.Views.Secretaria import SecretariaApp


# Iniciando a aplicação
if __name__ == "__main__":
    root = tk.Tk() 
    app = GerenteApp(root)
    root.mainloop()
