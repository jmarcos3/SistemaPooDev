import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,Revisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

from abc import ABC

class telas(ABC):
    def __init__(self,root, cargo):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        # Inicializando DAOs
        self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
        self.cliente_dao = ClienteDAO('db.db')
        self.venda_dao = VendaDAO('db.db')
        self.agenda_revisao_dao = AgendaRevisaoDAO('db.db')
        self.funcionario_dao = FuncionarioDAO('db.db')

        # Definindo o cargo
        cargos = {
            "gerente": "Gerente",
            "vendedor": "Vendedor",
            "mecanico": "Mecânico",
            "secretaria": "Secretária"
        }

        cargo_nome = cargos.get(cargo, "Cargo não encontrado")

        # Adicionando título com o cargo
        self.title_label = tk.Label(
            root,
            text=f"Concessionária de motos - Cargo: {cargo_nome}",
            font=("Arial", 18, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=0
        )

        self.title_label.pack(fill="x")
        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Estilos personalizados
        self.estilo_label = {"font": ("Arial", 16, "bold"), "foreground": "#333"}
        self.estilo_entrada = {"width": 25, "font": ("Arial", 14)}

        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=("Arial", 14))

###################################################################################

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
        
        self.listar_motos()


    def editar_moto(self):
        # Obter o funcionário selecionado
        selected_item = self.tree_moto.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione uma moto para editar.")
            return

        item = self.tree_moto.item(selected_item)
        moto_chassi = item['values'][0]  # Chassi
        moto_ano = item['values'][1]    # ano
        moto_preço = item['values'][2]  # preço
        moto_cor = item['values'][3]  # cor
        moto_modelo = item['values'][4]  # modelo

        # # Aqui você deve obter os dados de usuario e senha do banco de dados se necessário
        # usuario_atual = "usuario_exemplo"  # Substitua isso pelo valor correto
        # senha_atual = "senha_exemplo"      # Substitua isso pelo valor correto

        # Criar uma nova janela para editar o funcionário
        editar_popup = tk.Toplevel(self.root)
        editar_popup.title("Editar Moto")

        # Criar campos de entrada para editar os dados
        label_chassi = ttk.Label(editar_popup, text="Chassi:")
        label_chassi.grid(row=0, column=0, padx=5, pady=5)
        entry_chassi = ttk.Entry(editar_popup)
        entry_chassi.insert(0, moto_chassi)  
        entry_chassi.config(state='readonly')  # Não permitir editar o Chassi
        entry_chassi.grid(row=0, column=1, padx=5, pady=5)

        label_ano = ttk.Label(editar_popup, text="Ano:")
        label_ano.grid(row=1, column=0, padx=5, pady=5)
        entry_ano = ttk.Entry(editar_popup)
        entry_ano.insert(0, moto_ano)  # Preencher o nome atual
        entry_ano.grid(row=1, column=1, padx=5, pady=5)

        label_preço = ttk.Label(editar_popup, text="Preço:")
        label_preço.grid(row=2, column=0, padx=5, pady=5)
        entry_preço = ttk.Entry(editar_popup)
        entry_preço.insert(0, moto_preço)  # Preencher o nome atual
        entry_preço.grid(row=2, column=1, padx=5, pady=5)

        label_cor = ttk.Label(editar_popup, text="Cor:")
        label_cor.grid(row=3, column=0, padx=5, pady=5)
        entry_cor = ttk.Entry(editar_popup)
        entry_cor.insert(0, moto_cor)  # Preencher o cargo atual
        entry_cor.grid(row=3, column=1, padx=5, pady=5)

        label_modelo = ttk.Label(editar_popup, text="Cor:")
        label_modelo.grid(row=3, column=0, padx=5, pady=5)
        entry_modelo = ttk.Entry(editar_popup)
        entry_modelo.insert(0, moto_cor)  # Preencher o cargo atual
        entry_modelo.grid(row=3, column=1, padx=5, pady=5)

        # Botão para salvar as alterações
        def salvar_edicao():
            novo_ano = entry_ano.get()
            novo_preço= entry_preço.get()
            nova_cor= entry_preço.get()
            novo_modelo= entry_modelo.get()

            # Criar um objeto Funcionario com os dados atualizados
            moto_atualizada = Moto(chassi=moto_chassi,ano=novo_ano,preco=novo_preço, cor=nova_cor, modelo=novo_modelo)

            # Chamar o método para atualizar o funcionário no banco de dados
            self.moto_dao.atualizar_moto(moto_atualizada)

            # Fechar a janela popup
            editar_popup.destroy()

            # Atualizar a lista de funcionários no Treeview
            self.listar_motos()

        btn_salvar = ttk.Button(editar_popup, text="Salvar", style="Custom.TButton", command=salvar_edicao)
        btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)

        # Tornar a janela modal
        editar_popup.transient(self.root)
        editar_popup.grab_set()
        self.root.wait_window(editar_popup)
            
    def deletar_moto(self):
        selected_item = self.tree_moto.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione uma moto para deletar.")
            return

        item = self.tree_moto.item(selected_item)
        moto_id = item['values'][0]
        print(moto_id)

        try:
            self.moto_dao.deletar_moto(moto_id)
            messagebox.showinfo("Sucesso", "Moto deletada com sucesso!")
            self.listar_motos()  # Atualizar a lista
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar moto: {e}")    


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
    # Métodos CRUD para clientes
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

    def remover_cliente(self):
        cpf = self.entry_remover_cpf.get()
        self.cliente_dao.remover_cliente(cpf)
        print("Cliente removido com sucesso!")

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
        venda_data = item['values'][2]  # Data da venda
        venda_cpf = item['values'][3]  # CPF do cliente
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
            self.venda_dao.atualizar_venda(venda_atualizada)

            # Fechar a janela popup
            editar_popup.destroy()

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



######################################################################
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

    def editar_revisao(self):
        # Obter o funcionário selecionado
        selected_item = self.tree_revisao.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione um funcionário para editar.")
            return

        item = self.tree_revisao.item(selected_item)
        revisao_id = item['values'][0]  # id
        revisao_chassi = item['values'][1]    # chassi
        revisao_data = item['values'][2]  # data
        revisao_cpf = item['values'][3]  # cpf
        revisao_status = item['values'][4]  # status
        revisao_custo = item['values'][5]  # custo

        # Criar uma nova janela para editar o funcionário
        editar_popup = tk.Toplevel(self.root)
        editar_popup.title("Editar Funcionário")

        # Criar campos de entrada para editar os dados
        label_id = ttk.Label(editar_popup, text="ID:")
        label_id.grid(row=0, column=0, padx=5, pady=5)
        entry_id = ttk.Entry(editar_popup)
        entry_id.insert(0, revisao_id)  #
        entry_id.config(state='readonly')  # Não permitir editar
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        label_chassi = ttk.Label(editar_popup, text="Chassi:")
        label_chassi.grid(row=1, column=0, padx=5, pady=5)
        entry_chassi = ttk.Entry(editar_popup)
        entry_chassi.insert(0, revisao_chassi)
        entry_chassi.config(state='readonly')  # Não permitir editar   
        entry_chassi.grid(row=1, column=1, padx=5, pady=5)

        label_data = ttk.Label(editar_popup, text="Data:")
        label_data.grid(row=2, column=0, padx=5, pady=5)
        entry_data = ttk.Entry(editar_popup)
        entry_data.insert(0, revisao_data)  
        entry_data.config(state='readonly')  # Não permitir editar 
        entry_data.grid(row=2, column=1, padx=5, pady=5)

        label_cpf = ttk.Label(editar_popup, text="CPF:")
        label_cpf.grid(row=3, column=0, padx=5, pady=5)
        entry_cpf = ttk.Entry(editar_popup)
        entry_cpf.insert(0, revisao_cpf)  
        entry_cpf.config(state='readonly')  # Não permitir editar 
        entry_cpf.grid(row=3, column=1, padx=5, pady=5)

        label_status = ttk.Label(editar_popup, text="Status:")
        label_status.grid(row=4, column=0, padx=5, pady=5)
        entry_status = ttk.Entry(editar_popup)
        entry_status.insert(0, revisao_status)  
        entry_status.grid(row=4, column=1, padx=5, pady=5)

        label_custo = ttk.Label(editar_popup, text="Custo:")
        label_custo.grid(row=5, column=0, padx=5, pady=5)
        entry_custo = ttk.Entry(editar_popup)
        entry_custo.insert(0, revisao_custo)  
        entry_custo.grid(row=5, column=1, padx=5, pady=5)

        # Botão para salvar as alterações
        def salvar_edicao():
            novo_status = entry_status.get()
            novo_custo = entry_custo.get()

            # Criar um objeto Funcionario com os dados atualizados
            revisao_atualizada = Revisao(data=revisao_data,custo=novo_custo,status_revisao=novo_status,chassi_moto=revisao_chassi,cpf_cliente=revisao_cpf)

            # Chamar o método para atualizar o funcionário no banco de dados
            self.agenda_revisao_dao.atualizar_revisao(revisao_atualizada)

            # Fechar a janela popup
            editar_popup.destroy()

            # Atualizar a lista de funcionários no Treeview
            self.listar_revisoes()

        btn_salvar = ttk.Button(editar_popup, text="Salvar", style="Custom.TButton", command=salvar_edicao)
        btn_salvar.grid(row=6, column=0, columnspan=2, pady=10)

        # Tornar a janela modal
        editar_popup.transient(self.root)
        editar_popup.grab_set()
        self.root.wait_window(editar_popup)
    
    def deletar_revisao(self):
        selected_item = self.tree_revisao.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione um funcionário para deletar.")
            return

        item = self.tree_revisao.item(selected_item)
        revisao_id = item['values'][0]

        try:
            self.agenda_revisao_dao.deletar_revisao(revisao_id)
            messagebox.showinfo("Sucesso", "Funcionário deletado com sucesso!")
            self.listar_revisoes()  # Atualizar a lista
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar funcionário: {e}")

    def listar_revisoes(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree_revisao.get_children():
            self.tree_revisao.delete(i)

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

                self.tree_revisao.insert('', tk.END, values=(id_manutencao, chassi_moto, data, cpf, custo,status_revisao))

        else:
            messagebox.showinfo("Informação", "Nenhum funcionário encontrado.")

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
