import sqlite3

db = sqlite3.connect('db.db')

cursor = db.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS Funcionarios (
     cpf TEXT PRIMARY KEY,        -- CPF será a chave primária
     nome TEXT NOT NULL,          -- Nome do funcionário
     usuario TEXT UNIQUE NOT NULL,-- Nome de usuário (único)
     senha TEXT NOT NULL,         -- Senha do funcionário
     funcao TEXT NOT NULL         -- Função: Vendedor, Secretaria, Mecanico, Gerente
 )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Motos (
    chassi TEXT PRIMARY KEY,   -- Chassi como chave primária (único para cada moto)
    ano INTEGER NOT NULL,      -- Ano de fabricação da moto
    preco REAL NOT NULL,       -- Preço da moto
    cor TEXT NOT NULL,         -- Cor da moto
    modelo TEXT NOT NULL       -- Modelo da moto
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
    cpf TEXT PRIMARY KEY,            -- CPF como chave primária
    nome TEXT NOT NULL,              -- Nome do cliente
    email TEXT NOT NULL             -- Email do cliente
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Vendas (
    id_compra INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID da compra (gerado automaticamente)
    data DATE NOT NULL,                          -- Data da compra
    status TEXT NOT NULL,                        -- Status da compra (ex: Preparando, A caminho, Pronto)
    chassi_moto TEXT NOT NULL,                   -- Chassi da moto (referencia a tabela Motos)
    cpf_cliente TEXT NOT NULL,                   -- CPF do cliente (referencia a tabela Clientes),
    preco REAL NOT NULL,                         -- Preço da moto,
    FOREIGN KEY (chassi_moto) REFERENCES Motos(chassi), -- Referência para a moto comprada
    FOREIGN KEY (cpf_cliente) REFERENCES Clientes(cpf)  -- Referência para o cliente que fez a compra
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS AgendaRevisoes (
    id_revisao INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID da revisão (gerado automaticamente)
    data DATE NOT NULL,                           -- Data agendada para a revisão
    custo REAL,                                   -- Custo da revisão
    status_revisao TEXT NOT NULL,                 -- Status da revisão (ex: Aguardando, Revisado, Aguardando Peça)
    chassi_moto TEXT NOT NULL,                    -- Chassi da moto (referência a tabela Motos)
    cpf_cliente TEXT NOT NULL,                    -- CPF do cliente (referência a tabela Clientes),
    FOREIGN KEY (chassi_moto) REFERENCES Motos(chassi),  -- Referência para a moto
    FOREIGN KEY (cpf_cliente) REFERENCES Clientes(cpf)   -- Referência para o cliente
)
''')




