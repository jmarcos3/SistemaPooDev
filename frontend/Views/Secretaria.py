from tkinter import ttk
from .telas import telas

class SecretariaApp(telas):
    def __init__(self, root):
        super().__init__(root, "secretaria")

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12))
        style.theme_use("default")
        style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Motos", "Vendas", "Agenda de Revisões"]))
        
        #///////////////////////////////////////////////////////////////////////////
        
        # Aba de Motos
        self.tab_motos = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_motos, text="Motos")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_motos.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_motos.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_motos.rowconfigure(row, weight=1) 

        # Seção para listar 
        label_listar_funcionarios = ttk.Label(self.tab_motos, text="Motos Cadastradas", **self.estilo_label)
        label_listar_funcionarios.grid(row=0, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar 
        colunas = ('Chassi', 'Ano', 'Preço', 'Cor','Modelo')
        self.tree_moto = ttk.Treeview(self.tab_motos, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_moto.heading('Chassi', text='Chassi')
        self.tree_moto.heading('Ano', text='Ano')
        self.tree_moto.heading('Preço', text='Preço')
        self.tree_moto.heading('Cor', text='Cor')
        self.tree_moto.heading('Modelo', text='Modelo')

        # Ajustar o tamanho das colunas
        self.tree_moto.column('Chassi', width=150)
        self.tree_moto.column('Ano', width=120)
        self.tree_moto.column('Preço', width=100)
        self.tree_moto.column('Cor', width=100)
        self.tree_moto.column('Modelo', width=100)

        # Posicionar o Treeview
        self.tree_moto.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
             
        self.listar_motos()

        # ////////////////////////////////////////////////////////////////////////////

        # Aba de Vendas
        self.tab_venda = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_venda, text="Vendas")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_venda.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_venda.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_venda.rowconfigure(row, weight=1) 


        # Seção para listar 
        label_listar_funcionarios = ttk.Label(self.tab_venda, text="Lista de Vendas", **self.estilo_label)
        label_listar_funcionarios.grid(row=0, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar 
        colunas = ('ID','Chassi', 'CPF', 'Data', 'Status', 'Preço')
        self.tree = ttk.Treeview(self.tab_venda, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree.heading('ID', text='ID Venda')
        self.tree.heading('Chassi', text='Chassi')
        self.tree.heading('CPF', text='CPF Cliente')
        self.tree.heading('Data', text='Data')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Preço', text='Preço')

        # Ajustar o tamanho das colunas
        self.tree.column('ID', width=150)
        self.tree.column('Chassi', width=100)
        self.tree.column('CPF', width=100)
        self.tree.column('Data', width=100)
        self.tree.column('Status', width=100)
        self.tree.column('Preço', width=100)

        # Posicionar o Treeview
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        
        self.listar_vendas()

        # ////////////////////////////////////////////////////////////////////////////

        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

                # Configurando pesos das colunas e linhas para centralização
        self.tab_agenda.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_agenda.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_agenda.rowconfigure(row, weight=1) 

        # Seção para agendar revisão
        label_agendar_revisao = ttk.Label(self.tab_agenda, text="Agendar Revisão", **self.estilo_label)
        label_agendar_revisao.grid(row=0, column=0, columnspan=2, pady=(5,10))

        label_chassi_moto_revisao = ttk.Label(self.tab_agenda, text="Chassi:", **self.estilo_label)
        label_chassi_moto_revisao.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_chassi_moto_revisao = ttk.Entry(self.tab_agenda, **self.estilo_entrada)
        self.entry_chassi_moto_revisao.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_cpf_cliente_revisao = ttk.Label(self.tab_agenda, text="CPF do Cliente:", **self.estilo_label)
        label_cpf_cliente_revisao.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf_cliente_revisao = ttk.Entry(self.tab_agenda, **self.estilo_entrada)
        self.entry_cpf_cliente_revisao.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        btn_agendar_revisao = ttk.Button(self.tab_agenda, text="Agendar Revisão", style="Custom.TButton", command=self.agendar_revisao)
        btn_agendar_revisao.grid(row=3, column=1, pady=10, sticky="w")

        # Seção para listar
        label_listar_funcionarios = ttk.Label(self.tab_agenda, text="Revisões Agendadas", **self.estilo_label)
        label_listar_funcionarios.grid(row=4, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar 
        colunas = ('ID','Chassi', 'Data', 'CPF', 'Status', 'Custo')
        self.tree = ttk.Treeview(self.tab_agenda, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree.heading('ID', text='ID Revisão')
        self.tree.heading('Chassi', text='Chassi')
        self.tree.heading('Data', text='Data')
        self.tree.heading('CPF', text='Cpf')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Custo', text='Custo')

        # Ajustar o tamanho das colunas
        self.tree.column('ID', width=150)
        self.tree.column('Chassi', width=100)
        self.tree.column('Data', width=100)
        self.tree.column('CPF', width=100)
        self.tree.column('Status', width=100)
        self.tree.column('Custo', width=100)

        # Posicionar o Treeview
        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
     
        self.listar_revisoes()

