from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from ..estilos import estilos
from backend.Routes import Moto,MotoDAO

class AbaMotos(estilos):
    def __init__(self,root,notebook,cargo):
        super().__init__()

        self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
        
        if cargo == "gerente":
            valor = 7
        else:
            valor = 1

       # Aba de Motos"
        self.tab_motos = ttk.Frame(notebook, padding=15)
        notebook.add(self.tab_motos, text="Motos")

        # Configurando pesos das colunas e linhas para centralização
        self.tab_motos.columnconfigure(0, weight=1)  # Coluna da esquerda
        self.tab_motos.columnconfigure(1, weight=1)  # Coluna da direita
        for row in range(7):  # Para cada linha usada
            self.tab_motos.rowconfigure(row, weight=1)   
        
        if cargo != "gerente":
            pass
        else:
            # Seção para adicionar moto
            label_adicionar_moto = ttk.Label(self.tab_motos, text="Adicionar Moto", **self.estilo_label)
            label_adicionar_moto.grid(row=0, column=0, columnspan=2, pady=(5, 15))

            label_modelo = ttk.Label(self.tab_motos, text="Modelo:", **self.estilo_label)
            label_modelo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
            self.entry_modelo = ttk.Entry(self.tab_motos, **self.estilo_entrada)
            self.entry_modelo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

            label_ano = ttk.Label(self.tab_motos, text="Ano:", **self.estilo_label)
            label_ano.grid(row=2, column=0, padx=5, pady=5, sticky="e")
            self.entry_ano = ttk.Entry(self.tab_motos, **self.estilo_entrada)
            self.entry_ano.grid(row=2, column=1, padx=5, pady=5, sticky="w")

            label_preco = ttk.Label(self.tab_motos, text="Preço:", **self.estilo_label)
            label_preco.grid(row=3, column=0, padx=5, pady=5, sticky="e")
            self.entry_preco = ttk.Entry(self.tab_motos, **self.estilo_entrada)
            self.entry_preco.grid(row=3, column=1, padx=5, pady=5, sticky="w")

            # Substituindo o campo de entrada de cor por um Combobox
            label_cor = ttk.Label(self.tab_motos, text="Cor:", **self.estilo_label)
            label_cor.grid(row=4, column=0, padx=5, pady=5, sticky="e")

            # Combobox para seleção de cor
            cores_disponiveis = ["Amarelo", "Azul", "Bege", "Branca", "Cinza", "Dourada", "Grená", 
            "Laranja", "Marrom", "Prata", "Preta", "Rosa", "Roxa", "Verde", "Vermelha", "Fantasia"]

            self.combo_cor = ttk.Combobox(self.tab_motos, values=cores_disponiveis, state="readonly", **self.estilo_entrada)
            self.combo_cor.grid(row=4, column=1, padx=5, pady=5, sticky="w")
            self.combo_cor.set("Selecione a cor")  # Placeholder inicial

            label_chassi = ttk.Label(self.tab_motos, text="Chassi:", **self.estilo_label)
            label_chassi.grid(row=5, column=0, padx=5, pady=5, sticky="e")
            self.entry_chassi = ttk.Entry(self.tab_motos, **self.estilo_entrada)
            self.entry_chassi.grid(row=5, column=1, padx=5, pady=5, sticky="w")

            btn_adicionar_moto = ttk.Button(self.tab_motos, text="Adicionar moto", style="Custom.TButton", command=self.adicionar_moto)
            btn_adicionar_moto.grid(row=6, column=1, pady=10, sticky="w")

        # Seção para listar 
        label_listar_motos = ttk.Label(self.tab_motos, text="Motos Cadastradas", **self.estilo_label)
        label_listar_motos.grid(row=valor, column=0, pady=(5), columnspan=2)

        # Criando o Treeview para listar 
        colunas = ('Chassi', 'Ano', 'Preço', 'Cor','Modelo')
        self.tree_moto = ttk.Treeview(self.tab_motos, columns=colunas, show='headings')

        # Definindo os títulos das colunas
        self.tree_moto.heading('Chassi', text='Chassi')
        self.tree_moto.heading('Ano', text='Ano')
        self.tree_moto.heading('Preço', text='Preço')
        self.tree_moto.heading('Cor', text='Cor')
        self.tree_moto.heading('Modelo', text='Modelo')

        # Ajustar o tamanho das colunas
        self.tree_moto.column('Chassi', width=150)
        self.tree_moto.column('Ano', width=120)
        self.tree_moto.column('Preço', width=100)
        self.tree_moto.column('Cor', width=100)
        self.tree_moto.column('Modelo', width=100)

        # Posicionar o Treeview
        self.tree_moto.grid(row=(valor+1), column=0, columnspan=2, padx=10, pady=10, sticky='nsew')
        

        if cargo != "gerente":
            pass
        else:
            # Botões para editar e deletar motos
            btn_editar_moto = ttk.Button(self.tab_motos, text="Editar Moto", style="Custom.TButton", command=self.editar_moto)
            btn_editar_moto.grid(row=11, column=0, pady=10, sticky="n")

            btn_deletar_moto = ttk.Button(self.tab_motos, text="Deletar Moto", style="Custom.TButton", command=self.deletar_moto)
            btn_deletar_moto.grid(row=11, column=1, pady=10, sticky="n")
        
        # Botão de deslogar na parte superior direita, ao lado de "Adicionar Moto"
        btn_sair = ttk.Button(self.tab_motos, text="Sair", style="Custom.TButton", command=self.sair)
        btn_sair.grid(row=14, column=1, padx=0, pady=0, sticky="e")

        self.listar_motos()
        
###################################################################################

    # Métodos CRUD para motos
    def adicionar_moto(self):
        modelo = self.entry_modelo.get()
        ano = self.entry_ano.get()
        preco_str = self.entry_preco.get()  # Converter para float
        cor = self.combo_cor.get() # obtem valor do combobox
        chassi = self.entry_chassi.get()  # Chassi da moto

        if not modelo or not ano or not preco_str or not chassi:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        preco = float(preco_str)

        if cor == "Selecione a cor":
            messagebox.showerror("Erro", "Por favor, selecione uma cor válida.")
            return

        # Aqui você poderia adicionar uma lógica para mudar o status se for necessário
        moto = Moto(modelo=modelo, ano=ano, preco=preco, cor=cor, chassi=chassi)
        self.moto_dao.adicionar_moto(moto)

        messagebox.showinfo("Sucesso", "Moto adicionada com sucesso!")
        self.entry_modelo.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_chassi.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.combo_cor.set("Selecione a cor")
        self.combo_cor.configure(style="TCombobox")
        
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

        label_modelo = ttk.Label(editar_popup, text="Modelo:")
        label_modelo.grid(row=4, column=0, padx=5, pady=5)
        entry_modelo = ttk.Entry(editar_popup)
        entry_modelo.insert(0, moto_modelo)  # Preencher o cargo atual
        entry_modelo.grid(row=4, column=1, padx=5, pady=5)

        
        # Botão para salvar as alterações
        def salvar_edicao():
            novo_ano = entry_ano.get()
            novo_preço= entry_preço.get()
            nova_cor= entry_cor.get()
            novo_modelo= entry_modelo.get()

            # Criar um objeto Funcionario com os dados atualizados
            moto_atualizada = Moto(chassi=moto_chassi,ano=novo_ano,preco=novo_preço, cor=nova_cor, modelo=novo_modelo)

            # Chamar o método para atualizar o funcionário no banco de dados
            self.moto_dao.atualizar_moto(moto_atualizada)

            # Fechar a janela popup
            editar_popup.destroy()

            messagebox.showinfo("Sucesso", "Moto atualizada com sucesso!")
            
            # Atualizar a lista de funcionários no Treeview
            self.listar_motos()

        btn_salvar = ttk.Button(editar_popup, text="Salvar", style="Custom.TButton", command=salvar_edicao)
        btn_salvar.grid(row=5, column=0, columnspan=2, pady=10)

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

