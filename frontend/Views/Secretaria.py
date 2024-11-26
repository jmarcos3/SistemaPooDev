import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,Revisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

class SecretariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        # Inicializando DAOs
        self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
        self.venda_dao = VendaDAO('db.db')
        self.agenda_revisao_dao = AgendaRevisaoDAO('db.db')

        # Adicionando título
        self.title_label = tk.Label(
            root,
            text="Concessionária de motos",
            font=("Arial", 24, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=20
        )
        self.title_label.pack(fill="x")


        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Estilos personalizados
        estilo_label = {"font": ("Arial", 14, "bold"), "foreground": "#333"}
        estilo_entrada = {"width": 25, "font": ("Arial", 12)}

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 12))
        style.theme_use("default")
        style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Motos", "Vendas", "Agenda de Revisões"])
        )
        # ////////////////////////////////////////////////////////////////////////////

        # Aba de Motos
        self.tab_motos = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_motos, text="Motos")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_motos.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_motos.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_motos.rowconfigure(row, weight=1) 

        # Seção para listar 
        label_listar_funcionarios = ttk.Label(self.tab_motos, text="Motos Cadastradas", **estilo_label)
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
        label_listar_funcionarios = ttk.Label(self.tab_venda, text="Lista de Vendas", **estilo_label)
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
        label_agendar_revisao = ttk.Label(self.tab_agenda, text="Agendar Revisão", **estilo_label)
        label_agendar_revisao.grid(row=0, column=0, columnspan=2, pady=(5,10))

        label_chassi_moto_revisao = ttk.Label(self.tab_agenda, text="Chassi:", **estilo_label)
        label_chassi_moto_revisao.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_chassi_moto_revisao = ttk.Entry(self.tab_agenda, **estilo_entrada)
        self.entry_chassi_moto_revisao.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_cpf_cliente_revisao = ttk.Label(self.tab_agenda, text="CPF do Cliente:", **estilo_label)
        label_cpf_cliente_revisao.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf_cliente_revisao = ttk.Entry(self.tab_agenda, **estilo_entrada)
        self.entry_cpf_cliente_revisao.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        btn_agendar_revisao = ttk.Button(self.tab_agenda, text="Agendar Revisão", style="Custom.TButton", command=self.agendar_revisao)
        btn_agendar_revisao.grid(row=3, column=1, pady=10, sticky="w")

        # Seção para listar
        label_listar_funcionarios = ttk.Label(self.tab_agenda, text="Revisões Agendadas", **estilo_label)
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

        # ////////////////////////////////////////////////////////////////////////////

    def listar_motos(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree_moto.get_children():
            self.tree_moto.delete(i)

        # Buscar os funcionários no banco de dados
        motos = self.moto_dao.listar_motos()

        # Verifique se a lista de funcionários não está vazia
        if motos:
            # Inserir cada funcionário na Treeview
            for moto in motos:
                # Lembrando que funcionario é uma tupla, então acessar por índices
                chassi = moto[0]  # ID
                ano = moto[1]  # Ano
                preco = moto[2]  # Preço
                cor = moto[3]  # Cor
                modelo = moto[4]  # Modelo
                self.tree_moto.insert('', tk.END, values=(chassi, ano, preco, cor, modelo))
        else:
            messagebox.showinfo("Informação", "Nenhum  encontrado.")

        # ////////////////////////////////////////////////////////////////////////////

    def listar_vendas(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Buscar os funcionários no banco de dados
        vendas = self.venda_dao.listar_vendas()

        # Verifique se a lista de funcionários não está vazia
        if vendas:
            # Inserir cada funcionário na Treeview
            for venda in vendas:
                id_venda = venda[0]  # Primeiro campo (ID da venda)
                chassi = venda[3]    # Chassi
                cpf_cliente = venda[4] # CPF do cliente
                data = venda[1]      # Data da venda
                status = venda[2]    # Status da venda
                preco = venda[5]     # Preço da venda (adicionando o preço)

                self.tree.insert('', tk.END, values=(id_venda, chassi, cpf_cliente, data, status, preco))  # Adicionando o preço às inserções
        else:
            messagebox.showinfo("Informação", "Nenhum funcionário encontrado.") 


        # ////////////////////////////////////////////////////////////////////////////
        
    def agendar_revisao(self):
            # Obter dados da entrada
            chassi_moto = self.entry_chassi_moto_revisao.get()
            data_revisao = datetime.datetime.now().strftime("%Y-%m-%d")
            cpf = self.entry_cpf_cliente_revisao.get()

            # Validar entradas
            if not chassi_moto or not data_revisao or not cpf:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                return

            try:
                item = self.moto_dao.buscar_moto(chassi_moto)
                if item != None:
                    pass
                else:
                    raise Exception

            except Exception as e:
                messagebox.showerror("Erro", f"Digite um chassi válido")

            try:
                item = self.cliente_dao.buscar_cliente(cpf)
                if item != None:
                    revisao = Revisao(data=data_revisao, custo=250, status_revisao="Aguardando Moto", chassi_moto=chassi_moto, cpf_cliente=cpf)
                    self.agenda_revisao_dao.adicionar_revisao(revisao)
                    messagebox.showinfo("Sucesso", "Revisão agendada com sucesso!")
                    # Limpar campos após agendar
                    self.entry_chassi_moto_revisao.delete(0, tk.END)
                    self.entry_data_revisao.delete(0, tk.END)
                    self.entry_cpf_cliente_revisao.delete(0, tk.END)
                else: 
                    raise Exception      
            except Exception:
                messagebox.showerror("Erro", f"Digite um cpf válido")

    def listar_revisoes(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Buscar os funcionários no banco de dados
        revisoes = self.agenda_revisao_dao.listar_revisoes()

        # Verifique se a lista de funcionários não está vazia
        if revisoes:
            # Inserir cada funcionário na Treeview
            for revisao in revisoes:
                # Lembrando que funcionario é uma tupla, então acessar por índices
                id_manutencao = revisao[0]  # ID da manutenção
                chassi_moto = revisao[4]    # Chassi da moto
                data = revisao[1]           # Data da revisão
                cpf = revisao[5]       # Nome do mecânico (ajustar conforme sua lógica)
                custo = revisao[3] # Status da revisão
                status_revisao = revisao[2] # Status da revisão

                self.tree.insert('', tk.END, values=(id_manutencao, chassi_moto, data, cpf, custo,status_revisao))

        else:
            messagebox.showinfo("Informação", "Nenhum funcionário encontrado.")