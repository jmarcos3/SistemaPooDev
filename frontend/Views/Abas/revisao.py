from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ..estilos import estilos
from backend.Routes import Revisao,AgendaRevisaoDAO,VendaDAO,ClienteDAO
import datetime

class AbaAgenda(estilos):
    def __init__(self, root,notebook, cargo):
        super().__init__()

        self.agenda_revisao_dao = AgendaRevisaoDAO('db.db')
        self.vendas_dao = VendaDAO('db.db')
        self.cliente_dao = ClienteDAO('db.db')

        if cargo == "gerente" or cargo =="secretaria":
            valor = 4
        else:
            valor = 1

    # aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(notebook, padding=10)  # Reduzindo o padding
        notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_agenda.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_agenda.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_agenda.rowconfigure(row, weight=1)

        if cargo == "gerente" or cargo =="secretaria":
            # Seção para agendar revisão
            label_agendar_revisao = ttk.Label(self.tab_agenda, text="Agendar Revisão", **self.estilo_label)
            label_agendar_revisao.grid(row=0, column=0, columnspan=2, pady=(5, 10))  # Ajustando o padding

            label_chassi_moto_revisao = ttk.Label(self.tab_agenda, text="Chassi:", **self.estilo_label)
            label_chassi_moto_revisao.grid(row=1, column=0, padx=5, pady=5, sticky="e")
            self.entry_chassi_moto_revisao = ttk.Entry(self.tab_agenda, **self.estilo_entrada)
            self.entry_chassi_moto_revisao.grid(row=1, column=1, padx=5, pady=5, sticky="w")

            label_cpf_cliente_revisao = ttk.Label(self.tab_agenda, text="CPF do Cliente:", **self.estilo_label)
            label_cpf_cliente_revisao.grid(row=2, column=0, padx=5, pady=5, sticky="e")  # Corrigido o row
            self.entry_cpf_cliente_revisao = ttk.Entry(self.tab_agenda, **self.estilo_entrada)
            self.entry_cpf_cliente_revisao.grid(row=2, column=1, padx=5, pady=5, sticky="w")

            btn_agendar_revisao = ttk.Button(self.tab_agenda, text="Agendar Revisão", style="Custom.TButton", command=self.agendar_revisao)
            btn_agendar_revisao.grid(row=3, column=1, pady=5, sticky="w")  # Ajustando o padding
        else:
            pass

        # Seção para listar
        label_listar_revisoes = ttk.Label(self.tab_agenda, text="Revisões Agendadas", **self.estilo_label)
        label_listar_revisoes.grid(row=valor, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar
        colunas = ('ID', 'Chassi', 'Data', 'CPF', 'Status', 'Custo')
        self.tree_revisao = ttk.Treeview(self.tab_agenda, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_revisao.heading('ID', text='ID Manutenção')
        self.tree_revisao.heading('Chassi', text='Chassi')
        self.tree_revisao.heading('Data', text='Data')
        self.tree_revisao.heading('CPF', text='CPF Cliente')
        self.tree_revisao.heading('Status', text='Status')
        self.tree_revisao.heading('Custo', text='Custo')

        # Ajustar o tamanho das colunas
        self.tree_revisao.column('ID', width=150)
        self.tree_revisao.column('Chassi', width=100)
        self.tree_revisao.column('Data', width=100)
        self.tree_revisao.column('CPF', width=100)
        self.tree_revisao.column('Status', width=100)
        self.tree_revisao.column('Custo', width=100)

        # Posicionar o Treeview
        self.tree_revisao.grid(row=(valor+1), column=0, columnspan=2, padx=10, pady=5, sticky='nsew')  # Ajustando o padding

        if cargo == "gerente" or cargo == "mecanico":
            # Botões para editar e deletar revisão
            btn_editar_revisao = ttk.Button(self.tab_agenda, text="Editar Revisão", style="Custom.TButton", command=self.editar_revisao)
            btn_editar_revisao.grid(row=6, column=0, pady=5, sticky="n")
        else:
            pass

        if cargo != "gerente":
            pass
        else:
            btn_deletar_revisao = ttk.Button(self.tab_agenda, text="Deletar Revisão", style="Custom.TButton", command=self.deletar_revisao)
            btn_deletar_revisao.grid(row=6, column=1, pady=5, sticky="n")  # Ajustando o padding

        # Botão de deslogar na parte superior direita, ao lado de "Adicionar Moto"
        btn_sair = ttk.Button(self.tab_agenda, text="Sair", style="Custom.TButton", command=self.sair)
        btn_sair.grid(row=6, column=1, padx=0, pady=0, sticky="e")

        self.listar_revisoes()    

##############################################################
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
            item = self.vendas_dao.buscar_motoVendida(chassi_moto)
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
                self.entry_chassi_moto_revisao.delete(0, tk.END)
                self.entry_cpf_cliente_revisao.delete(0, tk.END)

                self.listar_revisoes()
                
            else: 
                raise Exception      
        except Exception as e:
            messagebox.showerror("Erro", f"Digite um cpf válido")
        
        # Limpar campos após agendar
        self.entry_chassi_moto_revisao.delete(0, tk.END)
        self.entry_cpf_cliente_revisao.delete(0, tk.END)

    def editar_revisao(self):
        # Obter o funcionário selecionado
        selected_item = self.tree_revisao.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Selecione uma revisão para editar.")
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

            messagebox.showinfo("Sucesso", "Revisão atualizada com sucesso!")

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
            messagebox.showerror("Erro", "Selecione uma revisão para deletar.")
            return

        item = self.tree_revisao.item(selected_item)
        revisao_id = item['values'][0]

        try:
            self.agenda_revisao_dao.deletar_revisao(revisao_id)
            messagebox.showinfo("Sucesso", "Revisão deletada com sucesso!")
            self.listar_revisoes()  # Atualizar a lista
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar revisão: {e}")

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
            messagebox.showinfo("Informação", "Nenhuma revisão encontrada.")

