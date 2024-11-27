from tkinter import ttk
from .telas import telas

class MecanicoApp(telas):
    def __init__(self, root):
        super().__init__(root, "mecanico")

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14, "bold"))
        style.theme_use("default")
        style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Agenda de Revisões"])
        )

        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Configurando pesos para centralizar
        self.tab_agenda.columnconfigure(0, weight=1)
        self.tab_agenda.columnconfigure(1, weight=1)
        for i in range(8):  # Número de linhas usadas
            self.tab_agenda.rowconfigure(i, weight=1)

        # Seção para listar revisões
        label_listar_funcionarios = ttk.Label(self.tab_agenda, text="Revisões Agendadas", **self.estilo_label)
        label_listar_funcionarios.grid(row=0, column=0, columnspan=2, pady=(5, 15))


        # Criando o Treeview para listar
        colunas = ('ID', 'Chassi', 'Data', 'CPF', 'Status', 'Custo')
        self.tree_revisao = ttk.Treeview(self.tab_agenda, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_revisao.heading('ID', text='ID Manutenção')
        self.tree_revisao.heading('Chassi', text='Chassi')
        self.tree_revisao.heading('Data', text='Data')
        self.tree_revisao.heading('CPF', text='CPF')
        self.tree_revisao.heading('Status', text='Status')
        self.tree_revisao.heading('Custo', text='Custo')

        # Ajustar o tamanho das colunas dinamicamente
        for col in colunas:
            self.tree_revisao.column(col, anchor='center', width=150)

        # Posicionar o Treeview
        self.tree_revisao.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        
        btn_editar_revisao = ttk.Button(self.tab_agenda, text="Editar revisão", style="Custom.TButton", command=self.editar_revisao)
        btn_editar_revisao.grid(row=2, column=0, pady=10, sticky="n")

        # # Adicionando barra de rolagem vertical
        # scrollbar_vertical = ttk.Scrollbar(self.tab_agenda, orient="vertical", command=self.tree.yview)
        # self.tree.configure(yscroll=scrollbar_vertical.set)
        # scrollbar_vertical.grid(row=1, column=2, sticky="ns")

        # # Adicionando barra de rolagem horizontal
        # scrollbar_horizontal = ttk.Scrollbar(self.tab_agenda, orient="horizontal", command=self.tree.xview)
        # self.tree.configure(xscroll=scrollbar_horizontal.set)
        # scrollbar_horizontal.grid(row=2, column=0, columnspan=2, sticky="ew")

        # Atualiza as revisões na inicialização
        self.listar_revisoes()
