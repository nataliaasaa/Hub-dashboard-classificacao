from utils.functions import *
import plotly.express as px


def write():
    st.markdown(''' 
    # Exploração de dados

    * A Classe 1 representa empresas noteiras e a Classe 0 empresas não noteiras.    
    ''')
    
    df = loadCSV()

    colunas = st.multiselect("Escolha uma ou mais colunas para ver os histogramas da distribuição de cada classe: ", df.columns)
    for i in colunas:
        fig = px.histogram(df, x=i, color="Class", barmode='overlay', color_discrete_sequence=["lightblue", "lightcoral"])
        st.plotly_chart(fig)