import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,Revisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

class GerenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        #self.root.geometry("600x800")  # Ajuste o tamanho da janela conforme necessário

        # Inicializando DAOs
        self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
        self.cliente_dao = ClienteDAO('db.db')
        self.venda_dao = VendaDAO('db.db')
        self.agenda_revisao_dao = AgendaRevisaoDAO('db.db')
        self.funcionario_dao = FuncionarioDAO('db.db')

        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Estilos personalizados
        estilo_label = {"font": ("Arial", 14, "bold"), "foreground": "#333"}
        estilo_entrada = {"width": 25, "font": ("Arial", 12)}

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14))

        # Aba de Motos
        self.tab_motos = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_motos, text="Motos")

        # Seção para adicionar moto
        label_adicionar_moto = ttk.Label(self.tab_motos, text="Adicionar Moto", **estilo_label)
        label_adicionar_moto.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        label_modelo = ttk.Label(self.tab_motos, text="Modelo:", **estilo_label)
        label_modelo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_modelo = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_modelo.grid(row=1, column=1, padx=5, pady=5)

        label_ano = ttk.Label(self.tab_motos, text="Ano:", **estilo_label)
        label_ano.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_ano = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_ano.grid(row=2, column=1, padx=5, pady=5)

        label_preco = ttk.Label(self.tab_motos, text="Preço:", **estilo_label)
        label_preco.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_preco = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_preco.grid(row=3, column=1, padx=5, pady=5)

        label_cor = ttk.Label(self.tab_motos, text="Cor:", **estilo_label)
        label_cor.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_cor = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_cor.grid(row=4, column=1, padx=5, pady=5)

        label_chassi = ttk.Label(self.tab_motos, text="Chassi:", **estilo_label)
        label_chassi.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_chassi = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_chassi.grid(row=5, column=1, padx=5, pady=5)

        btn_adicionar_moto = ttk.Button(self.tab_motos, text="Adicionar", style="Custom.TButton", command=self.adicionar_moto)
        btn_adicionar_moto.grid(row=6, column=1, pady=10, sticky="n")

        # Seção para remover moto
        label_remover_moto = ttk.Label(self.tab_motos, text="Remover Moto", **estilo_label)
        label_remover_moto.grid(row=7, column=0, columnspan=2, pady=(15, 5))

        label_id_moto_remover = ttk.Label(self.tab_motos, text="Chassi:", **estilo_label)
        label_id_moto_remover.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_moto_remover = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_id_moto_remover.grid(row=8, column=1, padx=5, pady=5)

        btn_remover_moto = ttk.Button(self.tab_motos, text="Remover", style="Custom.TButton", command=self.remover_moto)
        btn_remover_moto.grid(row=9, column=1, pady=5, sticky="n")

        # Seção para atualizar moto
        label_atualizar_moto = ttk.Label(self.tab_motos, text="Atualizar Moto", **estilo_label)
        label_atualizar_moto.grid(row=10, column=0, columnspan=2, pady=(15, 5))

        label_id_moto_atualizar = ttk.Label(self.tab_motos, text="Chassi:", **estilo_label)
        label_id_moto_atualizar.grid(row=11, column=0, padx=5, pady=5, sticky="e")
        self.entry_id_moto_atualizar = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_id_moto_atualizar.grid(row=11, column=1, padx=5, pady=5)

        label_campo_atualizar_moto = ttk.Label(self.tab_motos, text="Campo a Atualizar:", **estilo_label)
        label_campo_atualizar_moto.grid(row=12, column=0, padx=5, pady=5, sticky="e")
        self.entry_campo_atualizar_moto = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_campo_atualizar_moto.grid(row=12, column=1, padx=5, pady=5)

        label_novo_valor = ttk.Label(self.tab_motos, text="Novo Valor:", **estilo_label)
        label_novo_valor.grid(row=13, column=0, padx=5, pady=5, sticky="e")
        self.entry_valor_atualizar = ttk.Entry(self.tab_motos, **estilo_entrada)
        self.entry_valor_atualizar.grid(row=13, column=1, padx=5, pady=5)

        btn_atualizar_moto = ttk.Button(self.tab_motos, text="Atualizar", style="Custom.TButton", command=self.atualizar_moto)
        btn_atualizar_moto.grid(row=14, column=1, pady=10, sticky="n")

        # Seção para listar motos
        label_listar_motos = ttk.Label(self.tab_motos, text="Listar Motos:", **estilo_label)
        label_listar_motos.grid(row=15, column=0, pady=5)

        btn_listar_motos = ttk.Button(self.tab_motos, text="Listar Motos", style="Custom.TButton", command=self.listar_motos_popup)
        btn_listar_motos.grid(row=15, column=1, pady=10, sticky="s")


        # Aba de Clientes
        self.tab_cliente = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_cliente, text="Clientes")

        # Seção para adicionar cliente
        label_adicionar_cliente = ttk.Label(self.tab_cliente, text="Adicionar Cliente", **estilo_label)
        label_adicionar_cliente.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        label_nome = ttk.Label(self.tab_cliente, text="Nome:", **estilo_label)
        label_nome.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

        label_cpf = ttk.Label(self.tab_cliente, text="CPF:", **estilo_label)
        label_cpf.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5)

        label_email = ttk.Label(self.tab_cliente, text="Email:", **estilo_label)
        label_email.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_email.grid(row=3, column=1, padx=5, pady=5)

        btn_adicionar_cliente = ttk.Button(self.tab_cliente, text="Adicionar", style="Custom.TButton", command=self.adicionar_cliente)
        btn_adicionar_cliente.grid(row=4, column=1, pady=10, sticky="n")

        # Seção para atualizar cliente
        label_atualizar_cliente = ttk.Label(self.tab_cliente, text="Atualizar Cliente", **estilo_label)
        label_atualizar_cliente.grid(row=8, column=0, columnspan=2, pady=(15, 5))

        label_atualizar_cpf = ttk.Label(self.tab_cliente, text="CPF do Cliente:", **estilo_label)
        label_atualizar_cpf.grid(row=9, column=0, padx=5, pady=5, sticky="e")
        self.entry_atualizar_cpf = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_atualizar_cpf.grid(row=9, column=1, padx=5, pady=5)

        label_campo_atualizar = ttk.Label(self.tab_cliente, text="Campo a Atualizar:", **estilo_label)
        label_campo_atualizar.grid(row=10, column=0, padx=5, pady=5, sticky="e")
        self.entry_campo_atualizar = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_campo_atualizar.grid(row=10, column=1, padx=5, pady=5)

        label_novo_valor = ttk.Label(self.tab_cliente, text="Novo Valor:", **estilo_label)
        label_novo_valor.grid(row=11, column=0, padx=5, pady=5, sticky="e")
        self.entry_novo_valor = ttk.Entry(self.tab_cliente, **estilo_entrada)
        self.entry_novo_valor.grid(row=11, column=1, padx=5, pady=5)

        btn_atualizar_cliente = ttk.Button(self.tab_cliente, text="Atualizar", style="Custom.TButton", command=self.atualizar_cliente)
        btn_atualizar_cliente.grid(row=12, column=1, pady=10, sticky="n")

        # Seção para listar clientes
        label_listar_clientes = ttk.Label(self.tab_cliente, text="Listar Clientes:", **estilo_label)
        label_listar_clientes.grid(row=14, column=0, pady=5)

        btn_listar_clientes = ttk.Button(self.tab_cliente, text="Listar Clientes", style="Custom.TButton", command=self.listar_clientes_popup)
        btn_listar_clientes.grid(row=14, column=1, pady=5, sticky="n")


        # Aba de Vendas
        self.tab_venda = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_venda, text="Vendas")

        # Seção para gerar venda
        label_gerar_venda = ttk.Label(self.tab_venda, text="Gerar Venda", **estilo_label)
        label_gerar_venda.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        label_cpf_cliente = ttk.Label(self.tab_venda, text="Cliente:", **estilo_label)
        label_cpf_cliente.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf_cliente = ttk.Entry(self.tab_venda, **estilo_entrada)
        self.entry_cpf_cliente.grid(row=1, column=1, padx=5, pady=5)

        label_chassi_moto = ttk.Label(self.tab_venda, text="Chassi:", **estilo_label)
        label_chassi_moto.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_chassi_moto = ttk.Entry(self.tab_venda, **estilo_entrada)
        self.entry_chassi_moto.grid(row=2, column=1, padx=5, pady=5)

        btn_gerar_venda = ttk.Button(self.tab_venda, text="Gerar Venda", style="Custom.TButton", command=self.adicionar_venda)
        btn_gerar_venda.grid(row=3, column=1, pady=10, sticky="n")

        # Label para a seção de listar vendas
        label_listar_vendas = ttk.Label(self.tab_venda, text="Listar Vendas: ", **estilo_label)
        label_listar_vendas.grid(row=14, column=0, pady=(5))

        # Botão para listar vendas e abrir um pop-up
        btn_listar_vendas = ttk.Button(self.tab_venda, text="Listar Vendas", style="Custom.TButton", command=self.listar_vendas_popup)
        btn_listar_vendas.grid(row=14, column=1, pady=10, sticky="n")


        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Seção para agendar revisão
        label_agendar_revisao = ttk.Label(self.tab_agenda, text="Agendar Revisão", **estilo_label)
        label_agendar_revisao.grid(row=0, column=0, columnspan=2, pady=(0,15))

        label_chassi_moto_revisao = ttk.Label(self.tab_agenda, text="Chassi:", **estilo_label)
        label_chassi_moto_revisao.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_chassi_moto_revisao = ttk.Entry(self.tab_agenda, **estilo_entrada)
        self.entry_chassi_moto_revisao.grid(row=1, column=1, padx=5, pady=5)

        label_cpf_cliente_revisao = ttk.Label(self.tab_agenda, text="CPF do Cliente:", **estilo_label)
        label_cpf_cliente_revisao.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf_cliente_revisao = ttk.Entry(self.tab_agenda, **estilo_entrada)
        self.entry_cpf_cliente_revisao.grid(row=3, column=1, padx=5, pady=5)

        btn_agendar_revisao = ttk.Button(self.tab_agenda, text="Agendar Revisão", style="Custom.TButton", command=self.agendar_revisao)
        btn_agendar_revisao.grid(row=4, column=1, pady=10, sticky="n")

        # Seção para listar revisões agendadas
        label_listar_revisoes = ttk.Label(self.tab_agenda, text="Mostrar Agenda:", **estilo_label)
        label_listar_revisoes.grid(row=5, column=0, pady=(5))

        # Botão para listar revisões e abrir um pop-up
        btn_listar_revisoes = ttk.Button(self.tab_agenda, text="Listar Revisões", style="Custom.TButton", command=self.listar_revisoes_popup)
        btn_listar_revisoes.grid(row=5, column=1, pady=5, sticky="n")


        # Adicionando a aba de Funcionários
        self.tab_funcionarios = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_funcionarios, text="Funcionários")

        # Seção para adicionar funcionário
        label_add_funcionario = ttk.Label(self.tab_funcionarios, text="Adicionar Funcionário", **estilo_label)
        label_add_funcionario.grid(row=0, column=0, columnspan=2, pady=(0,15))

        label_nome_funcionario = ttk.Label(self.tab_funcionarios, text="Nome:", **estilo_label)
        label_nome_funcionario.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome_funcionario = ttk.Entry(self.tab_funcionarios, **estilo_entrada)
        self.entry_nome_funcionario.grid(row=1, column=1, padx=5, pady=5)

        label_cpf_funcionario = ttk.Label(self.tab_funcionarios, text="CPF:", **estilo_label)
        label_cpf_funcionario.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_cpf_funcionario = ttk.Entry(self.tab_funcionarios, **estilo_entrada)
        self.entry_cpf_funcionario.grid(row=2, column=1, padx=5, pady=5)

        label_cargo_funcionario = ttk.Label(self.tab_funcionarios, text="Cargo:", **estilo_label)
        label_cargo_funcionario.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_cargo_funcionario = ttk.Entry(self.tab_funcionarios, **estilo_entrada)
        self.entry_cargo_funcionario.grid(row=3, column=1, padx=5, pady=5)

        # Botão para adicionar funcionário
        btn_add_funcionario = ttk.Button(self.tab_funcionarios, text="Adicionar", style="Custom.TButton", command=self.adicionar_funcionario)
        btn_add_funcionario.grid(row=4, column=1, pady=10, sticky="n")

        # Seção para listar funcionários
        label_listar_funcionarios = ttk.Label(self.tab_funcionarios, text="Funcionários Cadastrados", **estilo_label)
        label_listar_funcionarios.grid(row=5, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar funcionários
        colunas = ('Nome', 'CPF', 'Cargo')
        self.tree_funcionarios = ttk.Treeview(self.tab_funcionarios, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_funcionarios.heading('Nome', text='Nome')
        self.tree_funcionarios.heading('CPF', text='CPF')
        self.tree_funcionarios.heading('Cargo', text='Cargo')

        # Ajustar o tamanho das colunas
        self.tree_funcionarios.column('Nome', width=150)
        self.tree_funcionarios.column('CPF', width=120)
        self.tree_funcionarios.column('Cargo', width=100)

        # Posicionar o Treeview
        self.tree_funcionarios.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Botões para editar e deletar funcionários
        btn_editar_funcionario = ttk.Button(self.tab_funcionarios, text="Editar Funcionário", style="Custom.TButton", command=self.editar_funcionario)
        btn_editar_funcionario.grid(row=7, column=0, pady=10, sticky="n")

        btn_deletar_funcionario = ttk.Button(self.tab_funcionarios, text="Deletar Funcionário", style="Custom.TButton", command=self.deletar_funcionario)
        btn_deletar_funcionario.grid(row=7, column=1, pady=10, sticky="n")
        
        self.listar_funcionarios()
        




    # Métodos CRUD para motos
    def adicionar_moto(self):
        modelo = self.entry_modelo.get()
        ano = self.entry_ano.get()
        preco = float(self.entry_preco.get())  # Converter para float
        cor = self.entry_cor.get()
        chassi = self.entry_chassi.get()  # Chassi da moto

        # Aqui você poderia adicionar uma lógica para mudar o status se for necessário
        moto = Moto(modelo=modelo, ano=ano, preco=preco, cor=cor, chassi=chassi)
        self.moto_dao.adicionar_moto(moto)
        print("Moto adicionada com sucesso!")


    def atualizar_moto(self):
        chassi = self.entry_id_moto_atualizar.get()  # Chassi da moto
        campo = self.entry_campo_atualizar_moto.get().lower().strip()  # Campo a ser atualizado
        novo_valor = self.entry_valor_atualizar.get().strip()  # Novo valor a ser atualizado

        print(f"Campo a ser atualizado: {campo}")
        print(f"Novo valor: {novo_valor}")

        if campo == "preco":
            try:
                novo_valor = float(novo_valor)  # Converte para float
                self.moto_dao.atualizar_moto(chassi=chassi, preco=novo_valor)
            except ValueError:
                print("Erro: O valor fornecido para 'preco' deve ser numérico.")
                return
        elif campo == "ano":
            try:
                novo_valor = int(novo_valor)  # Converte para int
                self.moto_dao.atualizar_moto(chassi=chassi, ano=novo_valor)
            except ValueError:
                print("Erro: O valor fornecido para 'ano' deve ser um número inteiro.")
                return
        elif campo == "cor":
            try:
                novo_valor = str(novo_valor)  # Converte para str
                self.moto_dao.atualizar_moto(chassi=chassi, cor=novo_valor)
            except ValueError:
                print("Erro: O valor fornecido para 'cor' deve ser uma string")
                return
        elif campo == "modelo":
            try:
                novo_valor = str(novo_valor)  # Converte para str
                self.moto_dao.atualizar_moto(chassi=chassi, modelo=novo_valor)
            except ValueError:
                print("Erro: O valor fornecido para 'modelo' deve ser uma string.")
                return
        else:
            print("Campo inválido. Só é possível atualizar 'preco','ano','cor' e 'modelo'.")
            return

        print("Moto atualizada com sucesso!")


    def remover_moto(self):
        id_moto = self.entry_id_moto_remover.get()
        self.moto_dao.deletar_moto(id_moto)  # Verifique se o método de remoção se chama deletar_moto
        print("Moto removida com sucesso!")

    def listar_motos_popup(self):
        # Criar uma nova janela (pop-up) referenciando a janela principal
        popup = tk.Toplevel(self.root)
        popup.title("Lista de Motos")

        # Definir o tamanho da nova janela
        popup.geometry("600x300")

        # Criar um Treeview para exibir as motos como uma tabela
        colunas = ('Chassi', 'Ano', 'Preço', 'Cor', 'Modelo')
        tree = ttk.Treeview(popup, columns=colunas, show='headings')

        tree.column('Chassi', width=100)
        tree.column('Ano', width=100)
        tree.column('Preço', width=100)
        tree.column('Cor', width=100)
        tree.column('Modelo', width=100)

        # Definir os títulos das colunas
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')

        # Inserir os dados das motos no Treeview
        motos = self.moto_dao.listar_motos()
        print("Motos encontradas:", motos)  # Verifique o que está sendo retornado

        if motos:
            for moto in motos:
                # Verifique se a tupla tem 5 elementos
                if len(moto) == 5:  # Certifique-se de que há 5 colunas
                    chassi = moto[0]  # ID
                    ano = moto[1]  # Ano
                    preco = moto[2]  # Preço
                    cor = moto[3]  # Cor
                    modelo = moto[4]  # Modelo
                    tree.insert('', tk.END, values=(chassi, ano, preco, cor, modelo))
                else:
                    print("Moto retornada com um número inesperado de campos:", moto)
        else:
            # Caso não haja motos, mostrar uma linha indicando isso
            tree.insert('', tk.END, values=('Nenhuma moto encontrada', '', '', '', ''))

        # Posicionar o Treeview na janela pop-up
        tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Adicionar um botão para fechar o pop-up
        btn_fechar = ttk.Button(popup, text="Fechar", style="Custom.TButton", command=popup.destroy)
        btn_fechar.pack(pady=10)




    # Métodos CRUD para clientes
    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()

        cliente = Cliente(nome=nome, cpf=cpf, email=email)
        self.cliente_dao.adicionar_cliente(cliente)
        print("Cliente adicionado com sucesso!")

    def remover_cliente(self):
        cpf = self.entry_remover_cpf.get()
        self.cliente_dao.remover_cliente(cpf)
        print("Cliente removido com sucesso!")

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

    def listar_clientes_popup(self):
        # Criar uma nova janela (pop-up) referenciando a janela principal
        popup = tk.Toplevel(self.root)  # Use self.root se o root for a janela principal (tk.Tk)
        popup.title("Lista de Clientes")

        # Definir o tamanho da nova janela
        popup.geometry("600x300")

        # Criar um Treeview para exibir os clientes como uma tabela
        colunas = ('CPF', 'Nome', 'Email')
        tree = ttk.Treeview(popup, columns=colunas, show='headings')
        
        # Definir os títulos das colunas
        tree.heading('CPF', text='CPF')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        # Ajustar o tamanho das colunas
        tree.column('CPF', width=150)
        tree.column('Nome', width=200)
        tree.column('Email', width=250)

        # Inserir os dados dos clientes no Treeview
        clientes = self.cliente_dao.listar_clientes()
        
        if clientes:
            for cliente in clientes:
                cpf = cliente[0]  # Primeiro campo (CPF)
                nome = cliente[1]  # Segundo campo (Nome)
                email = cliente[2]  # Terceiro campo (Email)
                tree.insert('', tk.END, values=(cpf, nome, email))  # Inserir na tabela
        else:
            # Caso não haja clientes, mostrar uma linha indicando isso
            tree.insert('', tk.END, values=('Nenhum cliente encontrado', '', ''))

        # Posicionar o Treeview na janela pop-up
        tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Adicionar um botão para fechar o pop-up
        btn_fechar = ttk.Button(popup, text="Fechar", style="Custom.TButton", command=popup.destroy)
        btn_fechar.pack(pady=10)

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




    def listar_vendas_popup(self):
        # Criar uma nova janela (pop-up) para listar as vendas
        popup = tk.Toplevel(self.root)
        popup.title("Vendas Realizadas")

        # Definir o tamanho da nova janela
        popup.geometry("700x300")  # Aumentei a largura para acomodar mais uma coluna

        # Criar um Treeview para exibir as vendas como uma tabela
        colunas = ('ID Venda', 'Chassi', 'CPF Cliente', 'Data', 'Status', 'Preço')  # Adicionando a coluna de Preço
        tree = ttk.Treeview(popup, columns=colunas, show='headings')

        # Definir os títulos das colunas
        tree.heading('ID Venda', text='ID Venda')
        tree.heading('Chassi', text='Chassi')
        tree.heading('CPF Cliente', text='CPF Cliente')
        tree.heading('Data', text='Data')
        tree.heading('Status', text='Status')
        tree.heading('Preço', text='Preço')  # Título da nova coluna

        # Ajustar o tamanho das colunas
        tree.column('ID Venda', width=100)
        tree.column('Chassi', width=100)
        tree.column('CPF Cliente', width=100)
        tree.column('Data', width=100)
        tree.column('Status', width=100)
        tree.column('Preço', width=100)  # Tamanho da nova coluna

        # Inserir os dados das vendas no Treeview
        vendas = self.venda_dao.listar_vendas()
        
        if vendas:
            for venda in vendas:
                id_venda = venda[0]  # Primeiro campo (ID da venda)
                chassi = venda[3]    # Chassi
                cpf_cliente = venda[4] # CPF do cliente
                data = venda[1]      # Data da venda
                status = venda[2]    # Status da venda
                preco = venda[5]     # Preço da venda (adicionando o preço)
                tree.insert('', tk.END, values=(id_venda, chassi, cpf_cliente, data, status, preco))  # Adicionando o preço às inserções
        else:
            # Caso não haja vendas, mostrar uma linha indicando isso
            tree.insert('', tk.END, values=('Nenhuma venda encontrada', '', '', '', '', ''))

        # Posicionar o Treeview na janela pop-up
        tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Adicionar um botão para fechar o pop-up
        btn_fechar = ttk.Button(popup, text="Fechar", style="Custom.TButton", command=popup.destroy)
        btn_fechar.pack(pady=10)






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

    def listar_revisoes_popup(self):
        # Criar uma nova janela (pop-up) para listar as revisões
        popup = tk.Toplevel(self.root)
        popup.title("Revisões Agendadas")

        # Definir o tamanho da nova janela
        popup.geometry("700x400")

        # Criar um Treeview para exibir as revisões como uma tabela
        colunas = ('ID Manutenção', 'Chassi Moto', 'Data', 'CPF', 'Status Revisão','Custo')
        tree = ttk.Treeview(popup, columns=colunas, show='headings')

        # Definir os títulos das colunas
        tree.heading('ID Manutenção', text='ID Manutenção')
        tree.heading('Chassi Moto', text='Chassi Moto')
        tree.heading('Data', text='Data')
        tree.heading('CPF', text='CPF')
        tree.heading('Status Revisão', text='Status Revisão')
        tree.heading('Custo', text='Custo')

        # Ajustar o tamanho das colunas
        tree.column('ID Manutenção', width=100)
        tree.column('Chassi Moto', width=100)
        tree.column('Data', width=100)
        tree.column('CPF', width=100)
        tree.column('Status Revisão', width=120)
        tree.column('Custo', width=100)

        # Inserir os dados das revisões no Treeview
        revisoes = self.agenda_revisao_dao.listar_revisoes()

        if revisoes:
            for revisao in revisoes:
                id_manutencao = revisao[0]  # ID da manutenção
                chassi_moto = revisao[4]    # Chassi da moto
                data = revisao[1]           # Data da revisão
                cpf = revisao[5]       # Nome do mecânico (ajustar conforme sua lógica)
                custo = revisao[3] # Status da revisão
                status_revisao = revisao[2] # Status da revisão
                tree.insert('', tk.END, values=(id_manutencao, chassi_moto, data, cpf, custo,status_revisao))
        else:
            # Caso não haja revisões, mostrar uma linha indicando isso
            tree.insert('', tk.END, values=('Nenhuma revisão encontrada', '', '', '', ''))

        # Posicionar o Treeview na janela pop-up
        tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Adicionar um botão para fechar o pop-up
        btn_fechar = ttk.Button(popup, text="Fechar", style="Custom.TButton", command=popup.destroy)
        btn_fechar.pack(pady=10)



    def adicionar_funcionario(self):
        nome = self.entry_nome_funcionario.get()
        cpf = self.entry_cpf_funcionario.get()
        cargo = self.entry_cargo_funcionario.get()

        # Validações básicas
        if not nome or not cpf or not cargo:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

       
        # Inserir o funcionário no banco de dados
        try:
            funcionario = Funcionario(cpf=cpf,nome=nome,usuario=cpf,senha=cpf,funcao=cargo)
            self.funcionario_dao.adicionar_funcionario(funcionario)
            messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
            self.listar_funcionarios()  # Atualizar a lista
            # Limpar os campos de entrada
            self.entry_nome_funcionario.delete(0, tk.END)
            self.entry_cpf_funcionario.delete(0, tk.END)
            self.entry_cargo_funcionario.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar funcionário: {e}")


    def listar_funcionarios(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree_funcionarios.get_children():
            self.tree_funcionarios.delete(i)

        # Buscar os funcionários no banco de dados
        funcionarios = self.funcionario_dao.listar_funcionarios()

        # Verifique se a lista de funcionários não está vazia
        if funcionarios:
            # Inserir cada funcionário na Treeview
            for funcionario in funcionarios:
                # Lembrando que funcionario é uma tupla, então acessar por índices
                
                nome_funcionario = funcionario[1]
                cpf_funcionario = funcionario[0]
                cargo_funcionario = funcionario[4]

                self.tree_funcionarios.insert('', 'end', values=(nome_funcionario, cpf_funcionario, cargo_funcionario))
        else:
            messagebox.showinfo("Informação", "Nenhum funcionário encontrado.")



    def editar_funcionario(self):
        # Obter o funcionário selecionado
        selected_item = self.tree_funcionarios.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione um funcionário para editar.")
            return

        item = self.tree_funcionarios.item(selected_item)
        funcionario_nome = item['values'][0]  # Nome
        funcionario_cpf = item['values'][1]    # CPF
        funcionario_cargo = item['values'][2]  # Cargo

        # Aqui você deve obter os dados de usuario e senha do banco de dados se necessário
        usuario_atual = "usuario_exemplo"  # Substitua isso pelo valor correto
        senha_atual = "senha_exemplo"      # Substitua isso pelo valor correto

        # Criar uma nova janela para editar o funcionário
        editar_popup = tk.Toplevel(self.root)
        editar_popup.title("Editar Funcionário")

        # Criar campos de entrada para editar os dados
        label_nome = ttk.Label(editar_popup, text="Nome:")
        label_nome.grid(row=0, column=0, padx=5, pady=5)
        entry_nome = ttk.Entry(editar_popup)
        entry_nome.insert(0, funcionario_nome)  # Preencher o nome atual
        entry_nome.grid(row=0, column=1, padx=5, pady=5)

        label_cpf = ttk.Label(editar_popup, text="CPF:")
        label_cpf.grid(row=1, column=0, padx=5, pady=5)
        entry_cpf = ttk.Entry(editar_popup)
        entry_cpf.insert(0, funcionario_cpf)  # Preencher o CPF atual
        entry_cpf.config(state='readonly')  # Não permitir editar o CPF
        entry_cpf.grid(row=1, column=1, padx=5, pady=5)

        label_cargo = ttk.Label(editar_popup, text="Cargo:")
        label_cargo.grid(row=2, column=0, padx=5, pady=5)
        entry_cargo = ttk.Entry(editar_popup)
        entry_cargo.insert(0, funcionario_cargo)  # Preencher o cargo atual
        entry_cargo.grid(row=2, column=1, padx=5, pady=5)

        # Botão para salvar as alterações
        def salvar_edicao():
            novo_nome = entry_nome.get()
            novo_cargo = entry_cargo.get()

            # Criar um objeto Funcionario com os dados atualizados
            funcionario_atualizado = Funcionario(nome=novo_nome,cpf=funcionario_cpf, usuario=usuario_atual, senha=senha_atual, funcao=novo_cargo)

            # Chamar o método para atualizar o funcionário no banco de dados
            self.funcionario_dao.atualizar_funcionario(funcionario_atualizado)

            # Fechar a janela popup
            editar_popup.destroy()

            # Atualizar a lista de funcionários no Treeview
            self.listar_funcionarios()

        btn_salvar = ttk.Button(editar_popup, text="Salvar", style="Custom.TButton", command=salvar_edicao)
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

        # Tornar a janela modal
        editar_popup.transient(self.root)
        editar_popup.grab_set()
        self.root.wait_window(editar_popup)




    def deletar_funcionario(self):
        selected_item = self.tree_funcionarios.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione um funcionário para deletar.")
            return

        item = self.tree_funcionarios.item(selected_item)
        funcionario_id = item['values'][1]


        try:
            self.funcionario_dao.deletar_funcionario(funcionario_id)
            messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
            self.listar_funcionarios()  # Atualizar a lista
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar funcionário: {e}")


    
 

# remover legenda do botão atualizar e aumentar o mesmo