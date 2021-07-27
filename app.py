import streamlit as st
import pandas as pd
import numpy as np
import pages.base
import pages.modelos
import pages.exploracao
import pages.predicao

MENU = {
    "Base de Dados" : pages.base,
    "Treinamento de Modelos": pages.modelos,
    "Exploração de Dados" : pages.exploracao,
    "Predição de Dados" : pages.predicao
}

def main():

    st.sidebar.title("Projeto Noteiras")

    password = st.text_input("Digite a senha")
    if password == 'minhasenha':
        menu_selection = st.sidebar.radio("Escolha uma opção", list(MENU.keys()))

        menu = MENU[menu_selection]
        with st.spinner(f"Loading {menu_selection} ..."):
            menu.write()


if __name__ == "__main__":
    main()
