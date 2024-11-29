from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ..estilos import estilos
from backend.Routes import Venda,VendaDAO, ClienteDAO, MotoDAO
import datetime

class AbaVendas(estilos):
    def __init__(self,root,notebook,cargo):
        super().__init__(root)

        self.cliente_dao = ClienteDAO('db.db')
        self.venda_dao = VendaDAO('db.db')
        self.moto_dao = MotoDAO('db.db')

        if cargo == "gerente" or cargo == "vendedor":
            valor = 4
        else: 
            valor = 1       

        # Aba de Vendas
        self.tab_venda = ttk.Frame(notebook, padding=10)
        notebook.add(self.tab_venda, text="Vendas")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_venda.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_venda.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_venda.rowconfigure(row, weight=1)
        
        
        if cargo == "gerente" or cargo == "vendedor":
            # Seção para gerar venda
            label_gerar_venda = ttk.Label(self.tab_venda, text="Gerar Venda", **self.estilo_label)
            label_gerar_venda.grid(row=0, column=0, columnspan=2, pady=(0, 15))

            label_cpf_cliente = ttk.Label(self.tab_venda, text="CPF Cliente:", **self.estilo_label)
            label_cpf_cliente.grid(row=1, column=0, padx=5, pady=3, sticky="e")
            self.entry_cpf_cliente = ttk.Entry(self.tab_venda, **self.estilo_entrada)
            self.entry_cpf_cliente.grid(row=1, column=1, padx=5, pady=3, sticky="w")

            label_chassi_moto = ttk.Label(self.tab_venda, text="Chassi:", **self.estilo_label)
            label_chassi_moto.grid(row=2, column=0, padx=5, pady=3, sticky="e")
            self.entry_chassi_moto = ttk.Entry(self.tab_venda, **self.estilo_entrada)
            self.entry_chassi_moto.grid(row=2, column=1, padx=5, pady=3, sticky="w")

            btn_gerar_venda = ttk.Button(self.tab_venda, text="Gerar Venda", style="Custom.TButton", command=self.adicionar_venda)
            btn_gerar_venda.grid(row=3, column=1, pady=5, sticky="w")
        else:
            pass

        # Seção para listar 
        label_listar_vendas = ttk.Label(self.tab_venda, text="Lista de Vendas", **self.estilo_label)
        label_listar_vendas.grid(row=valor, column=0, pady=(3), columnspan=2)

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
        self.tree_venda.grid(row=(valor+1), column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        if cargo != "gerente":
            pass
        else:
            btn_editar_venda = ttk.Button(self.tab_venda, text="Editar Venda", style="Custom.TButton", command=self.editar_venda)
            btn_editar_venda.grid(row=8, column=0, pady=10, sticky="n")    
            
            btn_deletar_venda = ttk.Button(self.tab_venda, text="Deletar Venda", style="Custom.TButton", command=self.deletar_venda)
            btn_deletar_venda.grid(row=8, column=1, pady=10, sticky="n")

        # Botão de deslogar na parte superior direita, ao lado de "Adicionar Moto"
        btn_sair = ttk.Button(self.tab_venda, text="Sair", style="Custom.TButton", command=self.sair)
        btn_sair.grid(row=14, column=1, padx=0, pady=0, sticky="e")

        self.listar_vendas()

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

                messagebox.showinfo("Sucesso", "Venda adicionada com sucesso!")
                self.entry_cpf_cliente.delete(0, tk.END)
                self.entry_chassi_moto.delete(0, tk.END)

                self.listar_vendas()
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
        for i in self.tree_venda.get_children():
            self.tree_venda.delete(i)

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

                self.tree_venda.insert('', tk.END, values=(id_venda, chassi, cpf_cliente, data, status, preco))  # Adicionando o preço às inserções
        else:
            messagebox.showinfo("Informação", "Nenhum funcionário encontrado.") 

    def editar_venda(self):
        # Obter a venda selecionada
        selected_item = self.tree_venda.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione uma venda para editar.")
            return

        item = self.tree_venda.item(selected_item)
        venda_id = item['values'][0]  # ID da venda
        venda_chassi = item['values'][1]  # Chassi
        venda_cpf = item['values'][2]  # CPF do cliente
        venda_data = item['values'][3]  # Data da venda
        venda_status = item['values'][4]  # Status
        venda_preco = item['values'][5]  # Preço

        # Criar uma nova janela para editar a venda
        editar_popup = tk.Toplevel(self.root)
        editar_popup.title("Editar Venda")

        # Criar campos de entrada para editar os dados
        label_id = ttk.Label(editar_popup, text="ID:")
        label_id.grid(row=0, column=0, padx=5, pady=5)
        entry_id = ttk.Entry(editar_popup)
        entry_id.insert(0, venda_id)  
        entry_id.config(state='readonly')  # Não permitir editar
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        label_chassi = ttk.Label(editar_popup, text="Chassi:")
        label_chassi.grid(row=1, column=0, padx=5, pady=5)
        entry_chassi = ttk.Entry(editar_popup)
        entry_chassi.insert(0, venda_chassi)
        entry_chassi.config(state='readonly')  # Não permitir editar   
        entry_chassi.grid(row=1, column=1, padx=5, pady=5)

        label_data = ttk.Label(editar_popup, text="Data:")
        label_data.grid(row=2, column=0, padx=5, pady=5)
        entry_data = ttk.Entry(editar_popup)
        entry_data.insert(0, venda_data)  
        entry_data.config(state='readonly')  # Não permitir editar 
        entry_data.grid(row=2, column=1, padx=5, pady=5)

        label_cpf = ttk.Label(editar_popup, text="CPF:")
        label_cpf.grid(row=3, column=0, padx=5, pady=5)
        entry_cpf = ttk.Entry(editar_popup)
        entry_cpf.insert(0, venda_cpf)  
        entry_cpf.config(state='readonly')  # Não permitir editar 
        entry_cpf.grid(row=3, column=1, padx=5, pady=5)

        label_status = ttk.Label(editar_popup, text="Status:")
        label_status.grid(row=4, column=0, padx=5, pady=5)
        entry_status = ttk.Entry(editar_popup)
        entry_status.insert(0, venda_status)  
        entry_status.grid(row=4, column=1, padx=5, pady=5)

        label_preco = ttk.Label(editar_popup, text="Preço:")
        label_preco.grid(row=5, column=0, padx=5, pady=5)
        entry_preco = ttk.Entry(editar_popup)
        entry_preco.insert(0, venda_preco)  
        entry_preco.grid(row=5, column=1, padx=5, pady=5)

        # Função para salvar as alterações
        def salvar_edicao():
            novo_status = entry_status.get()
            novo_preco = entry_preco.get()

            # Criar uma venda com os dados atualizados
            venda_atualizada = Venda(data=venda_data, status=novo_status, chassi_moto=venda_chassi, 
                                    cpf_cliente=venda_cpf, preco=novo_preco)

            # Chamar o método para atualizar a venda no banco de dados
            self.venda_dao.atualizar_venda(venda_atualizada,venda_id)

            # Fechar a janela popup
            editar_popup.destroy()

            messagebox.showinfo("Sucesso", "Venda atualizada com sucesso!")

            # Atualizar a lista de vendas no Treeview
            self.listar_vendas()

        # Botão para salvar as alterações
        btn_salvar = ttk.Button(editar_popup, text="Salvar", style="Custom.TButton", command=salvar_edicao)
        btn_salvar.grid(row=6, column=0, columnspan=2, pady=10)

        # Tornar a janela modal
        editar_popup.transient(self.root)
        editar_popup.grab_set()
        self.root.wait_window(editar_popup)

    def deletar_venda(self):
        # Obter a venda selecionada
        selected_item = self.tree_venda.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione uma venda para deletar.")
            return

        item = self.tree_venda.item(selected_item)
        venda_id = item['values'][0]

        try:
            # Remover a venda no banco de dados
            self.venda_dao.deletar_venda(venda_id)
            messagebox.showinfo("Sucesso", "Venda deletada com sucesso!")
            # Atualizar a lista de vendas
            self.listar_vendas()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar a venda: {e}")
