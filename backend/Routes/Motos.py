import sqlite3

# Classe Moto que define o objeto Moto
class Moto:
    def __init__(self, chassi, ano, preco, cor, modelo):
        self.chassi = chassi
        self.ano = ano
        self.preco = preco
        self.cor = cor
        self.modelo = modelo

# Classe MotoDAO para acessar os dados da tabela Motos
class MotoDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        # Conecta ao banco de dados
        return sqlite3.connect(self.db_path)

    def adicionar_moto(self, moto):
        # Adiciona uma nova moto à tabela Motos
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Motos (chassi, ano, preco, cor, modelo) 
            VALUES (?, ?, ?, ?, ?)
        ''', (moto.chassi, moto.ano, moto.preco, moto.cor, moto.modelo))
        conn.commit()
        conn.close()
        print("Moto adicionada com sucesso!")

    def listar_motos(self):
        # Lista todas as motos cadastradas
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Motos')
        motos = cursor.fetchall()
        conn.close()
        return motos

    def buscar_moto(self, chassi):
        # Busca uma moto pelo chassi
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Motos WHERE chassi = ?', (chassi,))
        moto = cursor.fetchone()
        conn.close()
        return moto

    def atualizar_moto(self, chassi, ano=None, preco=None, cor=None, modelo=None):
        # Atualiza os dados de uma moto específica
        conn = self.conectar()
        cursor = conn.cursor()
        
        # Atualiza os dados conforme os parâmetros fornecidos
        if ano:
            cursor.execute('UPDATE Motos SET ano = ? WHERE chassi = ?', (ano, chassi))
        if preco:
            cursor.execute('UPDATE Motos SET preco = ? WHERE chassi = ?', (preco, chassi))
        if cor:
            cursor.execute('UPDATE Motos SET cor = ? WHERE chassi = ?', (cor, chassi))
        if modelo:
            cursor.execute('UPDATE Motos SET modelo = ? WHERE chassi = ?', (modelo, chassi))
        
        conn.commit()
        conn.close()
        print("Moto atualizada com sucesso!")

    def deletar_moto(self, chassi):
        # Remove uma moto da tabela pelo chassi
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Motos WHERE chassi = ?', (chassi,))
        conn.commit()
        conn.close()
        print("Moto deletada com sucesso!")


# Testando o CRUD para motos
if __name__ == "__main__":
    moto_dao = MotoDAO('db.db')

    # Criar algumas motos
    moto1 = Moto("ABC123456789", 2021, 20000.0, "Vermelha", "Honda CG 160")
    moto2 = Moto("DEF987654321", 2022, 25000.0, "Preta", "Yamaha Fazer 250")
    
    # Adicionar motos ao banco de dados
    moto_dao.adicionar_moto(moto1)
    moto_dao.adicionar_moto(moto2)

    # Listar todas as motos
    print("Lista de Motos:")
    for moto in moto_dao.listar_motos():
        print(moto)

    # Buscar uma moto específica
    print("\nBuscando Moto com chassi ABC123456789:")
    print(moto_dao.buscar_moto("ABC123456789"))

    # Atualizar uma moto
    print("\nAtualizando o preço da moto com chassi ABC123456789...")
    moto_dao.atualizar_moto("ABC123456789", preco=21000.0)

    # Listar todas as motos após atualização
    print("\nLista de Motos após atualização:")
    for moto in moto_dao.listar_motos():
        print(moto)

    # Deletar uma moto
    print("\nDeletando a moto com chassi DEF987654321...")
    moto_dao.deletar_moto("DEF987654321")

    # Listar todas as motos após exclusão
    print("\nLista de Motos após exclusão:")
    for moto in moto_dao.listar_motos():
        print(moto)
