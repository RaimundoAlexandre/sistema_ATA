import sqlite3


def cadastrar_taxista(nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga):
    # Conectar ao banco de dados (ou criar o banco se não existir)
    conn = sqlite3.connect("taxistas.db")
    cursor = conn.cursor()

    # Criar a tabela de taxistas, caso não exista
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS taxistas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            num_inscricao TEXT NOT NULL,
            placa TEXT NOT NULL,
            ano_carro TEXT NOT NULL,
            modelo_carro TEXT NOT NULL,
            endereco TEXT NOT NULL,
            vaga TEXT NOT NULL
        )
    """)

    # Inserir o novo taxista na tabela
    cursor.execute("""
        INSERT INTO taxistas (nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga,))

    # Salvar as alterações no banco de dados
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()
