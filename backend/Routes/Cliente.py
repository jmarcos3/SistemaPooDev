import sqlite3

# Classe que representa um cliente
class Cliente:
    def __init__(self, cpf, nome, email):
        self.cpf = cpf
        self.nome = nome
        self.email = email

# Data Access Object (DAO) para a tabela de Clientes
class ClienteDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def adicionar_cliente(self, cliente):
        self.cursor.execute('''
            INSERT INTO Clientes (cpf, nome, email) 
            VALUES (?, ?, ?)
        ''', (cliente.cpf, cliente.nome, cliente.email))
        self.conn.commit()
        print("Cliente adicionado com sucesso!")

    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM Clientes')
        clientes = self.cursor.fetchall()
        return clientes

    def buscar_cliente(self, cpf):
        self.cursor.execute('SELECT * FROM Clientes WHERE cpf = ?', (cpf,))
        cliente = self.cursor.fetchone()
        
        return cliente

    def atualizar_cliente(self, cliente):
        if cliente.nome:
            self.cursor.execute('UPDATE Clientes SET nome = ? WHERE cpf = ?', (cliente.nome, cliente.cpf))
        if cliente.email:
            self.cursor.execute('UPDATE Clientes SET email = ? WHERE cpf = ?', (cliente.email, cliente.cpf))
        self.conn.commit()
        print("Cliente atualizado com sucesso!")

    def deletar_cliente(self, cpf):
        self.cursor.execute('DELETE FROM Clientes WHERE cpf = ?', (cpf,))
        self.conn.commit()
        print("Cliente deletado com sucesso!")

    def fechar_conexao(self):
        self.conn.close()

