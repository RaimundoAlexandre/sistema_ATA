import customtkinter as ctk
import tabela

from tabela import criar_tabela, exibir_dados, limpar_tabela
from cadastrar import cadastrar_taxista

# Cria a janela principal do aplicativo
app = ctk.CTk()
app.geometry('1280x620')  # Define as dimensões da janela (largura x altura)
app.title('Sistema ATA')  # Define o título da janela
app.resizable(width=False, height=False)  # Trava o dimensionamento da janela
ctk.set_default_color_theme("dark-blue")  # Define o tema de cores para "dark-blue"
ctk.set_appearance_mode("dark")  # Define o tema "dark" (modo escuro)

# Criar a tabela
criar_tabela(app)

# frames config
frame1 = ctk.CTkFrame(master=app, width=320, height=400).place(x=10, y=20)
frame2 = ctk.CTkFrame(master=app, width=1050, height=200).place(x=210, y=450)


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


# ...

# Função para criar os campos de cadastro
def entrada_cadastro():
    global nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga
    # Criação dos campos de entrada
    nome = ctk.CTkEntry(frame1, width=300, placeholder_text="Nome:")
    nome.place(x=20, y=40)
    cpf = ctk.CTkEntry(frame1, width=300, placeholder_text="CPF:")
    cpf.place(x=20, y=80)
    num_inscricao = ctk.CTkEntry(frame1, width=300, placeholder_text='Número de Inscrição:')
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
    bt_cadastro = ctk.CTkButton(frame1, text='Cadastrar', command=cadastrar)
    bt_cadastro.place(x=20, y=380)

    # Retornar somente os valores em uma tupla
    return nome, cpf, num_inscricao, placa, ano_carro, modelo_carro, endereco, vaga


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


def atualizar_tabela():
    # Limpar a tabela antes de exibir os dados atualizados
    tabela.limpar_tabela()

    # Exibir os dados dos taxistas na tabela
    tabela.exibir_dados()

    # Agendar a próxima atualização da tabela
    app.after(1000, atualizar_tabela)


# Botão para atualizar a tabela manualmente
bt_atualizar = ctk.CTkButton(app, text='Atualizar Tabela', command=atualizar_tabela)
bt_atualizar.place(x=1100, y=420)

# tabela dos cadastrados
criar_tabela(app)


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
