import sqlite3

# Classe AgendaRevisao que define o objeto Revisao
class Revisao:
    def __init__(self, data, custo, status_revisao, chassi_moto, cpf_cliente):
        self.data = data
        self.custo = custo
        self.status_revisao = status_revisao
        self.chassi_moto = chassi_moto
        self.cpf_cliente = cpf_cliente

# Classe AgendaRevisaoDAO para acessar os dados da tabela AgendaRevisoes
class AgendaRevisaoDAO:
    def __init__(self, db_path):
        self.db_path = db_path

    def conectar(self):
        # Conecta ao banco de dados
        return sqlite3.connect(self.db_path)

    def adicionar_revisao(self, revisao):
        # Adiciona uma nova revisão à tabela AgendaRevisoes
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO AgendaRevisoes (data, custo, status_revisao, chassi_moto, cpf_cliente) 
            VALUES (?, ?, ?, ?, ?)
        ''', (revisao.data, revisao.custo, revisao.status_revisao, revisao.chassi_moto, revisao.cpf_cliente))
        conn.commit()
        conn.close()
        print("Revisão adicionada com sucesso!")

    def listar_revisoes(self):
        # Lista todas as revisões cadastradas
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM AgendaRevisoes')
        revisoes = cursor.fetchall()
        conn.close()
        return revisoes

    def buscar_revisao(self, id_revisao):
        # Busca uma revisão pelo ID
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM AgendaRevisoes WHERE id_revisao = ?', (id_revisao,))
        revisao = cursor.fetchone()
        conn.close()
        return revisao

    def atualizar_revisao(self, id_revisao, data=None, custo=None, status_revisao=None, chassi_moto=None, cpf_cliente=None):
        # Atualiza os dados de uma revisão específica
        conn = self.conectar()
        cursor = conn.cursor()

        # Atualiza os dados conforme os parâmetros fornecidos
        if data:
            cursor.execute('UPDATE AgendaRevisoes SET data = ? WHERE id_revisao = ?', (data, id_revisao))
        if custo:
            cursor.execute('UPDATE AgendaRevisoes SET custo = ? WHERE id_revisao = ?', (custo, id_revisao))
        if status_revisao:
            cursor.execute('UPDATE AgendaRevisoes SET status_revisao = ? WHERE id_revisao = ?', (status_revisao, id_revisao))
        if chassi_moto:
            cursor.execute('UPDATE AgendaRevisoes SET chassi_moto = ? WHERE id_revisao = ?', (chassi_moto, id_revisao))
        if cpf_cliente:
            cursor.execute('UPDATE AgendaRevisoes SET cpf_cliente = ? WHERE id_revisao = ?', (cpf_cliente, id_revisao))

        conn.commit()
        conn.close()
        print("Revisão atualizada com sucesso!")

    def deletar_revisao(self, id_revisao):
        # Remove uma revisão da tabela pelo ID
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM AgendaRevisoes WHERE id_revisao = ?', (id_revisao,))
        conn.commit()
        conn.close()
        print("Revisão deletada com sucesso!")


# Testando o CRUD para agenda de revisões
if __name__ == "__main__":
    revisao_dao = AgendaRevisaoDAO('db.db')

    # Criar algumas revisões
    revisao1 = Revisao("2024-10-20", 250.00, "Aguardando", "ABC123456789", "12345678900")
    revisao2 = Revisao("2024-11-01", 300.00, "Aguardando Peça", "DEF987654321", "98765432100")
    
    # Adicionar revisões ao banco de dados
    revisao_dao.adicionar_revisao(revisao1)
    revisao_dao.adicionar_revisao(revisao2)

    # Listar todas as revisões
    print("Lista de Revisões:")
    for revisao in revisao_dao.listar_revisoes():
        print(revisao)

    # Buscar uma revisão específica
    print("\nBuscando Revisão com ID 1:")
    print(revisao_dao.buscar_revisao(1))

    # Atualizar uma revisão
    print("\nAtualizando o status da revisão com ID 1...")
    revisao_dao.atualizar_revisao(1, status_revisao="Revisado")

    # Listar todas as revisões após atualização
    print("\nLista de Revisões após atualização:")
    for revisao in revisao_dao.listar_revisoes():
        print(revisao)

    # Deletar uma revisão
    print("\nDeletando a revisão com ID 2...")
    revisao_dao.deletar_revisao(2)

    # Listar todas as revisões após exclusão
    print("\nLista de Revisões após exclusão:")
    for revisao in revisao_dao.listar_revisoes():
        print(revisao)
