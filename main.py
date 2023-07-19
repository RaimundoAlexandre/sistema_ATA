import customtkinter as ctk

app = ctk.CTk()
app.geometry('800x600')
app.title('Sistema ATA')
app.resizable(width=False, height=False)  # trava o dimensionamento
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark")  # seta o tema dark


def cadastro():
    nome = ctk.CTkEntry(app, placeholder_text="Nome:")
    nome.place(x=10, y=10)  # .pack(padx=10, pady=10)
    idade = ctk.CTkEntry(app, placeholder_text="Idade:")
    idade.place(x=10, y=50)  # pack(padx=10, pady=10)

    bt_cadastro = ctk.CTkButton(app, text='Cadastrar')
    bt_cadastro.place(x=10, y=90)  # pack(padx=10, pady=10)


cadastro()

app.mainloop()
