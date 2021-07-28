import streamlit as st

def write():
    st.markdown(''' 
    # Dashboard de classificação

    Essa aplicação se divide em 4 partes:

    ## Base de Dados

    O arquivo utilizado como base para o treinamento de modelos é o "Noteiras.xlsx", gerado com a junção 
    de duas bases de dados com empresas anotadas como noteiras (1) ou não noteiras (0).
    
    Na aba "Base de Dados", temos a opção de adicionar novas bases de dados à base Noteiras original.
    Para isso, basta adicionar o nome do arquivo com empresas noteiras no espaço "Digite o nome do arquivo de empresas noteiras"
    e o arquivo de empresas não noteiras no espaço "Digite o nome do arquivo de empresas noteiras". A coluna de identificação de classes
    será incluída automaticamente, portanto não é necessária a adição manual. Caso o arquivo não esteja no 
    mesmo diretório que essa aplicação, o caminho completo para o arquivo deve ser passado.
    É importante de os arquivos adicionados tenham o mesmo número de colunas e as mesmas colunas (com os nomes exatamente iguais) para a adição ser feita corretamente.
    Depois de adicionados os novos arquivos, a base original no diretório também será alterada.

    Caso o arquivo Noteiras não seja mais de interesse, ou haja necessidade de alteração das colunas, basta excluir o arquivo do diretório da aplicação
    e criar outro de mesmo nome, com uma coluna no final chamada "Class" preenchida por 1 caso a empresa seja noteira 
    e 0 caso a empresa não seja noteira.

    A Classe 1 representa empresas noteiras e a Classe 0 empresas não noteiras.    
    
    ## Exploração de Dados

    Nesta página são exibidos gráficos (histogramas) de cada coluna comparando o comportamento das empresas noteiras vs não noteiras.
    As colunas a serem plotadas podem ser selecionadas na aba "Escolha uma ou mais colunas para ver os histogramas da distribuição de cada classe".
    
    ## Treinamento de Modelos

    A página Treinamento de Modelos exibe inicialmente a base de dados que está sendo utilizada, por precaução. Em seguida,
    são exibidos em uma tabela os modelos disponíveis do algoritmo Pycaret, seguidos de sua acurácia e outros parâmetros de avaliação. De acordo com os resultados exibidos,
    o usuário deve preencher o campo "Digite o nome do modelo a ser treinado" com a sigla (indíce da tabela) do modelo mais satisfatório e abaixo com o nome com que o modelo 
    será salvo no diretório depois de treinado. O botão "Escolher modelo!" inicia o treinamento.

    Em poucos segundos serão exibidas algumas figuras:
    * Tabela com acurácia e outros parâmetros de cada um dos conjuntos de treinamento;
    * Curva ROC do modelo;
    * Matriz de confusão com valores verdadeiros (True Class) vs valores preditos (Predicted Class);
    * (Em alguns casos) Tabela com as colunas de maior importância para as decisões do modelo;
    * Tabela com as predições da base de validação (o modelo separa automaticamente uma porcentagem da base de dados original, que não utiliza durante o treinamento, para fazer a validação).

    Por último, o caminho onde o modelo foi salvo é exibido.

    ## Predição dos dados

    Uma vez que algum modelo é treinado e salvo no diretório desta aplicação, ele pode ser utilizado para realizar a predição de uma outra base de dados.
    Selecione um dos modelos disponíveis no seu diretório (que foram previamente treinados) e no campo "Nome da base para predição" insira o nome do arquivo 
    que deseja realizar a predição (ou o caminho completo do arquivo caso ele não esteja no diretório principal). Em seguida, basta clicar em Realizar predição. 
    A base predita pode ser salva como arquivo excel.
    
    **Importante:** A base de predição deve ter exatamente as mesmas colunas do arquivo utilizado para treinamento do modelo. Caso contrário, a predição será feita de maneira incorreta.

    ''')