import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,AgendaRevisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

class GerenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")

        # Inicializando DAOs
        self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
        self.cliente_dao = ClienteDAO('db.db')
        self.venda_dao = VendaDAO('db.db')
        self.agenda_revisao_dao = AgendaRevisaoDAO('db.db')

        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Aba de Motos
        self.tab_motos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_motos, text="Motos")

        # Seção para adicionar moto
        label_adicionar_moto = ttk.Label(self.tab_motos, text="Adicionar Moto")
        label_adicionar_moto.grid(row=0, column=0, columnspan=2, pady=5)

        label_modelo = ttk.Label(self.tab_motos, text="Modelo:")
        label_modelo.grid(row=1, column=0, padx=5, pady=5)
        self.entry_modelo = ttk.Entry(self.tab_motos)
        self.entry_modelo.grid(row=1, column=1, padx=5, pady=5)

        label_ano = ttk.Label(self.tab_motos, text="Ano:")
        label_ano.grid(row=2, column=0, padx=5, pady=5)
        self.entry_ano = ttk.Entry(self.tab_motos)
        self.entry_ano.grid(row=2, column=1, padx=5, pady=5)

        label_preco = ttk.Label(self.tab_motos, text="Preço:")
        label_preco.grid(row=3, column=0, padx=5, pady=5)
        self.entry_preco = ttk.Entry(self.tab_motos)
        self.entry_preco.grid(row=3, column=1, padx=5, pady=5)

        label_cor = ttk.Label(self.tab_motos, text="Cor:")
        label_cor.grid(row=4, column=0, padx=5, pady=5)
        self.entry_cor = ttk.Entry(self.tab_motos)
        self.entry_cor.grid(row=4, column=1, padx=5, pady=5)

        label_chassi = ttk.Label(self.tab_motos, text="Chassi:")
        label_chassi.grid(row=5, column=0, padx=5, pady=5)
        self.entry_chassi = ttk.Entry(self.tab_motos)
        self.entry_chassi.grid(row=5, column=1, padx=5, pady=5)

        btn_adicionar_moto = ttk.Button(self.tab_motos, text="Adicionar", command=self.adicionar_moto)
        btn_adicionar_moto.grid(row=6, column=1, pady=10)

        # Seção para remover moto
        label_remover_moto = ttk.Label(self.tab_motos, text="Remover Moto")
        label_remover_moto.grid(row=7, column=0, columnspan=2, pady=5)

        label_id_moto_remover = ttk.Label(self.tab_motos, text="ID da Moto:")
        label_id_moto_remover.grid(row=8, column=0, padx=5, pady=5)
        self.entry_id_moto_remover = ttk.Entry(self.tab_motos)
        self.entry_id_moto_remover.grid(row=8, column=1, padx=5, pady=5)

        btn_remover_moto = ttk.Button(self.tab_motos, text="Remover", command=self.remover_moto)
        btn_remover_moto.grid(row=9, column=1, pady=5)

        # Seção para atualizar moto
        label_atualizar_moto = ttk.Label(self.tab_motos, text="Atualizar Moto")
        label_atualizar_moto.grid(row=10, column=0, columnspan=2, pady=5)

        label_id_moto_atualizar = ttk.Label(self.tab_motos, text="ID da Moto:")
        label_id_moto_atualizar.grid(row=11, column=0, padx=5, pady=5)
        self.entry_id_moto_atualizar = ttk.Entry(self.tab_motos)
        self.entry_id_moto_atualizar.grid(row=11, column=1, padx=5, pady=5)

        label_campo_atualizar = ttk.Label(self.tab_motos, text="Campo a Atualizar:")
        label_campo_atualizar.grid(row=12, column=0, padx=5, pady=5)
        self.entry_campo_atualizar = ttk.Entry(self.tab_motos)
        self.entry_campo_atualizar.grid(row=12, column=1, padx=5, pady=5)

        label_novo_valor = ttk.Label(self.tab_motos, text="Novo Valor:")
        label_novo_valor.grid(row=13, column=0, padx=5, pady=5)
        self.entry_valor_atualizar = ttk.Entry(self.tab_motos)
        self.entry_valor_atualizar.grid(row=13, column=1, padx=5, pady=5)

        btn_atualizar_moto = ttk.Button(self.tab_motos, text="Atualizar", command=self.atualizar_moto)
        btn_atualizar_moto.grid(row=14, column=1, pady=10)

        # Seção para listar motos
        label_listar_motos = ttk.Label(self.tab_motos, text="Listar Motos:")
        label_listar_motos.grid(row=15, column=0, pady=5)

        # Botão para listar motos e abrir um pop-up
        btn_listar_motos = ttk.Button(self.tab_motos, text="Listar Motos", command=self.listar_motos_popup)
        btn_listar_motos.grid(row=15, column=1, pady=5)






        # Aba de Clientes
        self.tab_cliente = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_cliente, text="Clientes")
        
        # Seção para adicionar cliente
        label_adicionar_cliente = ttk.Label(self.tab_cliente, text="Adicionar Cliente")
        label_adicionar_cliente.grid(row=0, column=0, columnspan=2, pady=5)

        label_nome = ttk.Label(self.tab_cliente, text="Nome:")
        label_nome.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nome = ttk.Entry(self.tab_cliente)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

        label_cpf = ttk.Label(self.tab_cliente, text="CPF:")
        label_cpf.grid(row=2, column=0, padx=5, pady=5)
        self.entry_cpf = ttk.Entry(self.tab_cliente)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5)

        label_email = ttk.Label(self.tab_cliente, text="Email:")
        label_email.grid(row=3, column=0, padx=5, pady=5)
        self.entry_email = ttk.Entry(self.tab_cliente)
        self.entry_email.grid(row=3, column=1, padx=5, pady=5)

        btn_adicionar_cliente = ttk.Button(self.tab_cliente, text="Adicionar", command=self.adicionar_cliente)
        btn_adicionar_cliente.grid(row=4, column=1, pady=10)

        # # Seção para remover cliente
        # label_remover_cliente = ttk.Label(self.tab_cliente, text="Remover Cliente")
        # label_remover_cliente.grid(row=5, column=0, pady=5)

        # label_remover_cpf = ttk.Label(self.tab_cliente, text="CPF:")
        # label_remover_cpf.grid(row=6, column=0, padx=5, pady=5)
        # self.entry_remover_cpf = ttk.Entry(self.tab_cliente)
        # self.entry_remover_cpf.grid(row=6, column=1, padx=5, pady=5)

        # btn_remover_cliente = ttk.Button(self.tab_cliente, text="Remover", command=self.remover_cliente)
        # btn_remover_cliente.grid(row=7, column=1, pady=10)

        # Seção para atualizar cliente
        label_atualizar_cliente = ttk.Label(self.tab_cliente, text="Atualizar Cliente")
        label_atualizar_cliente.grid(row=8, column=0, columnspan=2, pady=5)

        label_atualizar_cpf = ttk.Label(self.tab_cliente, text="CPF do Cliente:")
        label_atualizar_cpf.grid(row=9, column=0, padx=5, pady=5)
        self.entry_atualizar_cpf = ttk.Entry(self.tab_cliente)
        self.entry_atualizar_cpf.grid(row=9, column=1, padx=5, pady=5)

        label_campo_atualizar = ttk.Label(self.tab_cliente, text="Campo a Atualizar:")
        label_campo_atualizar.grid(row=10, column=0, padx=5, pady=5)
        self.entry_campo_atualizar = ttk.Entry(self.tab_cliente)
        self.entry_campo_atualizar.grid(row=10, column=1, padx=5, pady=5)

        label_novo_valor = ttk.Label(self.tab_cliente, text="Novo Valor:")
        label_novo_valor.grid(row=11, column=0, padx=5, pady=5)
        self.entry_novo_valor = ttk.Entry(self.tab_cliente)
        self.entry_novo_valor.grid(row=11, column=1, padx=5, pady=5)

        btn_atualizar_cliente = ttk.Button(self.tab_cliente, text="Atualizar", command=self.atualizar_cliente)
        btn_atualizar_cliente.grid(row=12, column=1, pady=10)

        # Label para a seção de listar clientes
        label_listar_clientes = ttk.Label(self.tab_cliente, text="Listar Clientes: ")
        label_listar_clientes.grid(row=14, column=0,pady=5)

        # Botão para listar clientes e abrir um pop-up
        btn_listar_clientes = ttk.Button(self.tab_cliente, text="Listar Clientes", command=self.listar_clientes_popup)
        btn_listar_clientes.grid(row=14, column=1, columnspan=2, pady=5)




        # Aba de Vendas
        self.tab_venda = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_venda, text="Vendas")

        # Seção para gerar venda
        label_gerar_venda = ttk.Label(self.tab_venda, text="Gerar Venda")
        label_gerar_venda.grid(row=0, column=0, columnspan=2, pady=5)

        label_cpf_cliente = ttk.Label(self.tab_venda, text="CPF do Cliente:")
        label_cpf_cliente.grid(row=1, column=0, padx=5, pady=5)
        self.entry_cpf_cliente = ttk.Entry(self.tab_venda)
        self.entry_cpf_cliente.grid(row=1, column=1, padx=5, pady=5)

        label_chassi_moto = ttk.Label(self.tab_venda, text="Chassi da Moto:")
        label_chassi_moto.grid(row=2, column=0, padx=5, pady=5)
        self.entry_chassi_moto = ttk.Entry(self.tab_venda)
        self.entry_chassi_moto.grid(row=2, column=1, padx=5, pady=5)

        btn_gerar_venda = ttk.Button(self.tab_venda, text="Gerar Venda", command=self.adicionar_venda)
        btn_gerar_venda.grid(row=3, column=1, pady=10)

        # Label para a seção de listar vendas
        label_listar_vendas = ttk.Label(self.tab_venda, text="Listar Vendas: ")
        label_listar_vendas.grid(row=14, column=0, pady=5)

        # Botão para listar vendas e abrir um pop-up
        btn_listar_vendas = ttk.Button(self.tab_venda, text="Listar Vendas", command=self.listar_vendas_popup)
        btn_listar_vendas.grid(row=14, column=1, pady=10)





        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Seção para agendar revisão
        label_agendar_revisao = ttk.Label(self.tab_agenda, text="Agendar Revisão")
        label_agendar_revisao.grid(row=0, column=0, columnspan=2, pady=5)

        label_id_moto_revisao = ttk.Label(self.tab_agenda, text="ID da Moto:")
        label_id_moto_revisao.grid(row=1, column=0, padx=5, pady=5)
        self.entry_id_moto_revisao = ttk.Entry(self.tab_agenda)
        self.entry_id_moto_revisao.grid(row=1, column=1, padx=5, pady=5)

        label_data_revisao = ttk.Label(self.tab_agenda, text="Data da Revisão:")
        label_data_revisao.grid(row=2, column=0, padx=5, pady=5)
        self.entry_data_revisao = ttk.Entry(self.tab_agenda)
        self.entry_data_revisao.grid(row=2, column=1, padx=5, pady=5)

        label_mecanico_revisao = ttk.Label(self.tab_agenda, text="Mecânico Responsável:")
        label_mecanico_revisao.grid(row=3, column=0, padx=5, pady=5)
        self.entry_mecanico_revisao = ttk.Entry(self.tab_agenda)
        self.entry_mecanico_revisao.grid(row=3, column=1, padx=5, pady=5)

        btn_agendar_revisao = ttk.Button(self.tab_agenda, text="Agendar Revisão", command="")#self.agendar_revisao)
        btn_agendar_revisao.grid(row=4, column=1, pady=10)

        # Seção para listar revisões agendadas
        label_listar_revisoes = ttk.Label(self.tab_agenda, text="Mostrar Agenda:")
        label_listar_revisoes.grid(row=5, column=0, pady=5)

        # Botão para listar revisões e abrir um pop-up
        btn_listar_revisoes = ttk.Button(self.tab_agenda, text="Listar Revisões", command="")#self.listar_revisoes_popup)
        btn_listar_revisoes.grid(row=5, column=1, pady=5)






    # Métodos CRUD para motos
    def adicionar_moto(self):
        modelo = self.entry_modelo.get()
        ano = self.entry_ano.get()
        preco = float(self.entry_preco.get())  # Converter para float, caso seja necessário
        cor = self.entry_cor.get()
        chassi = self.entry_chassi.get()  # Supondo que você tenha um campo para o chassi

        moto = Moto(modelo=modelo, ano=ano, preco=preco, cor=cor, chassi=chassi)
        self.moto_dao.adicionar_moto(moto)
        print("Moto adicionada com sucesso!")

    def atualizar_moto(self):
        id_moto = self.entry_id_moto_atualizar.get()
        campo = self.entry_campo_atualizar.get()
        novo_valor = self.entry_valor_atualizar.get()

        # Verifica qual campo será atualizado e o formata corretamente
        if campo.lower() in ["preco", "ano"]:  # Certificando-se de que o preço e o ano são do tipo correto
            novo_valor = float(novo_valor) if campo.lower() == "preco" else int(novo_valor)

        self.moto_dao.atualizar_moto(id_moto, campo, novo_valor)
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
        btn_fechar = ttk.Button(popup, text="Fechar", command=popup.destroy)
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
        btn_fechar = ttk.Button(popup, text="Fechar", command=popup.destroy)
        btn_fechar.pack(pady=10)


    def adicionar_venda(self):
        cpf_cliente = self.entry_cpf_cliente.get()
        chassi_moto = self.entry_chassi_moto.get()

        # Gerar a data atual da venda
        data_venda = datetime.datetime.now().strftime("%Y-%m-%d")

        # Definir o status inicial da venda (por exemplo, "Em andamento")
        status = "Preparando"

        preco = self.moto_dao.buscar_preco(chassi_moto)

        # Cria um objeto Venda apenas com CPF do cliente, chassi da moto, data e status
        venda = Venda(data=data_venda, status=status, chassi_moto=chassi_moto, cpf_cliente=cpf_cliente, preco=preco[0])
        
        # Chama o método do DAO para adicionar a venda no banco de dados
        self.venda_dao.adicionar_venda(venda)
        print("Venda gerada com sucesso!")




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
        btn_fechar = ttk.Button(popup, text="Fechar", command=popup.destroy)
        btn_fechar.pack(pady=10)




    
    # def agendar_revisao(self):
    #     # Obter dados da entrada
    #     id_moto = self.entry_id_moto_revisao.get()
    #     data_revisao = self.entry_data_revisao.get()
    #     mecanico = self.entry_mecanico_revisao.get()

    #     # Validar entradas
    #     if not id_moto or not data_revisao or not mecanico:
    #         messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
    #         return

    #     # Inserir revisão no banco de dados
    #     try:
    #         self.revisao_dao.agendar_revisao(id_moto, data_revisao, mecanico)
    #         messagebox.showinfo("Sucesso", "Revisão agendada com sucesso!")
    #         # Limpar campos após agendar
    #         self.entry_id_moto_revisao.delete(0, tk.END)
    #         self.entry_data_revisao.delete(0, tk.END)
    #         self.entry_mecanico_revisao.delete(0, tk.END)
    #     except Exception as e:
    #         messagebox.showerror("Erro", f"Erro ao agendar revisão: {e}")


    # def listar_revisoes_popup(self):
    #     # Criar uma nova janela (pop-up) para listar as revisões
    #     popup = tk.Toplevel(self.root)
    #     popup.title("Revisões Agendadas")

    #     # Definir o tamanho da nova janela
    #     popup.geometry("600x300")

    #     # Criar um Treeview para exibir as revisões como uma tabela
    #     colunas = ('ID Moto', 'Data', 'Mecânico')
    #     tree = ttk.Treeview(popup, columns=colunas, show='headings')

    #     # Definir os títulos das colunas
    #     tree.heading('ID Moto', text='ID Moto')
    #     tree.heading('Data', text='Data')
    #     tree.heading('Mecânico', text='Mecânico')

    #     # Ajustar o tamanho das colunas
    #     tree.column('ID Moto', width=100)
    #     tree.column('Data', width=100)
    #     tree.column('Mecânico', width=150)

    #     # Inserir os dados das revisões no Treeview
    #     revisoes = self.revisao_dao.listar_revisoes()
        
    #     if revisoes:
    #         for revisao in revisoes:
    #             id_moto = revisao[0]  # Primeiro campo (ID Moto)
    #             data = revisao[1]  # Segundo campo (Data)
    #             mecanico = revisao[2]  # Terceiro campo (Mecânico)
    #             tree.insert('', tk.END, values=(id_moto, data, mecanico))
    #     else:
    #         # Caso não haja revisões, mostrar uma linha indicando isso
    #         tree.insert('', tk.END, values=('Nenhuma revisão encontrada', '', ''))

    #     # Posicionar o Treeview na janela pop-up
    #     tree.pack(padx=10, pady=10, expand=True, fill='both')

    #     # Adicionar um botão para fechar o pop-up
    #     btn_fechar = ttk.Button(popup, text="Fechar", command=popup.destroy)
    #     btn_fechar.pack(pady=10)

    
# Inicializando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = GerenteApp(root)
    root.mainloop()


    # revisões não está funcionando, não está criando nem listando
    # criar a tela adicionar funcionnário, crud
