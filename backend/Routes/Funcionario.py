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
    
    def buscar_funcao(self, username,password):
        self.cursor.execute('SELECT funcao FROM Funcionarios WHERE usuario = ? AND senha = ?', (username, password))
        funcionario = self.cursor.fetchone()
        return funcionario[0] if funcionario else None

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

# Adicionando Funcionarios para conseguir passar da tela de login
if __name__ == "__main__":
    funcionaro_dao = FuncionarioDAO('db.db')

    # Criando objetos de funcionários
    funcionario1 = Funcionario("12345678900", "João Silva", "1", "1", "Gerente")
    funcionario2 = Funcionario("98765432100", "Maria Oliveira", "2", "2", "Gerente")

    # Adicionar funcionários ao banco de dados
    funcionaro_dao.adicionar_funcionario(funcionario1)
    funcionaro_dao.adicionar_funcionario(funcionario2)

    # Fechar a conexão com o banco de dados
    funcionaro_dao.fechar_conexao()
