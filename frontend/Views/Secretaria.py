import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,Revisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

class SecretariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        # Inicializando DAOs
        self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
        self.venda_dao = VendaDAO('db.db')
        self.agenda_revisao_dao = AgendaRevisaoDAO('db.db')

        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Estilos personalizados
        estilo_label = {"font": ("Arial", 14, "bold"), "foreground": "#333"}
        estilo_entrada = {"width": 25, "font": ("Arial", 12)}

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14))

        # ////////////////////////////////////////////////////////////////////////////

        # Aba de Motos
        self.tab_motos = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_motos, text="Motos")

        # Seção para listar motos
        label_listar_motos = ttk.Label(self.tab_motos, text="Listar Motos:", **estilo_label)
        label_listar_motos.grid(row=15, column=0, pady=5)

        # Botão para listar motos
        btn_listar_motos = ttk.Button(self.tab_motos, text="Listar Motos", style="Custom.TButton", command=self.listar_motos_popup)
        btn_listar_motos.grid(row=15, column=1, pady=10, sticky="s")

        # ////////////////////////////////////////////////////////////////////////////

        # Aba de Vendas
        self.tab_venda = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_venda, text="Vendas")

        # Label para a seção de listar vendas
        label_listar_vendas = ttk.Label(self.tab_venda, text="Listar Vendas: ", **estilo_label)
        label_listar_vendas.grid(row=14, column=0, pady=(5))

        # Botão para listar vendas e abrir um pop-up
        btn_listar_vendas = ttk.Button(self.tab_venda, text="Listar Vendas", style="Custom.TButton", command=self.listar_vendas_popup)
        btn_listar_vendas.grid(row=14, column=1, pady=10, sticky="n")

        # ////////////////////////////////////////////////////////////////////////////

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

        # ////////////////////////////////////////////////////////////////////////////

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

        # ////////////////////////////////////////////////////////////////////////////

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

        # ////////////////////////////////////////////////////////////////////////////
        
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