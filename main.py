# GitHub: RaimundoAlexandre
import customtkinter as ctk
import tabela
import customtkinter as ctk
import sqlite3
from tkinter import messagebox
from tabela import criar_tabela, exibir_dados, limpar_tabela
from cadastrar import cadastrar_taxista

# Cria a janela principal do aplicativo
app = ctk.CTk()
app.geometry('1280x620')  # Define as dimensões da janela (largura x altura)
app.title('TaxiSys')  # Define o título da janela
app.resizable(width=False, height=False)  # Trava o dimensionamento da janela
ctk.set_default_color_theme("dark-blue")  # Define o tema de cores para "dark-blue"
ctk.set_appearance_mode("dark")  # Define o tema "dark" (modo escuro)

# Criar a tabela
criar_tabela(app)

# frames config
frame1 = ctk.CTkFrame(master=app, width=320, height=400).place(x=10, y=20)
frame2 = ctk.CTkFrame(master=app, width=1050, height=200).place(x=210, y=450)
frame3 = ctk.CTkFrame(master=app, width=500, height=200).place(x=380, y=50)

# Função para definir o tema
def novo_tema(tema: str):
    ctk.set_appearance_mode(tema)


# Variáveis globais para os campos de entrada
nome = None
cpf = None
num_inscricao = None
placa = None
ano_carro = None
modelo_carro = None
endereco = None
vaga = None


# Função para criar os campos de cadastro
def entrada_cadastro():
    # Criação dos campos de entrada
    nome = ctk.CTkEntry(frame1, width=300, placeholder_text="Nome:")
    nome.place(x=20, y=40)
    cpf = ctk.CTkEntry(frame1, width=300, placeholder_text="CPF:")
    cpf.place(x=20, y=80)
    num_inscricao = ctk.CTkEntry(frame1, width=300, placeholder_text='número de inscrição:')
    num_inscricao.place(x=20, y=120)
    placa = ctk.CTkEntry(frame1, width=300, placeholder_text='Placa:')
    placa.place(x=20, y=160)
    ano_carro = ctk.CTkEntry(frame1, width=300, placeholder_text='Ano do carro:')
    ano_carro.place(x=20, y=200)
    modelo_carro = ctk.CTkEntry(frame1, width=300, placeholder_text='Modelo do carro:')
    modelo_carro.place(x=20, y=240)
    endereco = ctk.CTkEntry(frame1, width=300, placeholder_text='Endereço:')
    endereco.place(x=20, y=280)
    vaga = ctk.CTkEntry(frame1, width=300, placeholder_text='Vaga:')
    vaga.place(x=20, y=320)

    # Cria um botão para fazer o cadastro
    bt_cadastro = ctk.CTkButton(frame1, text='Cadastrar',
                                command=lambda: cadastrar_taxista_callback(nome, cpf, num_inscricao, placa, ano_carro,
                                                                           modelo_carro, endereco, vaga))
    bt_cadastro.place(x=20, y=380)

    # Retornar somente os valores em uma tupla
    return nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga


# Função de callback para chamar a função cadastrar_taxista com os campos corretos
def cadastrar_taxista_callback(nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga):
    cadastrar_taxista(
        nome.get(),
        cpf.get(),
        num_inscricao.get(),
        placa.get(),
        ano_carro.get(),
        modelo_carro.get(),
        endereco.get(),
        vaga.get()
    )

    # Limpar os campos após o cadastro
    nome.delete(0, ctk.END)
    cpf.delete(0, ctk.END)
    num_inscricao.delete(0, ctk.END)
    placa.delete(0, ctk.END)
    ano_carro.delete(0, ctk.END)
    modelo_carro.delete(0, ctk.END)
    endereco.delete(0, ctk.END)
    vaga.delete(0, ctk.END)

    # Atualizar a tabela com os novos dados
    atualizar_tabela()


# Função para chamar a função de cadastro de taxista
def cadastrar():
    # Obter os valores dos campos de entrada
    nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga = entrada_cadastro()

    # Chamar a função cadastrar_taxista passando os valores
    cadastrar_taxista(
        nome.get(),
        cpf.get(),
        num_inscricao.get(),
        placa.get(),
        ano_carro.get(),
        modelo_carro.get(),
        endereco.get(),
        vaga.get()
    )

    # Limpar os campos após o cadastro
    nome.delete(0, ctk.END)
    cpf.delete(0, ctk.END)
    num_inscricao.delete(0, ctk.END)
    placa.delete(0, ctk.END)
    ano_carro.delete(0, ctk.END)
    modelo_carro.delete(0, ctk.END)
    endereco.delete(0, ctk.END)
    vaga.delete(0, ctk.END)

    # Atualizar a tabela com os novos dados
    atualizar_tabela()

    # Agendar a próxima atualização da tabela
    app.after(1000, atualizar_tabela)


# Função para atualizar a tabela com os dados dos taxistas cadastrados
def atualizar_tabela():
    global dados_exibidos
    # Definir a variável de controle como False para exibir os dados novamente
    dados_exibidos = False

    # Limpar a tabela antes de exibir os dados atualizados
    limpar_tabela()

    # Exibir os dados dos taxistas na tabela
    exibir_dados()

    # Definir a variável de controle como True para indicar que os dados foram exibidos
    dados_exibidos = True

    # Agendar a próxima atualização da tabela
    # app.after(1000, atualizar_tabela)


# Botão para atualizar a tabela manualmente
bt_atualizar = ctk.CTkButton(app, text='Atualizar Tabela', command=atualizar_tabela)
bt_atualizar.place(x=1100, y=420)

# tabela dos cadastrados
criar_tabela(app)


def deletar_taxista():
    # Obter o nome digitado pelo usuário
    nome_taxista = entry_deletar.get()

    # Conectar ao banco de dados
    conn = sqlite3.connect("taxistas.db")
    cursor = conn.cursor()

    # Verificar se o taxista com o nome informado existe
    cursor.execute("SELECT * FROM taxistas WHERE nome=?", (nome_taxista,))
    taxista = cursor.fetchone()

    if taxista:
        # Deletar o taxista
        cursor.execute("DELETE FROM taxistas WHERE nome=?", (nome_taxista,))
        conn.commit()

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Taxista {nome_taxista} deletado com sucesso.")
    else:
        # Exibir mensagem de erro
        messagebox.showerror("Erro", f"Taxista {nome_taxista} não encontrado.")

    # Fechar a conexão com o banco de dados
    conn.close()


# Criar o botão para deleção
bt_deletar = ctk.CTkButton(app, text='Deletar Taxista', command=deletar_taxista)
bt_deletar.place(x=1130, y=80)  # Posição à direita da janela

# Criar a entrada para o nome do taxista a ser deletado
entry_deletar = ctk.CTkEntry(app, width=300, placeholder_text="Nome do Taxista")
entry_deletar.place(x=970, y=40)  # Posição à direita da janela

# Seleção de tema
def tema_select():
    texto_tema = ctk.CTkLabel(app, text='Tema')
    texto_tema.place(x=10, y=520)

    bt_tema = ctk.CTkOptionMenu(app, values=["system", "dark", "light"], command=novo_tema)
    bt_tema.place(x=10, y=550)
    bt_tema.set("system")


tema_select()

entrada_cadastro()
# Inicializar a atualização da tabela
atualizar_tabela()

app.mainloop()
