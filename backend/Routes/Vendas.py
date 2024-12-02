import sqlite3

# Classe Venda que define o objeto Venda
class Venda:
    def __init__(self, data, status, chassi_moto, cpf_cliente, preco):
        self.data = data
        self.status = status
        self.chassi_moto = chassi_moto
        self.cpf_cliente = cpf_cliente
        self.preco = preco  # Adicionando o atributo preço

# Classe VendaDAO para acessar os dados da tabela Vendas
class VendaDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        # Conecta ao banco de dados
        return sqlite3.connect(self.db_path)

    def adicionar_venda(self, venda):
        # Adiciona uma nova venda à tabela Vendas
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Vendas (data, status, chassi_moto, cpf_cliente, preco)
            VALUES (?, ?, ?, ?, ?)
        ''', (venda.data, venda.status, venda.chassi_moto, venda.cpf_cliente, venda.preco))  # Passando o preço
        conn.commit()
        conn.close()
        print("Venda adicionada com sucesso!")

    def listar_vendas(self):
        # Lista todas as vendas cadastradas
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vendas')
        vendas = cursor.fetchall()
        conn.close()
        return vendas

    def buscar_venda(self, id_compra):
        # Busca uma venda pelo ID da compra
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vendas WHERE id_compra = ?', (id_compra,))
        venda = cursor.fetchone()
        conn.close()
        return venda
    
    def buscar_motoVendida(self, chassi,cpf):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Vendas WHERE chassi_moto = ? and cpf_cliente = ?', (chassi,cpf))
        moto = cursor.fetchone()
        conn.close()
        return moto

    def atualizar_venda(self, venda,id_compra):
        # Atualiza os dados de uma venda específica
        conn = self.conectar()
        cursor = conn.cursor()
        
        # Atualiza os dados conforme os parâmetros fornecidos
        if venda.data:
            cursor.execute('UPDATE Vendas SET data = ? WHERE id_compra = ?', (venda.data, id_compra))
        if venda.status:
            cursor.execute('UPDATE Vendas SET status = ? WHERE id_compra = ?', (venda.status, id_compra))
        if venda.chassi_moto:
            cursor.execute('UPDATE Vendas SET chassi_moto = ? WHERE id_compra = ?', (venda.chassi_moto, id_compra))
        if venda.cpf_cliente:
            cursor.execute('UPDATE Vendas SET cpf_cliente = ? WHERE id_compra = ?', (venda.cpf_cliente, id_compra))
        if venda.preco is not None:  # Verifica se o preço foi fornecido
            cursor.execute('UPDATE Vendas SET preco = ? WHERE id_compra = ?', (venda.preco, id_compra))

        conn.commit()
        conn.close()
        print("Venda atualizada com sucesso!")

    def deletar_venda(self, id_compra):
        # Remove uma venda da tabela pelo ID da compra
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Vendas WHERE id_compra = ?', (id_compra,))
        conn.commit()
        conn.close()
        print("Venda deletada com sucesso!")