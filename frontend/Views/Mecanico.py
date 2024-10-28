import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,Revisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

class MecanicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        #self.root.geometry("600x800")  # Ajuste o tamanho da janela conforme necessário

        # Inicializando DAOs
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

        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Seção para listar revisões agendadas
        label_listar_revisoes = ttk.Label(self.tab_agenda, text="Mostrar Agenda:", **estilo_label)
        label_listar_revisoes.grid(row=5, column=0, pady=(5))

        # Botão para listar revisões e abrir um pop-up
        btn_listar_revisoes = ttk.Button(self.tab_agenda, text="Listar Revisões", style="Custom.TButton", command=self.listar_revisoes_popup)
        btn_listar_revisoes.grid(row=5, column=1, pady=5, sticky="n")

    # ////////////////////////////////////////////////////////////////////////////

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
