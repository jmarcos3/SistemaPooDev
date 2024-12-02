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
    
    def buscar_preco(self, chassi):
        # Busca uma moto pelo chassi
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT preco FROM Motos WHERE chassi = ?', (chassi,))
        preco = cursor.fetchone()
        conn.close()
        return preco    

    def atualizar_moto(self, moto):
        # Atualiza os dados de uma moto específica
        conn = self.conectar()
        cursor = conn.cursor()
        
        # Atualiza os dados conforme os parâmetros fornecidos
        if moto.ano:
            cursor.execute('UPDATE Motos SET ano = ? WHERE chassi = ?', (moto.ano, moto.chassi))
        if moto.preco:
            cursor.execute('UPDATE Motos SET preco = ? WHERE chassi = ?', (moto.preco, moto.chassi))
        if moto.cor:
            cursor.execute('UPDATE Motos SET cor = ? WHERE chassi = ?', (moto.cor, moto.chassi))
        if moto.modelo:
            cursor.execute('UPDATE Motos SET modelo = ? WHERE chassi = ?', (moto.modelo, moto.chassi))
        
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
