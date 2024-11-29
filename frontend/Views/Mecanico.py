from tkinter import ttk
from .estilos import estilos
from .Abas.revisao import AbaAgenda

class MecanicoApp(estilos):
    def __init__(self, root):
        super().__init__(root)

        self.style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Agenda de Revisões"])
        )

        self.aba_agenda = AbaAgenda(root,self.notebook,"mecanico")
        