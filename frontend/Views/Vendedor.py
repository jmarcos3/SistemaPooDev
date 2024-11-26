import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,Revisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

class VendedorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        # Inicializando DAOs
        self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
        self.cliente_dao = ClienteDAO('db.db')
        self.venda_dao = VendaDAO('db.db')

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
        estilo_label = {"font": ("Arial", 16, "bold"), "foreground": "#333"}
        estilo_entrada = {"width": 25, "font": ("Arial", 14)}

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
        label_adicionar_cliente = ttk.Label(self.tab_cliente, text="Adicionar Cliente", **estilo_label)
        label_adicionar_cliente.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        label_nome = ttk.Label(self.tab_cliente, text="Nome:", **estilo_label)
        label_nome.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        label_cpf = ttk.Label(self.tab_cliente, text="CPF:", **estilo_label)
        label_cpf.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        label_email = ttk.Label(self.tab_cliente, text="Email:", **estilo_label)
        label_email.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_email.grid(row=3, column=1, padx=3, pady=3, sticky="w")

        btn_adicionar_cliente = ttk.Button(self.tab_cliente, text="Adicionar Cliente", style="Custom.TButton", command=self.adicionar_cliente)
        btn_adicionar_cliente.grid(row=4, column=1, pady=3, sticky="w")

        # Seção para listar clientes
        label_listar_clientes = ttk.Label(self.tab_cliente, text="Clientes Cadastrados", **estilo_label)
        label_listar_clientes.grid(row=5, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar 
        colunas = ('CPF', 'Nome', 'Email')
        self.tree = ttk.Treeview(self.tab_cliente, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree.heading('CPF', text='CPF')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Email', text='Email')

        # Ajustar o tamanho das colunas
        self.tree.column('CPF', width=150)
        self.tree.column('Nome', width=120)
        self.tree.column('Email', width=200)

        # Posicionar o Treeview
        self.tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Botões para editar e deletar 
        btn_editar_cliente = ttk.Button(self.tab_cliente, text="Editar Cliente", style="Custom.TButton", command=self.atualizar_cliente)
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
        label_gerar_venda = ttk.Label(self.tab_venda, text="Gerar Venda", **estilo_label)
        label_gerar_venda.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        label_cpf_cliente = ttk.Label(self.tab_venda, text="Cliente:", **estilo_label)
        label_cpf_cliente.grid(row=1, column=0, padx=5, pady=3, sticky="e")
        self.entry_cpf_cliente = ttk.Entry(self.tab_venda, **estilo_entrada)
        self.entry_cpf_cliente.grid(row=1, column=1, padx=5, pady=3, sticky="w")

        label_chassi_moto = ttk.Label(self.tab_venda, text="Chassi:", **estilo_label)
        label_chassi_moto.grid(row=2, column=0, padx=5, pady=3, sticky="e")
        self.entry_chassi_moto = ttk.Entry(self.tab_venda, **estilo_entrada)
        self.entry_chassi_moto.grid(row=2, column=1, padx=5, pady=3, sticky="w")

        btn_gerar_venda = ttk.Button(self.tab_venda, text="Gerar Venda", style="Custom.TButton", command=self.adicionar_venda)
        btn_gerar_venda.grid(row=3, column=1, pady=5, sticky="w")
##########################################
        # Seção para listar 
        label_listar_funcionarios = ttk.Label(self.tab_venda, text="Lista de Vendas", **estilo_label)
        label_listar_funcionarios.grid(row=4, column=0, pady=(3), columnspan=2)

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
        self.tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        
        self.listar_vendas()

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


####################################################################################
    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()

        cliente = Cliente(nome=nome, cpf=cpf, email=email)
        self.cliente_dao.adicionar_cliente(cliente)

        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

        print("Cliente adicionado com sucesso!")
        self.listar_clientes(self)

    def atualizar_cliente(self):
        cpf = self.entry_atualizar_cpf.get()  # CPF do cliente a ser atualizado
        campo = self.entry_campo_atualizar.get().lower()  # Campo a ser atualizado (nome ou email)
        novo_valor = self.entry_novo_valor.get()  # Novo valor para o campo

        if campo == "nome":  # Verifica qual campo será atualizado
            cliente = Cliente(cpf=cpf, nome=novo_valor, email=None)  # Cria cliente com o novo nome
            self.cliente_dao.atualizar_cliente(cliente)
        elif campo == "email":
            cliente = Cliente(cpf=cpf, nome=None, email=novo_valor)  # Cria cliente com o novo email
            self.cliente_dao.atualizar_cliente(cliente)
        else:
            print("Campo inválido. Só é possível atualizar 'nome' ou 'email'.")
            return
        
        print("Cliente atualizado com sucesso!")
    
    def listar_clientes(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Buscar os funcionários no banco de dados
        clientes = self.cliente_dao.listar_clientes()

        if clientes:
            for cliente in clientes:
                cpf = cliente[0]  # Primeiro campo (CPF)
                nome = cliente[1]  # Segundo campo (Nome)
                email = cliente[2]  # Terceiro campo (Email)
                self.tree.insert('', tk.END, values=(cpf, nome, email))  # Inserir na tabela
        else:
            messagebox.showinfo("Informação", "Nenhum item encontrado.")

######################################################################################
    def remover_moto_posvenda(self,chassi):
        self.moto_dao.deletar_moto(chassi)  # Verifique se o método de remoção se chama deletar_moto
        print("Moto removida com sucesso!")

    def adicionar_venda(self):
        cpf_cliente = self.entry_cpf_cliente.get()
        chassi_moto = self.entry_chassi_moto.get()
       
        try:
            item = self.cliente_dao.buscar_cliente(cpf_cliente)
            if item != None: 
                print('pass')
            else:
                if cpf_cliente == "":
                    raise ValueError
                else:
                    raise TypeError
        except TypeError:
            messagebox.showerror("Erro", "Digite um cliente cadastrado")
        except ValueError:
            messagebox.showerror("Erro", "Todos os campos precisam ser preenchidos")

        try:
            item = self.moto_dao.buscar_moto(chassi_moto)
            if item != None: 
                data_venda = datetime.datetime.now().strftime("%Y-%m-%d")
                status = "Preparando"
                preco = self.moto_dao.buscar_preco(chassi_moto)
                self.remover_moto_posvenda(chassi_moto)
                venda = Venda(data=data_venda, status=status, chassi_moto=chassi_moto, cpf_cliente=cpf_cliente, preco=preco[0])
                self.venda_dao.adicionar_venda(venda)
            else:
                if chassi_moto == "":
                    raise ValueError
                else:
                    raise TypeError
        except TypeError:
            messagebox.showerror("Erro", "Digite uma moto cadastrada")  
        except ValueError:
            messagebox.showerror("Erro", "Todos os campos precisam ser preenchidos")



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