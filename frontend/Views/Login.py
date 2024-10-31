# frontend/Views/Login.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import FuncionarioDAO

class LoginApp:
    def __init__(self, root, open_view_callback):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")  # Define o tamanho inicial da janela
        self.center_window()  # Chama a função para centralizar a janela

        self.open_view_callback = open_view_callback
        
        # Inicializando DAOs
        self.funcionario_dao = FuncionarioDAO('db.db')

        # Configuração de estilo de fonte
        font_large = ("Arial", 12, "bold")
        font_medium = ("Arial", 10)

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 10))

        # Espaçamento superior usando um padding vertical (pady)
        self.top_padding = tk.Label(root, text="")  # Label vazio apenas para espaçamento
        self.top_padding.pack(pady=1)  # Adiciona 20 pixels de padding superior

        # Campos de entrada
        self.username_label = tk.Label(root, text="Usuário", font=font_large)
        self.username_label.pack()
        self.username_entry = tk.Entry(root, font=font_medium)
        self.username_entry.pack(pady=5)
        
        self.password_label = tk.Label(root, text="Senha", font=font_large)
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*", font=font_medium)
        self.password_entry.pack(pady=5)
        
        self.login_button = ttk.Button(root, text="Login", style="Custom.TButton", command=self.login)
        self.login_button.pack(pady=8)


    def center_window(self):
        """Centraliza a janela na tela."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Simula consulta ao banco de dados para obter a função
        role = self.funcionario_dao.buscar_funcao(username,password)
        
        if role:
            self.root.destroy()  # Fecha a tela de login
            self.open_view_callback(tk.Tk(), role)  # Abre a view correspondente
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")
