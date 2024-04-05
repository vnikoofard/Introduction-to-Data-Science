import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime


if "data" not in st.session_state: #ao trocar de aba não queremos que execute novamente
    df_data = pd.read_csv("CLEAN_FIFA23_official_data.csv", index_col=0) 
    df_data = df_data[df_data["Contract Valid Until"] >= 2023] #jogadores com contrato ativo
    df_data = df_data[df_data["Value(£)"] > 0] #jogadores com valor de mercado maior que 0
    df_data = df_data.sort_values(by="Overall", ascending = False) #ordenando por Overall, dos melhores aos piores
    st.session_state["data"] = df_data #gravamos o df no session_state e jogamos no segundo projeto

st.write("# Dataset Fifa 23! ⚽") #aceita plotly, markdown, texto, etc.

st.sidebar.markdown("Desenvolvido por [João Ricardo](https://github.com/Joao-Ricardo-Arcoverde)")

btn = st.button("Acesse os dados no Kaggle")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

    st.markdown(
        """

        O conjunto de dados de jogadores de futebol de 2017 a 2023
        fornece informações abrangentes sobre jogadores de futebol
        profissionais. O conjunto de dados contém uma ampla gama
        de atributos, incluindo dados demográficos dos jogadores,
        características físicas, estatísticas de jogo, detalhes
        de contratos e afiliações de clubes. 
                  
        Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso
        valioso para analistas de futebol, pesquisadores e
        entusiastas interessados ​​em explorar vários
        aspectos do mundo do futebol, pois permite
        estudar atributos de jogadores, métricas de
        desempenho, avaliação de mercado, análise
        de clubes, posicionamento de jogadores e
        desenvolvimento do jogador ao longo do
        tempo.
            """)


