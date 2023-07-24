import sqlite3
import sqlite3
import customtkinter as ctk
from tkinter import ttk

# Variável global para verificar se os dados já foram exibidos
dados_exibidos = False


def criar_tabela(parent):
    global tabela
    # Criação da Treeview (tabela)
    tabela = ttk.Treeview(parent, columns=(
        "Nome", "CPF", "Número de Inscrição", "Placa", "Ano do Carro", "Modelo do Carro", "Endereço", "Vaga"))

    # Definir os cabeçalhos das colunas
    tabela.heading("#0", text="", anchor=ctk.CENTER)
    tabela.heading("Nome", text="Nome", anchor=ctk.CENTER)
    tabela.heading("CPF", text="CPF", anchor=ctk.CENTER)
    tabela.heading("Número de Inscrição", text="Número de Inscrição", anchor=ctk.CENTER)
    tabela.heading("Placa", text="Placa", anchor=ctk.CENTER)
    tabela.heading("Ano do Carro", text="Ano do Carro", anchor=ctk.CENTER)
    tabela.heading("Modelo do Carro", text="Modelo do Carro", anchor=ctk.CENTER)
    tabela.heading("Endereço", text="Endereço", anchor=ctk.CENTER)
    tabela.heading("Vaga", text="Vaga", anchor=ctk.CENTER)

    # Definir largura das colunas
    tabela.column("#0", minwidth=0, width=0, stretch=ctk.NO)
    tabela.column("Nome", anchor=ctk.W, width=120)
    tabela.column("CPF", anchor=ctk.W, width=100)
    tabela.column("Número de Inscrição", anchor=ctk.W, width=140)
    tabela.column("Placa", anchor=ctk.W, width=100)
    tabela.column("Ano do Carro", anchor=ctk.W, width=100)
    tabela.column("Modelo do Carro", anchor=ctk.W, width=140)
    tabela.column("Endereço", anchor=ctk.W, width=200)
    tabela.column("Vaga", anchor=ctk.W, width=80)

    # Definir tema dark para a tabela
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview",
                    background="#2a2d2e",
                    foreground="white",
                    rowheight=25,
                    fieldbackground="#343638",
                    bordercolor="#343638",
                    borderwidth=0)
    style.map('Treeview', background=[('selected', '#22559b')])

    style.configure("Treeview.Heading",
                    background="#565b5e",
                    foreground="white",
                    relief="flat")
    style.map("Treeview.Heading",
              background=[('active', '#3484F0')])

    # Empacotar a tabela
    tabela.pack(expand=ctk.YES, fill=ctk.BOTH)

    # Restante do código em tabela.py, caso haja...

    # define a posição
    tabela.place(x=210, y=460, width=1050, height=150)

    return tabela


# Função para limpar a tabela
def limpar_tabela():
    # Obter todos os itens da tabela
    itens = tabela.get_children()

    # Percorrer todos os itens na tabela e removê-los
    for item in itens:
        tabela.delete(item)


def exibir_dados():
    global dados_exibidos
    # Limpar a tabela antes de exibir os dados
    limpar_tabela()

    # Conectar ao banco de dados
    conn = sqlite3.connect("taxistas.db")
    cursor = conn.cursor()

    # Verificar se a tabela "taxistas" existe
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS taxistas (id INTEGER PRIMARY KEY, nome TEXT, cpf TEXT, num_inscricao TEXT,"
        " placa TEXT, ano_carro TEXT, modelo_carro TEXT, endereco TEXT, vaga TEXT)")

    # Consultar os dados dos taxistas
    cursor.execute("SELECT * FROM taxistas")
    dados_taxistas = cursor.fetchall()

    # Exibir os dados na tabela
    for taxista in dados_taxistas:
        tabela.insert("", "end", values=taxista)

        # Atualizar a variável para indicar que os dados já foram exibidos
        dados_exibidos = True
    # Exibir os dados na tabela
    for taxista in dados_taxistas:
        print(taxista)  # Adicione esta linha para exibir os dados
    # Fechar a conexão com o banco de dados
    conn.close()
