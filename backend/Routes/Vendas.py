import sqlite3

# Classe Venda que define o objeto Venda
class Venda:
    def __init__(self, data, status, chassi_moto, cpf_cliente):
        self.data = data
        self.status = status
        self.chassi_moto = chassi_moto
        self.cpf_cliente = cpf_cliente

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
            INSERT INTO Vendas (data, status, chassi_moto, cpf_cliente) 
            VALUES (?, ?, ?, ?)
        ''', (venda.data, venda.status, venda.chassi_moto, venda.cpf_cliente))
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

    def atualizar_venda(self, id_compra, data=None, status=None, chassi_moto=None, cpf_cliente=None):
        # Atualiza os dados de uma venda específica
        conn = self.conectar()
        cursor = conn.cursor()
        
        # Atualiza os dados conforme os parâmetros fornecidos
        if data:
            cursor.execute('UPDATE Vendas SET data = ? WHERE id_compra = ?', (data, id_compra))
        if status:
            cursor.execute('UPDATE Vendas SET status = ? WHERE id_compra = ?', (status, id_compra))
        if chassi_moto:
            cursor.execute('UPDATE Vendas SET chassi_moto = ? WHERE id_compra = ?', (chassi_moto, id_compra))
        if cpf_cliente:
            cursor.execute('UPDATE Vendas SET cpf_cliente = ? WHERE id_compra = ?', (cpf_cliente, id_compra))
        
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


# Testando o CRUD para vendas
if __name__ == "__main__":
    venda_dao = VendaDAO('db.db')

    # Criar algumas vendas
    venda1 = Venda("2023-10-15", "Preparando", "ABC123456789", "12345678900")
    venda2 = Venda("2023-10-16", "A caminho", "DEF987654321", "98765432100")
    
    # Adicionar vendas ao banco de dados
    venda_dao.adicionar_venda(venda1)
    venda_dao.adicionar_venda(venda2)

    # Listar todas as vendas
    print("Lista de Vendas:")
    for venda in venda_dao.listar_vendas():
        print(venda)

    # Buscar uma venda específica
    print("\nBuscando Venda com ID 1:")
    print(venda_dao.buscar_venda(1))

    # Atualizar uma venda
    print("\nAtualizando o status da venda com ID 1...")
    venda_dao.atualizar_venda(1, status="Pronto")

    # Listar todas as vendas após atualização
    print("\nLista de Vendas após atualização:")
    for venda in venda_dao.listar_vendas():
        print(venda)

    # Deletar uma venda
    print("\nDeletando a venda com ID 2...")
    venda_dao.deletar_venda(2)

    # Listar todas as vendas após exclusão
    print("\nLista de Vendas após exclusão:")
    for venda in venda_dao.listar_vendas():
        print(venda)
