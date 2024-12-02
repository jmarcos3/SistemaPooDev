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

    def atualizar_revisao(self, revisao):
        # Atualiza os dados de uma revisão específica
        conn = self.conectar()
        cursor = conn.cursor()

        # Atualiza os dados conforme os parâmetros fornecidos
        if revisao.data:
            cursor.execute('UPDATE AgendaRevisoes SET data = ? WHERE chassi_moto = ?', (revisao.data, revisao.chassi_moto))
        if revisao.custo:
            cursor.execute('UPDATE AgendaRevisoes SET custo = ? WHERE chassi_moto = ?', (revisao.custo, revisao.chassi_moto))
        if revisao.status_revisao:
            cursor.execute('UPDATE AgendaRevisoes SET status_revisao = ? WHERE chassi_moto = ?', (revisao.status_revisao, revisao.chassi_moto))
        if revisao.chassi_moto:
            cursor.execute('UPDATE AgendaRevisoes SET chassi_moto = ? WHERE chassi_moto = ?', (revisao.chassi_moto, revisao.chassi_moto))
        if revisao.cpf_cliente:
            cursor.execute('UPDATE AgendaRevisoes SET cpf_cliente = ? WHERE chassi_moto = ?', (revisao.cpf_cliente, revisao.chassi_moto))

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

