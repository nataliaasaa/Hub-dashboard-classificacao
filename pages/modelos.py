import streamlit as st
import os
from pycaret.classification import *
from utils.functions import *

def write():
    st.markdown(''' 
    # Treinamento de modelos    
    ''')
    
    df = loadCSV()
    #df = clean_df(df)
    st.markdown(''' 
    ## Base de dados utilizada    
    ''')
    st.dataframe(df)

    st.markdown(''' 
    ## Modelos disponíveis    
    ''')
    # Setup do pycaret
    clf1 = setup(df, target = 'Class', session_id=123, log_experiment=True, normalize = True, transformation = True, silent=True, experiment_name='noteira')
    # Comparando os modelos
    best_model = compare_models(fold=5)
    # Output para dataframe p visualização
    best_model_results = pull()
    st.dataframe(best_model_results)
    
    st.markdown(''' 
    #### Escolha o modelo com melhor acurácia, e no campo "Digite o nome do modelo a ser treinado", digite a sigla do modelo como está escrita no índice da tabela acima.    
    ''')
    
    # Escolhendo o melhor modelo
    choose_model = st.text_input("Digite o nome do modelo a ser treinado: ")
    choose_name_model = st.text_input("Digite o nome com que o modelo será salvo: ")
    if st.button('Escolher modelo!'):
        my_model = create_model(choose_model)
        tuned_model = tune_model(my_model)
        tuned_model_results = pull()
        st.dataframe(tuned_model_results)
        plot_model(tuned_model, plot = 'auc', display_format='streamlit')
        plot_model(tuned_model, plot = 'confusion_matrix', display_format='streamlit')
        try:
            plot_model(tuned_model, plot = 'feature', display_format='streamlit')
            st.markdown(''' ### Colunas de maior importância para a classificação''')
            feature_importance = pd.DataFrame({'Feature': get_config('X_train').columns, 'Value' : abs(tuned_model.coef_[0])}).sort_values(by='Value', ascending=False)        
            st.dataframe(feature_importance)
        except:
            pass
        evaluate_model(tuned_model)
        # Salvando modelo
        save_model(tuned_model, model_name=choose_name_model)
        my_path = os.getcwd()
        st.markdown(" Modelo salvo em " + my_path + "/" + choose_name_model + ".pkl")