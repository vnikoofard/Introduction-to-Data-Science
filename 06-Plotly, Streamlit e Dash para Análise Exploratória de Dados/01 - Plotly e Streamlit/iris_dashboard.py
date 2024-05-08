import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboard Iris", page_icon="🌺")

st.title("Dashboard Iris")

st.write("Este é um dashboard interativo para análise dos dados Iris.")

iris = px.data.iris()

iris = iris.rename(columns={"sepal_length":"comprimento_sepala",
                            "sepal_width":"largura_sepala",
                            "petal_length":"comprimento_petala",
                            "petal_width":"largura_petala",
                            "species":"espécie",
                            "species_id":"id_espécie"})

def atualizar_grafico(especies_escolhidas, amostra):
    dados_filtrados = iris[(iris['espécie'].isin(especies_escolhidas)) & (iris['comprimento_petala'] >= amostra[0]) & (iris['comprimento_petala'] <= amostra[1])]
    fig = px.scatter(dados_filtrados,
                    x= "comprimento_petala",
                    y = "largura_petala",
                        color="espécie",
                            title="Gráfico de dispersão: Espécies de Iris")

    fig.update_layout(xaxis_title="Comprimento da Sépala",
                    yaxis_title="Largura da Sépala")
    
    return fig


especies_escolhidas = st.multiselect(label = "Escolha uma ou mais espécies",
                options=iris["espécie"].unique(),
                default=iris["espécie"].unique())

amostra = st.slider("Comprimento de Pétala",
                    min_value=iris["comprimento_petala"].min(),
                    max_value=iris["comprimento_petala"].max(),
                    value=(iris["comprimento_petala"].min(),
                           iris["comprimento_petala"].max()),
                    step=0.1)

st.plotly_chart(atualizar_grafico(especies_escolhidas,amostra))
