# This Python file uses the following encoding: utf-8
# Importa a biblioteca customtkinter e a renomeia para ctk
from menu import *

# Cria a janela principal do aplicativo
app = ctk.CTk()
app.geometry('1280x620')  # Define as dimensões da janela (largura x altura)
app.title('Sistema ATA')  # Define o título da janela
app.resizable(width=False, height=False)  # Trava o dimensionamento da janela
ctk.set_default_color_theme("dark-blue")  # Define o tema de cores para "dark-blue"
ctk.set_appearance_mode("dark")  # Define o tema "dark" (modo escuro)


# Função para criar os campos de cadastro
def cadastro():
    # Cria um campo de entrada de texto para c cadastro
    nome = ctk.CTkEntry(app, width=300, placeholder_text="Nome:")
    nome.place(x=220, y=40)

    cpf = ctk.CTkEntry(app, width=300, placeholder_text="CPF:")
    cpf.place(x=220, y=80)

    num_inscricao = ctk.CTkEntry(app, width=300, placeholder_text='número de inscrição:')
    num_inscricao.place(x=220, y=120)

    placa = ctk.CTkEntry(app, width=300, placeholder_text='Placa:')
    placa.place(x=220, y=160)

    ano_carro = ctk.CTkEntry(app, width=300, placeholder_text='Ano do carro:')
    ano_carro.place(x=220, y=200)

    modelo_carro = ctk.CTkEntry(app, width=300, placeholder_text='Modelo do carro:')
    modelo_carro.place(x=220, y=240)

    endereco = ctk.CTkEntry(app, width=300, placeholder_text='Endereço:')
    endereco.place(x=220, y=280)

    vaga = ctk.CTkEntry(app, width=300, placeholder_text='Vaga:')
    vaga.place(x=220, y=320)

    # Cria um botão para fazer o cadastro
    bt_cadastro = ctk.CTkButton(app, text='cadastrar')
    bt_cadastro.place(x=220, y=380)


# frames config
frame1 = ctk.CTkFrame(master=app, width=190, height=400).place(x=10, y=20)
frame2 = ctk.CTkFrame(master=app, width=320, height=400).place(x=210, y=20)
frame3 = ctk.CTkFrame(master=app, width=700, height=580).place(x=550, y=20)


# Seleção de tema

def tema_select():
    texto_tema = ctk.CTkLabel(app, text='Tema')
    texto_tema.place(x=10, y=520)

    bt_tema = ctk.CTkOptionMenu(app, values=["system", "dark", "light"], command=novo_tema)
    bt_tema.place(x=10, y=550)
    bt_tema.set("system")


tema_select()

cadastro()

app.mainloop()
