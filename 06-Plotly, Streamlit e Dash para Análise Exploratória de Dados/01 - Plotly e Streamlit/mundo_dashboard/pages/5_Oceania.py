import streamlit as st
import plotly.express as px
import json 
from Mundo import *

st.set_page_config(page_title="Oceania", page_icon="🇦🇺", layout="wide")

st.subheader("Oceania")
st.markdown("""
            A Oceania é um continente insular, composto por regiões da Ásia e da América.
            
            Ela é dividida entre:
            - Australásia
            - Melanésia
            - Micronésia
            - Polinésia
            
            Seus principais países são: Austrália, Papua-Nova Guiné, Nova Zelândia, Fiji e Ilhas Salomão.
            """)
st.divider()

col1, col2 = st.columns(2)

col1.plotly_chart(grafico_barras_populosos("Oceania","Bluered"))
col2.plotly_chart(grafico_bolhas("Oceania"))

mais_populoso, maior_expectativa_vida, maior_pib_per_capita, menos_populoso,menor_expectativa_vida, menor_pib_per_capita = calcular_metricas_continente("Oceania")

col3, col4, col5 = st.columns(3)
col6, col7, col8 = st.columns(3)

col3.metric(label="Mais Populoso", value=f"{mais_populoso}")
col4.metric(label="Maior Expectativa de Vida", value=f"{maior_expectativa_vida}")
col5.metric(label="Maior PIB per Capita", value=f"{maior_pib_per_capita}")
col6.metric(label="Menos Populoso", value=f"{menos_populoso}")
col7.metric(label="Menor Expectativa de Vida", value=f"{menor_expectativa_vida}")
col8.metric(label="Menor PIB per Capita", value=f"{menor_pib_per_capita}")
