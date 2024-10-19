import tkinter as tk
from tkinter import ttk
from backend.Routes import AgendaRevisaoDAO,ClienteDAO,FuncionarioDAO,MotoDAO,VendaDAO

class Cliente:
    def __init__(self, cpf, nome, email):
        self.cpf = cpf
        self.nome = nome
        self.email = email

class Moto:
    def __init__(self, chassi, ano, preco, cor, modelo):
        self.chassi = chassi
        self.ano = ano
        self.preco = preco
        self.cor = cor
        self.modelo = modelo

class AgendaRevisao:
    def __init__(self, data, custo, status_revisao, chassi_moto, cpf_cliente):
        self.data = data
        self.custo = custo
        self.status_revisao = status_revisao
        self.chassi_moto = chassi_moto
        self.cpf_cliente = cpf_cliente

class Venda:
    def __init__(self, data, status, chassi_moto, cpf_cliente):
        self.data = data
        self.status = status
        self.chassi_moto = chassi_moto
        self.cpf_cliente = cpf_cliente

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

        # Adicionando a aba de Motos
        self.tab_motos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_motos, text="Motos")

        # Seção de Atualizar Moto
        self.label_atualizar = ttk.Label(self.tab_motos, text="Atualizar Moto")
        self.label_atualizar.grid(row=0, column=0, columnspan=2, pady=5)

        self.label_id_moto_atualizar = ttk.Label(self.tab_motos, text="ID da Moto:")
        self.label_id_moto_atualizar.grid(row=1, column=0, sticky=tk.W)
        self.entry_id_moto_atualizar = ttk.Entry(self.tab_motos)
        self.entry_id_moto_atualizar.grid(row=1, column=1)

        self.label_campo_atualizar = ttk.Label(self.tab_motos, text="Campo a Atualizar:")
        self.label_campo_atualizar.grid(row=2, column=0, sticky=tk.W)
        self.entry_campo_atualizar = ttk.Entry(self.tab_motos)
        self.entry_campo_atualizar.grid(row=2, column=1)

        self.label_valor_atualizar = ttk.Label(self.tab_motos, text="Novo Valor:")
        self.label_valor_atualizar.grid(row=3, column=0, sticky=tk.W)
        self.entry_valor_atualizar = ttk.Entry(self.tab_motos)
        self.entry_valor_atualizar.grid(row=3, column=1)

        self.btn_atualizar = ttk.Button(self.tab_motos, text="Atualizar", command=self.atualizar_moto)
        self.btn_atualizar.grid(row=4, column=0, columnspan=2, pady=5)

        # Seção de Remover Moto
        self.label_remover = ttk.Label(self.tab_motos, text="Remover Moto")
        self.label_remover.grid(row=5, column=0, columnspan=2, pady=5)

        self.label_id_moto_remover = ttk.Label(self.tab_motos, text="ID da Moto:")
        self.label_id_moto_remover.grid(row=6, column=0, sticky=tk.W)
        self.entry_id_moto_remover = ttk.Entry(self.tab_motos)
        self.entry_id_moto_remover.grid(row=6, column=1)

        self.btn_remover = ttk.Button(self.tab_motos, text="Remover", command=self.remover_moto)
        self.btn_remover.grid(row=7, column=0, columnspan=2, pady=5)

        # Seção de Adicionar Moto
        self.label_adicionar = ttk.Label(self.tab_motos, text="Adicionar Moto")
        self.label_adicionar.grid(row=8, column=0, columnspan=2, pady=5)

        self.label_modelo = ttk.Label(self.tab_motos, text="Modelo:")
        self.label_modelo.grid(row=9, column=0, sticky=tk.W)
        self.entry_modelo = ttk.Entry(self.tab_motos)
        self.entry_modelo.grid(row=9, column=1)

        self.label_ano = ttk.Label(self.tab_motos, text="Ano:")
        self.label_ano.grid(row=10, column=0, sticky=tk.W)
        self.entry_ano = ttk.Entry(self.tab_motos)
        self.entry_ano.grid(row=10, column=1)

        self.label_preco = ttk.Label(self.tab_motos, text="Preço:")
        self.label_preco.grid(row=11, column=0, sticky=tk.W)
        self.entry_preco = ttk.Entry(self.tab_motos)
        self.entry_preco.grid(row=11, column=1)

        self.label_cor = ttk.Label(self.tab_motos, text="Cor:")
        self.label_cor.grid(row=12, column=0, sticky=tk.W)
        self.entry_cor = ttk.Entry(self.tab_motos)
        self.entry_cor.grid(row=12, column=1)

        self.chassi = ttk.Label(self.tab_motos, text="Chassi")
        self.chassi.grid(row=13, column=0, sticky=tk.W)
        self.entry_chassi = ttk.Entry(self.tab_motos)
        self.entry_chassi.grid(row=13, column=1)

        self.btn_adicionar = ttk.Button(self.tab_motos, text="Adicionar", command=self.adicionar_moto)
        self.btn_adicionar.grid(row=14, column=0, columnspan=2, pady=5)





        # Aba de Clientes
        self.tab_cliente = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_cliente, text="Clientes")
        
        # Seção para adicionar cliente
        label_adicionar_cliente = ttk.Label(self.tab_cliente, text="Adicionar Cliente")
        label_adicionar_cliente.grid(row=0, column=0, pady=5)

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

        # Seção para remover cliente
        label_remover_cliente = ttk.Label(self.tab_cliente, text="Remover Cliente")
        label_remover_cliente.grid(row=5, column=0, pady=5)

        label_remover_cpf = ttk.Label(self.tab_cliente, text="CPF:")
        label_remover_cpf.grid(row=6, column=0, padx=5, pady=5)
        self.entry_remover_cpf = ttk.Entry(self.tab_cliente)
        self.entry_remover_cpf.grid(row=6, column=1, padx=5, pady=5)

        btn_remover_cliente = ttk.Button(self.tab_cliente, text="Remover", command=self.remover_cliente)
        btn_remover_cliente.grid(row=7, column=1, pady=10)

        # Seção para atualizar cliente
        label_atualizar_cliente = ttk.Label(self.tab_cliente, text="Atualizar Cliente")
        label_atualizar_cliente.grid(row=8, column=0, pady=5)

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





        # Adicionando a aba de Vendas
        self.tab_vendas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_vendas, text="Vendas")

        # Seção de Registrar Venda
        self.label_registrar_venda = ttk.Label(self.tab_vendas, text="Registrar Venda")
        self.label_registrar_venda.grid(row=0, column=0, columnspan=2, pady=5)

        self.label_id_moto_venda = ttk.Label(self.tab_vendas, text="ID da Moto:")
        self.label_id_moto_venda.grid(row=1, column=0, sticky=tk.W)
        self.entry_id_moto_venda = ttk.Entry(self.tab_vendas)
        self.entry_id_moto_venda.grid(row=1, column=1)

        self.label_cpf_cliente_venda = ttk.Label(self.tab_vendas, text="CPF do Cliente:")
        self.label_cpf_cliente_venda.grid(row=2, column=0, sticky=tk.W)
        self.entry_cpf_cliente_venda = ttk.Entry(self.tab_vendas)
        self.entry_cpf_cliente_venda.grid(row=2, column=1)

        self.btn_registrar_venda = ttk.Button(self.tab_vendas, text="Registrar Venda")
        self.btn_registrar_venda.grid(row=3, column=0, columnspan=2, pady=5)





        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Seção de Agendar Revisão
        self.label_agendar_revisao = ttk.Label(self.tab_agenda, text="Agendar Revisão")
        self.label_agendar_revisao.grid(row=0, column=0, columnspan=2, pady=5)

        self.label_id_moto_revisao = ttk.Label(self.tab_agenda, text="ID da Moto:")
        self.label_id_moto_revisao.grid(row=1, column=0, sticky=tk.W)
        self.entry_id_moto_revisao = ttk.Entry(self.tab_agenda)
        self.entry_id_moto_revisao.grid(row=1, column=1)

        self.label_data_revisao = ttk.Label(self.tab_agenda, text="Data da Revisão:")
        self.label_data_revisao.grid(row=2, column=0, sticky=tk.W)
        self.entry_data_revisao = ttk.Entry(self.tab_agenda)
        self.entry_data_revisao.grid(row=2, column=1)

        self.label_mecanico_revisao = ttk.Label(self.tab_agenda, text="Mecânico Responsável:")
        self.label_mecanico_revisao.grid(row=3, column=0, sticky=tk.W)
        self.entry_mecanico_revisao = ttk.Entry(self.tab_agenda)
        self.entry_mecanico_revisao.grid(row=3, column=1)

        self.btn_agendar_revisao = ttk.Button(self.tab_agenda, text="Agendar Revisão")
        self.btn_agendar_revisao.grid(row=4, column=0, columnspan=2, pady=5)


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
        cpf = self.entry_atualizar_cpf.get()
        campo = self.entry_campo_atualizar.get()
        novo_valor = self.entry_novo_valor.get()

        self.cliente_dao.atualizar_cliente(cpf, campo, novo_valor)
        print("Cliente atualizado com sucesso!")

# Inicializando a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = GerenteApp(root)
    root.mainloop()
