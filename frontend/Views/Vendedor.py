from tkinter import ttk
from .estilos import estilos
from .Abas.venda import AbaVendas
from .Abas.cliente import AbaClientes
from .Abas.moto import AbaMotos

class VendedorApp(estilos):
    def __init__(self, root):
        super().__init__(root)

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14, "bold"))
        style.theme_use("default")
        style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Motos", "Clientes", "Vendas"])
        )
        self.aba_motos = AbaMotos(root,self.notebook,"vendedor")
        self.aba_cliente = AbaClientes(root,self.notebook)
        self.aba_venda = AbaVendas(root,self.notebook,"vendedor")