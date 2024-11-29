from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ..estilos import estilos
from backend.Routes import Funcionario,FuncionarioDAO

class AbaFuncionarios(estilos):
    def __init__(self,root,notebook):
        super().__init__(root)
        self.funcionario_dao = FuncionarioDAO('db.db')

        # Adicionando a aba de Funcionários
        self.tab_funcionarios = ttk.Frame(notebook, padding=10)
        notebook.add(self.tab_funcionarios, text="Funcionários")

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

        # Botão de deslogar na parte superior direita, ao lado de "Adicionar Moto"
        btn_sair = ttk.Button(self.tab_funcionarios, text="Sair", style="Custom.TButton", command=self.sair)
        btn_sair.grid(row=14, column=1, padx=0, pady=0, sticky="e")

        self.listar_funcionarios()

##########################################################################
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
        for i in self.tree.get_children():
            self.tree.delete(i)

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

                self.tree.insert('', 'end', values=(nome_funcionario, cpf_funcionario, cargo_funcionario))
        else:
            messagebox.showinfo("Informação", "Nenhum funcionário encontrado.")



    def editar_funcionario(self):
        # Obter o funcionário selecionado
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione um funcionário para editar.")
            return

        item = self.tree.item(selected_item)
        funcionario_nome = item['values'][0]  # Nome
        funcionario_cpf = item['values'][1]    # CPF
        funcionario_cargo = item['values'][2]  # Cargo

        # # Aqui você deve obter os dados de usuario e senha do banco de dados se necessário
        # usuario_atual = "usuario_exemplo"  # Substitua isso pelo valor correto
        # senha_atual = "senha_exemplo"      # Substitua isso pelo valor correto

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
            funcionario_atualizado = Funcionario(nome=novo_nome,cpf=funcionario_cpf, usuario=funcionario_cpf, senha=funcionario_cpf, funcao=novo_cargo)

            # Chamar o método para atualizar o funcionário no banco de dados
            self.funcionario_dao.atualizar_funcionario(funcionario_atualizado)

            # Fechar a janela popup
            editar_popup.destroy()

            messagebox.showinfo("Sucesso", "Funcionario atualizado com sucesso!")

            # Atualizar a lista de funcionários no Treeview
            self.listar_funcionarios()

        btn_salvar = ttk.Button(editar_popup, text="Salvar", style="Custom.TButton", command=salvar_edicao)
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

        # Tornar a janela modal
        editar_popup.transient(self.root)
        editar_popup.grab_set()
        self.root.wait_window(editar_popup)

    def deletar_funcionario(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione um funcionário para deletar.")
            return

        item = self.tree.item(selected_item)
        funcionario_id = item['values'][1]

        try:
            self.funcionario_dao.deletar_funcionario(funcionario_id)
            messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
            self.listar_funcionarios()  # Atualizar a lista
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar funcionário: {e}")
    