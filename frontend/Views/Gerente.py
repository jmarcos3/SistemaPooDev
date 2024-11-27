from tkinter import ttk
from .telas import telas

class GerenteApp(telas):
    def __init__(self, root):
        super().__init__(root, "gerente")

        # Personalizando abas
        style = ttk.Style()

        style.theme_use("default")
        style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Motos", "Clientes", "Vendas", "Agenda de Revisões", "Funcionários"])
        )
       # Aba de Motos
        self.tab_motos = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_motos, text="Motos")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_motos.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_motos.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_motos.rowconfigure(row, weight=1)   

        # Seção para adicionar moto
        label_adicionar_moto = ttk.Label(self.tab_motos, text="Adicionar Moto", **self.estilo_label)
        label_adicionar_moto.grid(row=0, column=0, columnspan=2, pady=(5, 15))

        label_modelo = ttk.Label(self.tab_motos, text="Modelo:", **self.estilo_label)
        label_modelo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_modelo = ttk.Entry(self.tab_motos, **self.estilo_entrada)
        self.entry_modelo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_ano = ttk.Label(self.tab_motos, text="Ano:", **self.estilo_label)
        label_ano.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_ano = ttk.Entry(self.tab_motos, **self.estilo_entrada)
        self.entry_ano.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        label_preco = ttk.Label(self.tab_motos, text="Preço:", **self.estilo_label)
        label_preco.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_preco = ttk.Entry(self.tab_motos, **self.estilo_entrada)
        self.entry_preco.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        label_cor = ttk.Label(self.tab_motos, text="Cor:", **self.estilo_label)
        label_cor.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_cor = ttk.Entry(self.tab_motos, **self.estilo_entrada)
        self.entry_cor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        label_chassi = ttk.Label(self.tab_motos, text="Chassi:", **self.estilo_label)
        label_chassi.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_chassi = ttk.Entry(self.tab_motos, **self.estilo_entrada)
        self.entry_chassi.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        btn_adicionar_moto = ttk.Button(self.tab_motos, text="Adicionar moto", style="Custom.TButton", command=self.adicionar_moto)
        btn_adicionar_moto.grid(row=6, column=1, pady=10, sticky="w")

        # Seção para listar 
        label_listar_funcionarios = ttk.Label(self.tab_motos, text="Motos Cadastradas", **self.estilo_label)
        label_listar_funcionarios.grid(row=7, column=0, pady=(5), columnspan=2)

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
        self.tree_moto.grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        
        # Botões para editar e deletar motos
        btn_editar_moto = ttk.Button(self.tab_motos, text="Editar Moto", style="Custom.TButton", command=self.editar_moto)
        btn_editar_moto.grid(row=11, column=0, pady=10, sticky="n")

        btn_deletar_moto = ttk.Button(self.tab_motos, text="Deletar Moto", style="Custom.TButton", command=self.deletar_moto)
        btn_deletar_moto.grid(row=11, column=1, pady=10, sticky="n")
        
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

        btn_editar_venda = ttk.Button(self.tab_venda, text="Editar Venda", style="Custom.TButton", command=self.editar_venda)
        btn_editar_venda.grid(row=8, column=0, pady=10, sticky="n")

        btn_deletar_venda = ttk.Button(self.tab_venda, text="Deletar Venda", style="Custom.TButton", command=self.deletar_venda)
        btn_deletar_venda.grid(row=8, column=1, pady=10, sticky="n")

        
        self.listar_vendas()

#################################################################

        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook, padding=10)  # Reduzindo o padding
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_agenda.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_agenda.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_agenda.rowconfigure(row, weight=1)

        # Seção para agendar revisão
        label_agendar_revisao = ttk.Label(self.tab_agenda, text="Agendar Revisão", **self.estilo_label)
        label_agendar_revisao.grid(row=0, column=0, columnspan=2, pady=(5, 10))  # Ajustando o padding

        label_chassi_moto_revisao = ttk.Label(self.tab_agenda, text="Chassi:", **self.estilo_label)
        label_chassi_moto_revisao.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_chassi_moto_revisao = ttk.Entry(self.tab_agenda, **self.estilo_entrada)
        self.entry_chassi_moto_revisao.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_cpf_cliente_revisao = ttk.Label(self.tab_agenda, text="CPF do Cliente:", **self.estilo_label)
        label_cpf_cliente_revisao.grid(row=2, column=0, padx=5, pady=5, sticky="e")  # Corrigido o row
        self.entry_cpf_cliente_revisao = ttk.Entry(self.tab_agenda, **self.estilo_entrada)
        self.entry_cpf_cliente_revisao.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        btn_agendar_revisao = ttk.Button(self.tab_agenda, text="Agendar Revisão", style="Custom.TButton", command=self.agendar_revisao)
        btn_agendar_revisao.grid(row=3, column=1, pady=5, sticky="w")  # Ajustando o padding

        # Seção para listar
        label_listar_revisoes = ttk.Label(self.tab_agenda, text="Revisões Agendadas", **self.estilo_label)
        label_listar_revisoes.grid(row=4, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar
        colunas = ('ID', 'Chassi', 'Data', 'CPF', 'Status', 'Custo')
        self.tree_revisao = ttk.Treeview(self.tab_agenda, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_revisao.heading('ID', text='ID Manutenção')
        self.tree_revisao.heading('Chassi', text='Chassi')
        self.tree_revisao.heading('Data', text='Data')
        self.tree_revisao.heading('CPF', text='CPF Cliente')
        self.tree_revisao.heading('Status', text='Status')
        self.tree_revisao.heading('Custo', text='Custo')

        # Ajustar o tamanho das colunas
        self.tree_revisao.column('ID', width=150)
        self.tree_revisao.column('Chassi', width=100)
        self.tree_revisao.column('Data', width=100)
        self.tree_revisao.column('CPF', width=100)
        self.tree_revisao.column('Status', width=100)
        self.tree_revisao.column('Custo', width=100)

        # Posicionar o Treeview
        self.tree_revisao.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')  # Ajustando o padding

        # Botões para editar e deletar revisão
        btn_editar_revisao = ttk.Button(self.tab_agenda, text="Editar Revisão", style="Custom.TButton", command=self.editar_revisao)
        btn_editar_revisao.grid(row=6, column=0, pady=5, sticky="n")

        btn_deletar_revisao = ttk.Button(self.tab_agenda, text="Deletar Revisão", style="Custom.TButton", command=self.deletar_revisao)
        btn_deletar_revisao.grid(row=6, column=1, pady=5, sticky="n")  # Ajustando o padding

        self.listar_revisoes()


##########################################################################################
#      
        # Adicionando a aba de Funcionários
        self.tab_funcionarios = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_funcionarios, text="Funcionários")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_funcionarios.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_funcionarios.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_funcionarios.rowconfigure(row, weight=1)

        # Seção para adicionar funcionário
        label_add_funcionario = ttk.Label(self.tab_funcionarios, text="Adicionar Funcionário", **self.estilo_label)
        label_add_funcionario.grid(row=0, column=0, columnspan=2, pady=(5, 10))  # Ajustando o padding

        label_nome_funcionario = ttk.Label(self.tab_funcionarios, text="Nome:", **self.estilo_label)
        label_nome_funcionario.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome_funcionario = ttk.Entry(self.tab_funcionarios, **self.estilo_entrada)
        self.entry_nome_funcionario.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_cpf_funcionario = ttk.Label(self.tab_funcionarios, text="CPF:", **self.estilo_label)
        label_cpf_funcionario.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf_funcionario = ttk.Entry(self.tab_funcionarios, **self.estilo_entrada)
        self.entry_cpf_funcionario.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        label_cargo_funcionario = ttk.Label(self.tab_funcionarios, text="Cargo:", **self.estilo_label)
        label_cargo_funcionario.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_cargo_funcionario = ttk.Entry(self.tab_funcionarios, **self.estilo_entrada)
        self.entry_cargo_funcionario.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Botão para adicionar funcionário
        btn_add_funcionario = ttk.Button(self.tab_funcionarios, text="Adicionar funcionário", style="Custom.TButton", command=self.adicionar_funcionario)
        btn_add_funcionario.grid(row=4, column=1, pady=5, sticky="w")  # Ajustando o padding

        # Seção para listar
        label_listar_funcionarios = ttk.Label(self.tab_funcionarios, text="Funcionários Cadastrados", **self.estilo_label)
        label_listar_funcionarios.grid(row=5, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar
        colunas = ('Nome', 'CPF', 'Cargo')
        self.tree = ttk.Treeview(self.tab_funcionarios, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('CPF', text='CPF')
        self.tree.heading('Cargo', text='Cargo')

        # Ajustar o tamanho das colunas
        self.tree.column('Nome', width=150)
        self.tree.column('CPF', width=120)
        self.tree.column('Cargo', width=100)

        # Posicionar o Treeview
        self.tree.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        # Botões para editar e deletar funcionários
        btn_editar_funcionario = ttk.Button(self.tab_funcionarios, text="Editar Funcionário", style="Custom.TButton", command=self.editar_funcionario)
        btn_editar_funcionario.grid(row=7, column=0, pady=5, sticky="n")

        btn_deletar_funcionario = ttk.Button(self.tab_funcionarios, text="Deletar Funcionário", style="Custom.TButton", command=self.deletar_funcionario)
        btn_deletar_funcionario.grid(row=7, column=1, pady=5, sticky="n")  # Ajustando o padding

        self.listar_funcionarios()
