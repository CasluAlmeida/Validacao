import sqlite3

# Conectar ao banco de dados em memória (temporário)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Criando a tabela Contratado
cursor.execute('''
    CREATE TEMPORARY TABLE Contratado (
        id INTEGER PRIMARY KEY,
        Nome TEXT,
        CPF TEXT,
        id_profissao INTEGER,
        Datanascimento DATE
    );
''')

# Criando a tabela Profissao
cursor.execute('''
    CREATE TEMPORARY TABLE Profissao (
        id INTEGER PRIMARY KEY,
        Nome_profissao TEXT
    );
''')

# Criando a tabela Pagamento
cursor.execute('''
    CREATE TEMPORARY TABLE Pagamento (
        id_contratado INTEGER,
        Valor DECIMAL(10, 2),
        PRIMARY KEY (id_contratado),
        FOREIGN KEY (id_contratado) REFERENCES Contratado(id)
    );
''')

# Inserindo dados de exemplo na tabela Profissao
cursor.executemany('''
    INSERT INTO Profissao (id, Nome_profissao) VALUES (?, ?);
''', [
    (1, 'Advogado'),
    (2, 'Empresário'),
    (3, 'Médico')
])

# Inserindo dados de exemplo na tabela Contratado
cursor.executemany('''
    INSERT INTO Contratado (id, Nome, CPF, id_profissao, Datanascimento) VALUES (?, ?, ?, ?, ?);
''', [
    (1, 'João Silva', '12345678901', 1, '1980-01-01'),
    (2, 'Maria Oliveira', '98765432100', 2, '1985-05-23'),
    (3, 'Carlos Pereira', '45612378901', 1, '1990-11-15'),
    (4, 'Ana Santos', '74185296300', 3, '1982-07-30')
])

# Inserindo dados de exemplo na tabela Pagamento
cursor.executemany('''
    INSERT INTO Pagamento (id_contratado, Valor) VALUES (?, ?);
''', [
    (1, 5000.00),
    (2, 7000.00),
    (3, 5500.00),
    (4, 4000.00)
])

# Comitar as mudanças
conn.commit()

# Consultando os dados das tabelas
cursor.execute('SELECT * FROM Contratado')
print('Contratados:')
for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT * FROM Profissao')
print('\nProfissões:')
for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT * FROM Pagamento')
print('\nPagamentos:')
for row in cursor.fetchall():
    print(row)

# Fechando a conexão
conn.close()
