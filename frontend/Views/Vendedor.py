from tkinter import ttk
from .telas import telas

class VendedorApp(telas):
    def __init__(self, root):
        super().__init__(root, "vendedor")

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14, "bold"))
        style.theme_use("default")
        style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Motos", "Clientes", "Vendas"])
        )

        # Aba de Motos
        self.tab_motos = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_motos, text="Motos")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_motos.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_motos.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_motos.rowconfigure(row, weight=1)   

#############################################################################################
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

##############################################################
        # Aba de Clientes
        self.tab_cliente = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_cliente, text="Clientes")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_cliente.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_cliente.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_cliente.rowconfigure(row, weight=1)   

        # Seção para adicionar cliente
        label_adicionar_cliente = ttk.Label(self.tab_cliente, text="Adicionar Cliente", **self.estilo_label)
        label_adicionar_cliente.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        label_nome = ttk.Label(self.tab_cliente, text="Nome:", **self.estilo_label)
        label_nome.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = ttk.Entry(self.tab_cliente, **self.estilo_entrada)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_cpf = ttk.Label(self.tab_cliente, text="CPF:", **self.estilo_label)
        label_cpf.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf = ttk.Entry(self.tab_cliente, **self.estilo_entrada)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        label_email = ttk.Label(self.tab_cliente, text="Email:", **self.estilo_label)
        label_email.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = ttk.Entry(self.tab_cliente, **self.estilo_entrada)
        self.entry_email.grid(row=3, column=1, padx=3, pady=3, sticky="w")

        btn_adicionar_cliente = ttk.Button(self.tab_cliente, text="Adicionar Cliente", style="Custom.TButton", command=self.adicionar_cliente)
        btn_adicionar_cliente.grid(row=4, column=1, pady=3, sticky="w")

        # Seção para listar clientes
        label_listar_clientes = ttk.Label(self.tab_cliente, text="Clientes Cadastrados", **self.estilo_label)
        label_listar_clientes.grid(row=5, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar 
        colunas = ('CPF', 'Nome', 'Email')
        self.tree_cliente = ttk.Treeview(self.tab_cliente, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_cliente.heading('CPF', text='CPF')
        self.tree_cliente.heading('Nome', text='Nome')
        self.tree_cliente.heading('Email', text='Email')

        # Ajustar o tamanho das colunas
        self.tree_cliente.column('CPF', width=150)
        self.tree_cliente.column('Nome', width=120)
        self.tree_cliente.column('Email', width=200)

        # Posicionar o Treeview
        self.tree_cliente.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Botões para editar e deletar 
        btn_editar_cliente = ttk.Button(self.tab_cliente, text="Editar Cliente", style="Custom.TButton", command=self.editar_cliente)
        btn_editar_cliente.grid(row=7, column=1, pady=10, sticky="n")

        # Listar clientes
        self.listar_clientes()


###################################################################################################
        # Aba de Vendas
        self.tab_venda = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_venda, text="Vendas")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_venda.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_venda.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_venda.rowconfigure(row, weight=1)

        # Seção para gerar venda
        label_gerar_venda = ttk.Label(self.tab_venda, text="Gerar Venda", **self.estilo_label)
        label_gerar_venda.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        label_cpf_cliente = ttk.Label(self.tab_venda, text="Cliente:", **self.estilo_label)
        label_cpf_cliente.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_cpf_cliente = ttk.Entry(self.tab_venda, **self.estilo_entrada)
        self.entry_cpf_cliente.grid(row=1, column=1, padx=5, pady=3, sticky="w")

        label_chassi_moto = ttk.Label(self.tab_venda, text="Chassi:", **self.estilo_label)
        label_chassi_moto.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_chassi_moto = ttk.Entry(self.tab_venda, **self.estilo_entrada)
        self.entry_chassi_moto.grid(row=2, column=1, padx=5, pady=3, sticky="w")

        btn_gerar_venda = ttk.Button(self.tab_venda, text="Gerar Venda", style="Custom.TButton", command=self.adicionar_venda)
        btn_gerar_venda.grid(row=3, column=1, pady=5, sticky="w")
##########################################
        # Seção para listar 
        label_listar_funcionarios = ttk.Label(self.tab_venda, text="Lista de Vendas", **self.estilo_label)
        label_listar_funcionarios.grid(row=4, column=0, pady=(3), columnspan=2)

        # Criando o Treeview para listar 
        colunas = ('ID','Chassi', 'CPF', 'Data', 'Status', 'Preço')
        self.tree_venda = ttk.Treeview(self.tab_venda, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_venda.heading('ID', text='ID Venda')
        self.tree_venda.heading('Chassi', text='Chassi')
        self.tree_venda.heading('CPF', text='CPF Cliente')
        self.tree_venda.heading('Data', text='Data')
        self.tree_venda.heading('Status', text='Status')
        self.tree_venda.heading('Preço', text='Preço')

        # Ajustar o tamanho das colunas
        self.tree_venda.column('ID', width=150)
        self.tree_venda.column('Chassi', width=100)
        self.tree_venda.column('CPF', width=100)
        self.tree_venda.column('Data', width=100)
        self.tree_venda.column('Status', width=100)
        self.tree_venda.column('Preço', width=100)

        # Posicionar o Treeview
        self.tree_venda.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        
        self.listar_vendas()
