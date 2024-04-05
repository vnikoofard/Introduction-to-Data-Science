import streamlit as st
import plotly.express as px
import json
from Mundo import *

st.set_page_config(page_title="Asia", page_icon="🇯🇵", layout="wide")

st.subheader("Ásia")
st.markdown("""
            A Ásia é o maior dos continentes, tanto em área como em população.
            
            Ela é dividida entre:
            - Ásia Central
            - Ásia Oriental
            - Ásia Meridional
            - Ásia Ocidental
            - Sudeste Asiático
            
            Seus principais países são: China, Índia, Indonésia, Paquistão e Bangladesh.
            """)
st.divider()

col1, col2 = st.columns(2)

col1.plotly_chart(grafico_barras_populosos("Asia", "Turbo"))
col2.plotly_chart(grafico_bolhas("Asia"))

mais_populoso, maior_expectativa_vida, maior_pib_per_capita, menos_populoso,menor_expectativa_vida, menor_pib_per_capita = calcular_metricas_continente("Asia")

col3, col4, col5 = st.columns(3)
col6, col7, col8 = st.columns(3)

col3.metric(label="Mais Populoso", value=f"{mais_populoso}")
col4.metric(label="Maior Expectativa de Vida", value=f"{maior_expectativa_vida}")
col5.metric(label="Maior PIB per Capita", value=f"{maior_pib_per_capita}")
col6.metric(label="Menos Populoso", value=f"{menos_populoso}")
col7.metric(label="Menor Expectativa de Vida", value=f"{menor_expectativa_vida}")
col8.metric(label="Menor PIB per Capita", value=f"{menor_pib_per_capita}")
