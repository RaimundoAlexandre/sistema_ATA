import customtkinter as ctk
import sqlite3


def procurar(nome_taxista):
    # Conectar ao banco de dados
    conn = sqlite3.connect("taxistas.db")
    cursor = conn.cursor()

    # Procurar o taxista pelo nome
    cursor.execute("SELECT * FROM taxistas WHERE nome=?", (nome_taxista,))
    dados_taxista = cursor.fetchone()

    # Fechar a conexão com o banco de dados
    conn.close()

    # Retornar os dados do taxista encontrado ou None se não for encontrado
    return dados_taxista