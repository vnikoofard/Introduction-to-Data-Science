import streamlit as st
import plotly.express as px
import json
from Mundo import *

st.set_page_config(page_title="Europa", page_icon="🇩🇪", layout="wide")

st.subheader("Europa")
st.markdown("""
            A Europa é um dos continentes que compõem o supercontinente Euroasiático.

            Ela é dividade entre:
            - Europa Ocidentals
            - Europa Oriental
            
            Seus principais países são: Alemanha, França, Itália, Espanha e Reino Unido.
            """)

st.divider()

col1, col2 = st.columns(2)

col1.plotly_chart(grafico_barras_populosos("Europe", "Sunset"))
col2.plotly_chart(grafico_bolhas("Europe"))

mais_populoso, maior_expectativa_vida, maior_pib_per_capita, menos_populoso,menor_expectativa_vida, menor_pib_per_capita = calcular_metricas_continente("Europe")

col3, col4, col5 = st.columns(3)
col6, col7, col8 = st.columns(3)

col3.metric(label="Mais Populoso", value=f"{mais_populoso}")
col4.metric(label="Maior Expectativa de Vida", value=f"{maior_expectativa_vida}")
col5.metric(label="Maior PIB per Capita", value=f"{maior_pib_per_capita}")
col6.metric(label="Menos Populoso", value=f"{menos_populoso}")
col7.metric(label="Menor Expectativa de Vida", value=f"{menor_expectativa_vida}")
col8.metric(label="Menor PIB per Capita", value=f"{menor_pib_per_capita}")
