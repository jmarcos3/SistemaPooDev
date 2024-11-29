import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import FuncionarioDAO

class LoginApp:
    def __init__(self, root, open_view_callback):
        self.root = root
        self.root.title("Login da Concessionária de moto")
        self.center_window()  # Centraliza a janela
        self.root.state('zoomed')
        self.open_view_callback = open_view_callback
        
        # Inicializando DAOs
        self.funcionario_dao = FuncionarioDAO('db.db')

        # Configuração de fontes
        font_large = ("Arial", 16, "bold")
        font_medium = ("Arial", 14)
        
        # Estilos
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14, "bold"), width=20, padding=12, relief="flat", background="#4CAF50", foreground="white")
        style.map("Custom.TButton", background=[("active", "#45a049")])
        
        # Estilo do fundo
        self.root.configure(bg="#f7f7f7")
        
        # Titulo
        self.title_label = tk.Label(root, text="Concessionária de motos", font=("Arial", 24, "bold"), bg="#4CAF50", fg="white", pady=20)
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

        self.login_label = tk.Label(root, text="Acesso ao sistema", font=font_large, bg="#f7f7f7", fg="#333")
        self.login_label.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

        # Espaçamento
        self.top_padding = tk.Label(root, text="", bg="#f7f7f7")
        self.top_padding.grid(row=1, column=0, pady=10)

        # Alinhar os rótulos e campos de entrada
        self.username_label = tk.Label(root, text="Usuário:", font=font_large, bg="#f7f7f7", fg="#333")
        self.username_label.grid(row=2, column=0, padx=20, sticky="e", pady=5)  # Ajustado o espaçamento

        self.username_entry = tk.Entry(root, font=font_medium, bd=2, relief="flat", width=30, highlightbackground="#4CAF50", highlightthickness=2)
        self.username_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")  # Ajuste com padding para aproximar

        self.password_label = tk.Label(root, text="Senha:", font=font_large, bg="#f7f7f7", fg="#333")
        self.password_label.grid(row=3, column=0, padx=20, sticky="e", pady=5)  # Ajustado o espaçamento

        self.password_entry = tk.Entry(root, show="*", font=font_medium, bd=2, relief="flat", width=30, highlightbackground="#4CAF50", highlightthickness=2)
        self.password_entry.grid(row=3, column=1, pady=5, padx=10, sticky="w")  # Ajuste com padding para aproximar

        # Estilos
        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=("Arial", 13, "bold"),
                        width=20,
                        padding=12,
                        relief="flat",
                        background="#4CAF50",  # Cor de fundo
                        foreground="black")  # Cor do texto
        style.map("Custom.TButton",
                background=[("active", "#45a049")],  # Cor do fundo ao passar o mouse
                foreground=[("active", "black")])  # Cor do texto ao passar o mouse

        # Botão de login
        self.login_button = ttk.Button(root, text="Login", style="Custom.TButton", command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=30)


        # Ajustando as colunas para que fiquem centralizadas
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

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
        role = self.funcionario_dao.buscar_funcao(username, password)
        
        if role:
            self.root.destroy()  # Fecha a tela de login
            self.open_view_callback(tk.Tk(), role)  # Abre a view correspondente
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")
