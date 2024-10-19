import tkinter as tk
from tkinter import ttk
from frontend.Views.Gerente import GerenteApp


# Iniciando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = GerenteApp(root)
    root.mainloop()
