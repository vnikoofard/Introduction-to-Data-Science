import streamlit as st
import plotly.express as px
import json

# Dashboard Mundo

st.set_page_config(page_title="Mundo", page_icon="🌍", layout="wide")

st.sidebar.markdown("Desenvolvido por [João Ricardo](https://github.com/Joao-Ricardo-Arcoverde)")
st.sidebar.markdown("Documentação [Streamlit](https://docs.streamlit.io/library/api-reference)")
st.sidebar.markdown("Documentação [Plotly](https://plotly.com/python/)")


st.title("Dashboard Mundo")

st.subheader("Introdução")

st.markdown("""
        Este é um dashboard interativo que nos
         apresenta informações sobre os **continentes do mundo**, como população, PIB per capita, expectativa de vida, etc. 
         
        Com ele poderemos observar as principais características de cada continente e comparar os dados entre eles.
            
         Use o menu lateral para navegar entre as páginas e
         explorar as principais informações de cada continente!
            """)

st.divider()

linhas_territoriais = json.load(open("world-countries.json",'r'))
mundo = px.data.gapminder().rename(columns={"country":"país",
                              "continent":"continente",
                              "year":"ano",
                               "lifeExp":"ExpVida",
                               "pop":"pop",
                               "gdpPercap":"PIBpercap",
                               "iso_alpha":"sigla",
                                "iso_num":"num_sigla",
                                 })

def mapa_mundi(lat, lon):
     fig1 = px.choropleth_mapbox(mundo,
                     geojson=linhas_territoriais,
                     locations="sigla",
                     color="pop",
                     color_continuous_scale="Sunsetdark",
                     mapbox_style="open-street-map",
                     zoom=1.1,
                     opacity=1,
                     width=1300,
                     height=700,
                     center={"lat":lat, "lon":lon})
     fig1.update_geos(fitbounds="locations", visible=False)
     fig1.update_layout(title="Mapa-múndi",
                    xaxis_title="Longitude",
                    yaxis_title="Latitude",
                    legend_title="População")

     return fig1


st.markdown("**Clique abaixo para visualizar o mapa-múndi**") 

btn = st.button("Mapa-múndi")

if btn:
    st.plotly_chart(mapa_mundi(20,0))
    col1, col2, col3 = st.columns(3)
    col1.metric(label="População Mundial", value=f"{mundo[mundo['ano']==2007]['pop'].sum():,.0f}")
    col2.metric(label="Países", value=f"{mundo['país'].nunique()}")
    col3.metric(label="Continentes", value=f"{mundo['continente'].nunique()}")


def grafico_barras_populosos(continente, tema):
    continente = mundo[mundo["continente"]==continente]
    continente_2007_populosos = continente[continente["ano"]==2007].sort_values("pop", ascending=False).head(5)

    fig1 = px.bar(
        continente_2007_populosos,
        x="país",
        y="pop",
        color="pop",
        color_continuous_scale=tema,
        text_auto=True
    )
    fig1.update_layout(title="Os 5 países mais populosos em 2007",
                        xaxis_title="Países",
                        yaxis_title="População",
                        legend_title="População")

    return fig1

def grafico_bolhas(continente):
    continente = mundo[mundo["continente"]==continente]
    fig2 = px.scatter(
        continente[continente["ano"]==2007],
        x="ExpVida",
        y="PIBpercap",
        size="pop",
        color="país",
        color_discrete_sequence=px.colors.qualitative.Set1,
        log_y=True,
        size_max=60,
        range_x=[40,85]
    )


    fig2.update_layout(title="Expectativa de vida x PIB per capita",
                        xaxis_title="Expectativa de vida",
                        yaxis_title="PIB per capita",
                        legend_title="Países")

    return fig2

def calcular_metricas_continente(continente):
    continente_data = mundo[mundo['continente'] == continente]
    
    mais_populoso = continente_data.loc[continente_data['pop'].idxmax()]["país"]
    maior_expectativa_vida = continente_data.loc[continente_data['ExpVida'].idxmax()]["país"]
    maior_pib_per_capita = continente_data.loc[continente_data['PIBpercap'].idxmax()]["país"]
    menos_populoso = continente_data.loc[continente_data['pop'].idxmin()]["país"]
    menor_expectativa_vida = continente_data.loc[continente_data['ExpVida'].idxmin()]["país"]
    menor_pib_per_capita = continente_data.loc[continente_data['PIBpercap'].idxmin()]["país"]
    
    return mais_populoso, maior_expectativa_vida, maior_pib_per_capita, menos_populoso, menor_expectativa_vida, menor_pib_per_capita




