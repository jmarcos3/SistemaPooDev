import tkinter as tk
from tkinter import ttk
from backend.Routes import AgendaRevisaoDAO,ClienteDAO,FuncionarioDAO,MotoDAO,VendaDAO

class GerenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")

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

        self.btn_atualizar = ttk.Button(self.tab_motos, text="Atualizar")
        self.btn_atualizar.grid(row=4, column=0, columnspan=2, pady=5)

        # Seção de Remover Moto
        self.label_remover = ttk.Label(self.tab_motos, text="Remover Moto")
        self.label_remover.grid(row=5, column=0, columnspan=2, pady=5)

        self.label_id_moto_remover = ttk.Label(self.tab_motos, text="ID da Moto:")
        self.label_id_moto_remover.grid(row=6, column=0, sticky=tk.W)
        self.entry_id_moto_remover = ttk.Entry(self.tab_motos)
        self.entry_id_moto_remover.grid(row=6, column=1)

        self.btn_remover = ttk.Button(self.tab_motos, text="Remover")
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

        self.label_id_compra = ttk.Label(self.tab_motos, text="ID da Compra (opcional):")
        self.label_id_compra.grid(row=13, column=0, sticky=tk.W)
        self.entry_id_compra = ttk.Entry(self.tab_motos)
        self.entry_id_compra.grid(row=13, column=1)

        self.btn_adicionar = ttk.Button(self.tab_motos, text="Adicionar")
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

        # Inicia o loop principal
        self.root.mainloop()

    def adicionar_cliente(self):
        # Implementar lógica para adicionar cliente
        pass

    def remover_cliente(self):
        # Implementar lógica para remover cliente
        pass

    def atualizar_cliente(self):
        # Implementar lógica para atualizar cliente
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenteApp(root)