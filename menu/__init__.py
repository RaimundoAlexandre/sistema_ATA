# Importa a biblioteca customtkinter e a renomeia para ctk
import customtkinter as ctk


# Função para definir o tema
def novo_tema(tema: str):
    ctk.set_appearance_mode(tema)
