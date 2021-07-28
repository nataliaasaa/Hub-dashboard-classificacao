import pandas as pd
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import base64
from io import BytesIO

def loadCSV():
    df = pd.read_excel("Noteiras.xlsx")
    return df

def loadnewCSV(nome):
    df = pd.read_excel(nome)
    return df

def clean_df(df):
    my_list = ['CNPJ Raiz', 'razao social']
    my_nan_list = df.columns[df.isna().any()].tolist()
    for i in my_list:
        if i in df.columns:
            df.drop(i, axis=1, inplace=True)
    if 'CNAE Empresa' in df.columns:
        df['CNAE Empresa'] = df['CNAE Empresa'].replace("'-2", 0.0)
        df['CNAE Empresa'] = pd.to_numeric(df['CNAE Empresa'])

    df=df.dropna(axis=1, how='all', inplace=True)
    df.fillna(0, inplace=True)
    st.write("Colunas com valores nulos trocados por 0: ", my_nan_list)
    df.drop_duplicates(inplace=True, ignore_index=True)
    return df

def clean_df_pred(df):
    my_list = ['CNPJ Raiz', 'razao social','Qtde de Razão Social Diferente', '% Maior Fornecedor Últimos 180 dias']
    my_nan_list = df.columns[df.isna().any()].tolist()
    for i in my_list:
        if i in df.columns:
            df.drop(i, axis=1, inplace=True)
    if 'CNAE Empresa' in df.columns:
        df['CNAE Empresa'] = df['CNAE Empresa'].replace("'-2", 0.0)
        df['CNAE Empresa'] = pd.to_numeric(df['CNAE Empresa'])
    df.dropna(axis=1, how='all', inplace=True)
    df.fillna(0, inplace=True)
    st.write("Colunas com valores nulos trocados por 0: ", my_nan_list)
    return df

def encoding(df):
    le = LabelEncoder()
    for i in df.select_dtypes(include='object').columns:
        df[i] = le.fit_transform(df[i])
    return df

def to_excel(df):
            output = BytesIO()
            writer = pd.ExcelWriter(output)
            df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            processed_data = output.getvalue()
            return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download xlsx file</a>' # decode b'abc' => abc
