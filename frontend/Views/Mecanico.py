import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
#from PIL import Image, ImageTk
from backend.Routes import AgendaRevisaoDAO, Revisao
import datetime  # Para obter a data atual automaticamente

class MecanicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Controle de Motos")
        self.root.state('zoomed')

        # Inicializando DAOs
        self.agenda_revisao_dao = AgendaRevisaoDAO('db.db')

        # Adicionando título
        self.title_label = tk.Label(
            root,
            text="Concessionária de motos",
            font=("Arial", 24, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=20
        )
        self.title_label.pack(fill="x")

        # Criando o notebook (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Estilos personalizados
        estilo_label = {"font": ("Arial", 16, "bold"), "foreground": "#333"}
        estilo_entrada = {"width": 25, "font": ("Arial", 14)}

        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 14, "bold"))
        style.theme_use("default")
        style.configure("TNotebook.Tab",
            font=("Arial", 13, "bold"),  # Defina o tamanho e estilo da fonte
            width=self.root.winfo_screenwidth() // len(["Agenda de Revisões"])
        )

        # Adicionando a aba de Agenda de Revisões
        self.tab_agenda = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.tab_agenda, text="Agenda de Revisões")

        # Configurando pesos para centralizar
        self.tab_agenda.columnconfigure(0, weight=1)
        self.tab_agenda.columnconfigure(1, weight=1)
        for i in range(8):  # Número de linhas usadas
            self.tab_agenda.rowconfigure(i, weight=1)

        # Seção para listar revisões
        label_listar_funcionarios = ttk.Label(self.tab_agenda, text="Revisões Agendadas", **estilo_label)
        label_listar_funcionarios.grid(row=0, column=0, columnspan=2, pady=(5, 15))

        #         # Adicionando foto do gerente com nome do cargo
        # # Carregar a imagem do gerente
        # self.img_mecanico = Image.open("mecanico.png")  # Substitua pelo caminho da imagem
        # self.img_mecanico = self.img_mecanico.resize((100, 100))  # Redimensiona a imagem para tamanho adequado
        # self.img_mecanico_tk = ImageTk.PhotoImage(self.img_mecanico)

        # # Exibindo a imagem do 
        # self.img_label = tk.Label(self.tab_agenda, image=self.img_mecanico_tk)
        # self.img_label.grid(row=1, column=0, padx=5, pady=10)

        # # Nome do cargo abaixo da imagem
        # label_cargo_mecanico = ttk.Label(self.tab_agenda, text="Mecanico", font=("Arial", 12, "bold"))
        # label_cargo_mecanico.grid(row=2, column=0, pady=5)


        # Criando o Treeview para listar
        colunas = ('ID', 'Chassi', 'Data', 'CPF', 'Status', 'Custo')
        self.tree = ttk.Treeview(self.tab_agenda, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree.heading('ID', text='ID Manutenção')
        self.tree.heading('Chassi', text='Chassi')
        self.tree.heading('Data', text='Data')
        self.tree.heading('CPF', text='CPF')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Custo', text='Custo')

        # Ajustar o tamanho das colunas dinamicamente
        for col in colunas:
            self.tree.column(col, anchor='center', width=150)

        # Posicionar o Treeview
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

        # Adicionando barra de rolagem vertical
        scrollbar_vertical = ttk.Scrollbar(self.tab_agenda, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar_vertical.set)
        scrollbar_vertical.grid(row=1, column=2, sticky="ns")

        # Adicionando barra de rolagem horizontal
        scrollbar_horizontal = ttk.Scrollbar(self.tab_agenda, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscroll=scrollbar_horizontal.set)
        scrollbar_horizontal.grid(row=2, column=0, columnspan=2, sticky="ew")

        # Atualiza as revisões na inicialização
        self.listar_revisoes()

    # ////////////////////////////////////////////////////////////////////////////

    def listar_revisoes(self):
        # Limpar o Treeview antes de listar os dados
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Buscar as revisões no banco de dados
        revisoes = self.agenda_revisao_dao.listar_revisoes()

        # Verifique se a lista de revisões não está vazia
        if revisoes:
            # Inserir cada revisão na Treeview
            for revisao in revisoes:
                # Aqui, estou assumindo que 'revisao' é uma tupla com a estrutura correta
                id_manutencao = revisao[0]  # ID da manutenção
                chassi_moto = revisao[4]    # Chassi da moto
                data = revisao[1]           # Data da revisão
                cpf = revisao[5]            # CPF do cliente ou mecânico (ajustar conforme sua lógica)
                custo = revisao[3]          # Custo da revisão
                status_revisao = revisao[2] # Status da revisão

                # Adiciona a revisão na Treeview
                self.tree.insert('', tk.END, values=(id_manutencao, chassi_moto, data, cpf, status_revisao, custo))

        else:
            messagebox.showinfo("Informação", "Nenhuma revisão agendada.")
