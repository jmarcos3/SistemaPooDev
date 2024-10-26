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

# Testando o CRUD orientado a objetos para Clientes
if __name__ == "__main__":
    cliente_dao = ClienteDAO('db.db')

    # Criando objetos de clientes
    cliente1 = Cliente("12345678900", "Ana Silva", "ana@exemplo.com")
    cliente2 = Cliente("98765432100", "Carlos Pereira", "carlos@exemplo.com")

    # Adicionar clientes ao banco de dados
    cliente_dao.adicionar_cliente(cliente1)
    cliente_dao.adicionar_cliente(cliente2)

    # Listar todos os clientes
    print("Lista de Clientes:")
    for cliente in cliente_dao.listar_clientes():
        print(cliente)

    # Buscar um cliente pelo CPF
    print("\nBuscar Cliente com CPF 12345678900:")
    print(cliente_dao.buscar_cliente("12345678900"))

    # Atualizar um cliente
    print("\nAtualizando o email do cliente com CPF 12345678900 para 'ana1@exemplo.com'...")
    cliente1.email = "ana1@exemplo.com"
    cliente_dao.atualizar_cliente(cliente1)

    # Listar todos os clientes após atualização
    print("\nLista de Clientes após atualização:")
    for cliente in cliente_dao.listar_clientes():
        print(cliente)

    # Deletar um cliente
    print("\nDeletando o cliente com CPF 98765432100...")
    cliente_dao.deletar_cliente("98765432100")

    # Listar todos os clientes após exclusão
    print("\nLista de Clientes após exclusão:")
    for cliente in cliente_dao.listar_clientes():
        print(cliente)

    # Fechar a conexão com o banco de dados
    cliente_dao.fechar_conexao()
