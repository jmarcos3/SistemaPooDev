import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend.Routes import AgendaRevisaoDAO,Revisao,ClienteDAO,Cliente,FuncionarioDAO,Funcionario,MotoDAO,Moto,VendaDAO,Venda
import datetime  # Para obter a data atual automaticamente

class VendedorApp:
    def __init__(self, root):
      self.root = root
      self.root.title("Sistema de Controle de Motos")
      #self.root.geometry("600x800")  # Ajuste o tamanho da janela conforme necessário

        # Inicializando DAOs
      self.moto_dao = MotoDAO('db.db')  # Altere o nome do banco conforme necessário
      self.cliente_dao = ClienteDAO('db.db')
      self.venda_dao = VendaDAO('db.db')

      # Criando o notebook (abas)
      self.notebook = ttk.Notebook(self.root)
      self.notebook.pack(pady=10, expand=True)

      # Estilos personalizados
      estilo_label = {"font": ("Arial", 14, "bold"), "foreground": "#333"}
      estilo_entrada = {"width": 25, "font": ("Arial", 12)}

      style = ttk.Style()
      style.configure("Custom.TButton", font=("Arial", 14))

# ////////////////////////////////////////////////////////////////////////////
      # Aba de Clientes
      self.tab_cliente = ttk.Frame(self.notebook, padding=15)
      self.notebook.add(self.tab_cliente, text="Clientes")


      # Seção para adicionar cliente
      label_adicionar_cliente = ttk.Label(self.tab_cliente, text="Adicionar Cliente", **estilo_label)
      label_adicionar_cliente.grid(row=0, column=0, columnspan=2, pady=(0, 15))

      label_nome = ttk.Label(self.tab_cliente, text="Nome:", **estilo_label)
      label_nome.grid(row=1, column=0, padx=5, pady=5, sticky="e")
      self.entry_nome = ttk.Entry(self.tab_cliente, **estilo_entrada)
      self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

      label_cpf = ttk.Label(self.tab_cliente, text="CPF:", **estilo_label)
      label_cpf.grid(row=2, column=0, padx=5, pady=5, sticky="e")
      self.entry_cpf = ttk.Entry(self.tab_cliente, **estilo_entrada)
      self.entry_cpf.grid(row=2, column=1, padx=5, pady=5)

      label_email = ttk.Label(self.tab_cliente, text="Email:", **estilo_label)
      label_email.grid(row=3, column=0, padx=5, pady=5, sticky="e")
      self.entry_email = ttk.Entry(self.tab_cliente, **estilo_entrada)
      self.entry_email.grid(row=3, column=1, padx=5, pady=5)

      btn_adicionar_cliente = ttk.Button(self.tab_cliente, text="Adicionar", style="Custom.TButton", command=self.adicionar_cliente)
      btn_adicionar_cliente.grid(row=4, column=1, pady=10, sticky="n")

      # Seção para atualizar cliente
      label_atualizar_cliente = ttk.Label(self.tab_cliente, text="Atualizar Cliente", **estilo_label)
      label_atualizar_cliente.grid(row=8, column=0, columnspan=2, pady=(15, 5))

      label_atualizar_cpf = ttk.Label(self.tab_cliente, text="CPF do Cliente:", **estilo_label)
      label_atualizar_cpf.grid(row=9, column=0, padx=5, pady=5, sticky="e")
      self.entry_atualizar_cpf = ttk.Entry(self.tab_cliente, **estilo_entrada)
      self.entry_atualizar_cpf.grid(row=9, column=1, padx=5, pady=5)

      label_campo_atualizar = ttk.Label(self.tab_cliente, text="Campo a Atualizar:", **estilo_label)
      label_campo_atualizar.grid(row=10, column=0, padx=5, pady=5, sticky="e")
      self.entry_campo_atualizar = ttk.Entry(self.tab_cliente, **estilo_entrada)
      self.entry_campo_atualizar.grid(row=10, column=1, padx=5, pady=5)

      label_novo_valor = ttk.Label(self.tab_cliente, text="Novo Valor:", **estilo_label)
      label_novo_valor.grid(row=11, column=0, padx=5, pady=5, sticky="e")
      self.entry_novo_valor = ttk.Entry(self.tab_cliente, **estilo_entrada)
      self.entry_novo_valor.grid(row=11, column=1, padx=5, pady=5)

      btn_atualizar_cliente = ttk.Button(self.tab_cliente, text="Atualizar", style="Custom.TButton", command=self.atualizar_cliente)
      btn_atualizar_cliente.grid(row=12, column=1, pady=10, sticky="n")

      # Seção para listar clientes
      label_listar_clientes = ttk.Label(self.tab_cliente, text="Listar Clientes:", **estilo_label)
      label_listar_clientes.grid(row=14, column=0, pady=5)

      btn_listar_clientes = ttk.Button(self.tab_cliente, text="Listar Clientes", style="Custom.TButton", command=self.listar_clientes_popup)
      btn_listar_clientes.grid(row=14, column=1, pady=5, sticky="n")


# ////////////////////////////////////////////////////////////////////////////
      # Aba de Vendas
      self.tab_venda = ttk.Frame(self.notebook, padding=15)
      self.notebook.add(self.tab_venda, text="Vendas")

      # Seção para gerar venda
      label_gerar_venda = ttk.Label(self.tab_venda, text="Gerar Venda", **estilo_label)
      label_gerar_venda.grid(row=0, column=0, columnspan=2, pady=(0, 15))

      label_cpf_cliente = ttk.Label(self.tab_venda, text="Cliente:", **estilo_label)
      label_cpf_cliente.grid(row=1, column=0, padx=5, pady=5, sticky="e")
      self.entry_cpf_cliente = ttk.Entry(self.tab_venda, **estilo_entrada)
      self.entry_cpf_cliente.grid(row=1, column=1, padx=5, pady=5)

      label_chassi_moto = ttk.Label(self.tab_venda, text="Chassi:", **estilo_label)
      label_chassi_moto.grid(row=2, column=0, padx=5, pady=5, sticky="e")
      self.entry_chassi_moto = ttk.Entry(self.tab_venda, **estilo_entrada)
      self.entry_chassi_moto.grid(row=2, column=1, padx=5, pady=5)

      btn_gerar_venda = ttk.Button(self.tab_venda, text="Gerar Venda", style="Custom.TButton", command=self.adicionar_venda)
      btn_gerar_venda.grid(row=3, column=1, pady=10, sticky="n")

      # Label para a seção de listar vendas
      label_listar_vendas = ttk.Label(self.tab_venda, text="Listar Vendas: ", **estilo_label)
      label_listar_vendas.grid(row=14, column=0, pady=(5))

      # Botão para listar vendas e abrir um pop-up
      btn_listar_vendas = ttk.Button(self.tab_venda, text="Listar Vendas", style="Custom.TButton", command=self.listar_vendas_popup)
      btn_listar_vendas.grid(row=14, column=1, pady=10, sticky="n")

      label_listar_motos = ttk.Label(self.tab_venda, text="Listar Motos:", **estilo_label)
      label_listar_motos.grid(row=16, column=0, pady=5)
            
      # Botão para listar motos
      btn_listar_motos = ttk.Button(self.tab_venda, text="Listar Motos", style="Custom.TButton", command=self.listar_motos_popup)
      btn_listar_motos.grid(row=16, column=1, pady=10, sticky="s")

# ////////////////////////////////////////////////////////////////////////////

    # Métodos CRUD para clientes
    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()

        cliente = Cliente(nome=nome, cpf=cpf, email=email)
        self.cliente_dao.adicionar_cliente(cliente)
        print("Cliente adicionado com sucesso!")

    def remover_cliente(self):
        cpf = self.entry_remover_cpf.get()
        self.cliente_dao.remover_cliente(cpf)
        print("Cliente removido com sucesso!")

    def atualizar_cliente(self):
        cpf = self.entry_atualizar_cpf.get()  # CPF do cliente a ser atualizado
        campo = self.entry_campo_atualizar.get().lower()  # Campo a ser atualizado (nome ou email)
        novo_valor = self.entry_novo_valor.get()  # Novo valor para o campo

        if campo == "nome":  # Verifica qual campo será atualizado
            cliente = Cliente(cpf=cpf, nome=novo_valor, email=None)  # Cria cliente com o novo nome
            self.cliente_dao.atualizar_cliente(cliente)
        elif campo == "email":
            cliente = Cliente(cpf=cpf, nome=None, email=novo_valor)  # Cria cliente com o novo email
            self.cliente_dao.atualizar_cliente(cliente)
        else:
            print("Campo inválido. Só é possível atualizar 'nome' ou 'email'.")
            return
        
        print("Cliente atualizado com sucesso!")

    def listar_clientes_popup(self):
        # Criar uma nova janela (pop-up) referenciando a janela principal
        popup = tk.Toplevel(self.root)  # Use self.root se o root for a janela principal (tk.Tk)
        popup.title("Lista de Clientes")

        # Definir o tamanho da nova janela
        popup.geometry("600x300")

        # Criar um Treeview para exibir os clientes como uma tabela
        colunas = ('CPF', 'Nome', 'Email')
        tree = ttk.Treeview(popup, columns=colunas, show='headings')
        
        # Definir os títulos das colunas
        tree.heading('CPF', text='CPF')
        tree.heading('Nome', text='Nome')
        tree.heading('Email', text='Email')

        # Ajustar o tamanho das colunas
        tree.column('CPF', width=150)
        tree.column('Nome', width=200)
        tree.column('Email', width=250)

        # Inserir os dados dos clientes no Treeview
        clientes = self.cliente_dao.listar_clientes()
        
        if clientes:
            for cliente in clientes:
                cpf = cliente[0]  # Primeiro campo (CPF)
                nome = cliente[1]  # Segundo campo (Nome)
                email = cliente[2]  # Terceiro campo (Email)
                tree.insert('', tk.END, values=(cpf, nome, email))  # Inserir na tabela
        else:
            # Caso não haja clientes, mostrar uma linha indicando isso
            tree.insert('', tk.END, values=('Nenhum cliente encontrado', '', ''))

        # Posicionar o Treeview na janela pop-up
        tree.pack(padx=10, pady=10, expand=True, fill='both')

        # Adicionar um botão para fechar o pop-up
        btn_fechar = ttk.Button(popup, text="Fechar", command=popup.destroy)
        btn_fechar.pack(pady=10)

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
        btn_fechar = ttk.Button(popup, text="Fechar", command=popup.destroy)
        btn_fechar.pack(pady=10)

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
        btn_fechar = ttk.Button(popup, text="Fechar", command=popup.destroy)
        btn_fechar.pack(pady=10)
