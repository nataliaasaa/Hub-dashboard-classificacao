
import streamlit as st
from pycaret.classification import *
from utils.functions import *
import os
import pandas as pd


def write():
    st.markdown(''' 
    # Predição

    * A Classe 1 representa empresas noteiras e a Classe 0 empresas não noteiras.    
    ''')

    #Lista os modelos disponíveis
    files = os.listdir()
    pkl_file_list = []
    for file in files:
        if file.endswith(".pkl"):
            pkl_file_list.append(file.rsplit('.', 1)[0])
    
    selet_model = st.selectbox('Selecione um dos modelos disponíveis: ', pkl_file_list)
    base_predicao = st.text_input('Nome da base para predição: ')
    
    if st.button('Realizar predição'):
        #Carrega a base a partir do nome escolhido
        predict_df = loadnewCSV(base_predicao)
        to_show = predict_df.copy()
        predict_df = clean_df_pred(predict_df)
        # Label encoder
        #predict_df = encoding(predict_df)
        
        # Carrega o modelo
        loaded_model = load_model(selet_model)
        # Predição
        predictions = predict_model(loaded_model, data=predict_df)
        to_show['Predição'] = predictions['Label']
        to_show['Score'] = predictions['Score']
        st.dataframe(to_show)

        
        
        st.markdown(get_table_download_link(to_show), unsafe_allow_html=True)
