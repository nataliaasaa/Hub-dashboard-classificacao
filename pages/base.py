import streamlit as st
from PIL import Image
import pandas as pd
from io import BytesIO
from utils.functions import *

def write():
    st.markdown(''' 
    # Base de dados 

    A base de dados inicial utilizada é o aquivo Noteiras.xlsx.
   
    Novas bases de dados podem ser adicionadas à base original, 
    basta especificar o nome do arquivo XLSX no campo disponível. 
    Os arquivos de empresas noteiras e não noteiras devem ser adicionados 
    separadamente.  

    Obs: Se o arquivo não estiver no diretório em que o programa está
    sendo executado, basta escrever o caminho completo do arqivo.
    ''')
    
    df = loadCSV()

    if st.checkbox("Adicionar novas bases de dados."): 

        filename_noteira = st.text_input('Digite o nome do arquivo de empresas noteiras:')
        filename_nao_noteira = st.text_input('Digite o nome do arquivo de empresas não noteiras:')

        if st.button('Adicionar!'):
            # Base das empresas noteiras com coluna de classe = 1
            df_noteira = pd.read_excel(filename_noteira)
            df_noteira['Class'] = 1
            # Base das empresas não noteiras com coluna de classe = 0
            df_nao_noteira = pd.read_excel(filename_nao_noteira)
            df_nao_noteira['Class'] = 0
            # Concatenando as duas mais a base original
            df = pd.concat([df, df_noteira, df_nao_noteira], ignore_index=True)
    
    df_final = clean_df(df)
    df_final.to_excel('Noteiras.xlsx', index=False)
    st.dataframe(df_final)



