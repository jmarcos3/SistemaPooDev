import sqlite3

# Classe que representa um funcionário
class Funcionario:
    def __init__(self, cpf, nome, usuario, senha, funcao):
        self.cpf = cpf
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.funcao = funcao

# Data Access Object (DAO) para a tabela de Funcionarios
class FuncionarioDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def adicionar_funcionario(self, funcionario):
        self.cursor.execute('''
            INSERT INTO Funcionarios (cpf, nome, usuario, senha, funcao) 
            VALUES (?, ?, ?, ?, ?)
        ''', (funcionario.cpf, funcionario.nome, funcionario.usuario, funcionario.senha, funcionario.funcao))
        self.conn.commit()
        print("Funcionário adicionado com sucesso!")

    def listar_funcionarios(self):
        self.cursor.execute('SELECT * FROM Funcionarios')
        funcionarios = self.cursor.fetchall()
        return funcionarios

    def buscar_funcionario(self, cpf):
        self.cursor.execute('SELECT * FROM Funcionarios WHERE cpf = ?', (cpf,))
        funcionario = self.cursor.fetchone()
        return funcionario

    def atualizar_funcionario(self, funcionario):
        if funcionario.nome:
            self.cursor.execute('UPDATE Funcionarios SET nome = ? WHERE cpf = ?', (funcionario.nome, funcionario.cpf))
        if funcionario.usuario:
            self.cursor.execute('UPDATE Funcionarios SET usuario = ? WHERE cpf = ?', (funcionario.usuario, funcionario.cpf))
        if funcionario.senha:
            self.cursor.execute('UPDATE Funcionarios SET senha = ? WHERE cpf = ?', (funcionario.senha, funcionario.cpf))
        if funcionario.funcao:
            self.cursor.execute('UPDATE Funcionarios SET funcao = ? WHERE cpf = ?', (funcionario.funcao, funcionario.cpf))
        self.conn.commit()
        print("Funcionário atualizado com sucesso!")

    def deletar_funcionario(self, cpf):
        self.cursor.execute('DELETE FROM Funcionarios WHERE cpf = ?', (cpf,))
        self.conn.commit()
        print("Funcionário deletado com sucesso!")

    def fechar_conexao(self):
        self.conn.close()

# Testando o CRUD orientado a objetos
if __name__ == "__main__":
    funcionaro_dao = FuncionarioDAO('db.db')

    # Criando objetos de funcionários
    funcionario1 = Funcionario("12345678900", "João Silva", "joao123", "senha123", "vendedor")
    funcionario2 = Funcionario("98765432100", "Maria Oliveira", "maria456", "senha456", "gerente")

    # Adicionar funcionários ao banco de dados
    funcionaro_dao.adicionar_funcionario(funcionario1)
    funcionaro_dao.adicionar_funcionario(funcionario2)

    # Listar todos os funcionários
    print("Lista de Funcionários:")
    for funcionario in funcionaro_dao.listar_funcionarios():
        print(funcionario)

    # Buscar um funcionário pelo CPF
    print("\nBuscar Funcionário com CPF 12345678900:")
    print(funcionaro_dao.buscar_funcionario("12345678900"))

    # Atualizar o nome do funcionário
    print("\nAtualizando o nome do funcionário com CPF 12345678900 para 'João Pedro'...")
    funcionario1.nome = "João Pedro"
    funcionaro_dao.atualizar_funcionario(funcionario1)

    # Listar todos os funcionários após atualização
    print("\nLista de Funcionários após atualização:")
    for funcionario in funcionaro_dao.listar_funcionarios():
        print(funcionario)

    # Deletar um funcionário
    print("\nDeletando o funcionário com CPF 98765432100...")
    funcionaro_dao.deletar_funcionario("98765432100")

    # Listar todos os funcionários após exclusão
    print("\nLista de Funcionários após exclusão:")
    for funcionario in funcionaro_dao.listar_funcionarios():
        print(funcionario)

    # Fechar a conexão com o banco de dados
    funcionaro_dao.fechar_conexao()
