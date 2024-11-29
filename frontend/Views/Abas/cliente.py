from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ..estilos import estilos
from backend.Routes import Cliente,ClienteDAO

class AbaClientes(estilos):
    def __init__(self,root,notebook):
        super().__init__(root)

        self.cliente_dao = ClienteDAO('db.db')
        # Aba de Clientes
        self.tab_cliente = ttk.Frame(notebook, padding=15)
        notebook.add(self.tab_cliente, text="Clientes")

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

        # Botão de deslogar na parte superior direita, ao lado de "Adicionar Moto"
        btn_sair = ttk.Button(self.tab_cliente, text="Sair", style="Custom.TButton", command=self.sair)
        btn_sair.grid(row=14, column=1, padx=0, pady=0, sticky="e")

        # Listar clientes
        self.listar_clientes()
    
########################################################

# Métodos CRUD para clientes
    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()

        cliente = Cliente(nome=nome, cpf=cpf, email=email)
        self.cliente_dao.adicionar_cliente(cliente)

        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)


        self.listar_clientes()

    def remover_cliente(self):
        cpf = self.entry_remover_cpf.get()
        self.cliente_dao.remover_cliente(cpf)
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")

    def editar_cliente(self):
        # Obter o funcionário selecionado
        selected_item = self.tree_cliente.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione um cliente para editar.")
            return

        item = self.tree_cliente.item(selected_item)
        cliente_cpf = item['values'][0]  # cpf
        cliente_nome = item['values'][1]    # nome
        cliente_email = item['values'][2]  # email


        # # Aqui você deve obter os dados de usuario e senha do banco de dados se necessário
        # usuario_atual = "usuario_exemplo"  # Substitua isso pelo valor correto
        # senha_atual = "senha_exemplo"      # Substitua isso pelo valor correto

        # Criar uma nova janela para editar o funcionário
        editar_popup = tk.Toplevel(self.root)
        editar_popup.title("Editar Cliente")

        # Criar campos de entrada para editar os dados
        label_chassi = ttk.Label(editar_popup, text="Cliente:")
        label_chassi.grid(row=0, column=0, padx=5, pady=5)
        entry_chassi = ttk.Entry(editar_popup)
        entry_chassi.insert(0, cliente_cpf)  
        entry_chassi.config(state='readonly')  # Não permitir editar o Chassi
        entry_chassi.grid(row=0, column=1, padx=5, pady=5)

        label_nome = ttk.Label(editar_popup, text="Nome:")
        label_nome.grid(row=1, column=0, padx=5, pady=5)
        entry_nome = ttk.Entry(editar_popup)
        entry_nome.insert(0, cliente_nome)  # Preencher o nome atual
        entry_nome.grid(row=1, column=1, padx=5, pady=5)

        label_email = ttk.Label(editar_popup, text="email:")
        label_email.grid(row=2, column=0, padx=5, pady=5)
        entry_email = ttk.Entry(editar_popup)
        entry_email.insert(0, cliente_email)  # Preencher o nome atual
        entry_email.grid(row=2, column=1, padx=5, pady=5)

        # Botão para salvar as alterações
        def salvar_edicao():
            novo_nome = entry_nome.get()
            novo_email = entry_email.get()


            # Criar um objeto Funcionario com os dados atualizados
            cliente_atualizado = Cliente(cpf=cliente_cpf,nome=novo_nome,email=novo_email)

            # Chamar o método para atualizar o funcionário no banco de dados
            self.cliente_dao.atualizar_cliente(cliente_atualizado)

            # Fechar a janela popup
            editar_popup.destroy()

            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")

            # Atualizar a lista de funcionários no Treeview
            self.listar_clientes()

        btn_salvar = ttk.Button(editar_popup, text="Salvar", style="Custom.TButton", command=salvar_edicao)
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

        # Tornar a janela modal
        editar_popup.transient(self.root)
        editar_popup.grab_set()
        self.root.wait_window(editar_popup)
    
    def listar_clientes(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree_cliente.get_children():
            self.tree_cliente.delete(i)

        # Buscar os funcionários no banco de dados
        clientes = self.cliente_dao.listar_clientes()

        if clientes:
            for cliente in clientes:
                cpf = cliente[0]  # Primeiro campo (CPF)
                nome = cliente[1]  # Segundo campo (Nome)
                email = cliente[2]  # Terceiro campo (Email)
                self.tree_cliente.insert('', tk.END, values=(cpf, nome, email))  # Inserir na tabela
        else:
            messagebox.showinfo("Informação", "Nenhum item encontrado.")

    def sair(self):
        resposta = messagebox.askyesno("Sair", "Você tem certeza que deseja sair?")
        if resposta:
            # Fechar a janela principal ou redirecionar para a tela de login
            self.root.quit()