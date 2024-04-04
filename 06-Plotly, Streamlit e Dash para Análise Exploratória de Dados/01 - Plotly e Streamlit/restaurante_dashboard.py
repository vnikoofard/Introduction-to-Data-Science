import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Dashboard Restaurante", page_icon="🍽️")

st.sidebar.markdown("Desenvolvido por [João Ricardo](https://github.com/Joao-Ricardo-Arcoverde)")

st.title("Dashboard Restaurante")

st.write("Este é um dashboard interativo para análise dos dados de clientes de um restaurante.")

st.write("## Análise de Contas")

escolha = st.radio("Escolha um Gráfico", ["Contas por Dia", "Homens e Mulheres", "Fumantes vs Não Fumantes"])

restaurante = px.data.tips().rename(columns={"total_bill":"conta_total",
                           "tip":"gorjeta",
                           "sex":"genero",
                            "smoker":"fumante",
                            "day":"dia",
                            "time":"horário",
                            "size":"tamanho"})
mapeamento_sexo = {
    'Male': 'Homem',
    'Female': 'Mulher'
    }

mapeamento_fumante = {
    'Yes': 'Sim',
    'No': 'Não'}

mapeamento_dia = {
    'Sun':'Dom',
    'Sat':'Sab',
    'Thur':'Qui',
    'Fri':'Sex'
}

mapeamento_ref = {
    'Dinner':'Jantar',
    'Lunch':'Almoço'
}

restaurante['genero'] = restaurante['genero'].replace(mapeamento_sexo)
restaurante['fumante'] = restaurante['fumante'].replace(mapeamento_fumante)
restaurante['dia'] = restaurante['dia'].replace(mapeamento_dia)
restaurante['horário'] = restaurante['horário'].replace(mapeamento_ref)

def atualizar_grafico(escolha):
    receitas_dias = restaurante.groupby("dia")["conta_total"].sum().reset_index(name="Total")

    mapa_ordem = ["Qui","Sex","Sab","Dom"]
    mapa_cores_dias = {"Qui":"gray",
                "Sex":"red",
                "Sab":"gray",
                "Dom":"gray"}

    fig1 = px.bar(data_frame = receitas_dias,
                x="dia",
                y="Total",
                color = "dia",
                color_discrete_map=mapa_cores_dias,
                text_auto = True)
    fig1.update_xaxes(categoryorder="array",
                    categoryarray=mapa_ordem)
    fig1.update_layout(title="Dias Mais Movimentados",
                    xaxis_title="Dia",
                    yaxis_title="Quantidade")

    #-----------------#

    homens_mulheres = restaurante["genero"].value_counts().reset_index(name="Qtd")

    mapa_cores_genero = {"Homem":"blue",
                "Mulher":"pink" }

    fig2 = px.bar(data_frame = homens_mulheres,
                x="genero",
                y="Qtd",
                color="genero",
                color_discrete_map=mapa_cores_genero)

    fig2.update_layout(title="Homens e Mulheres - Gastos",
                  xaxis_title="Gênero",
                  yaxis_title="Quantidade")
    
    #-----------------#

    fumantes = restaurante["fumante"].value_counts().reset_index(name="Qtd")
    mapa_cores_fuma = {"Sim":"green",
              "Não":"red" }

    fig3 = px.bar(data_frame = fumantes,
                x="fumante",
                y="Qtd",
                color="fumante",
                color_discrete_map=mapa_cores_fuma,
                barmode="group")

    fig3.update_layout(title="Homens e Mulheres - Fumantes",
                    xaxis_title="Fumante",
                    yaxis_title="Quantidade")
    
    if escolha == "Contas por Dia":
        return fig1
    elif escolha == "Homens e Mulheres":
        return fig2
    else:
        return fig3

st.plotly_chart(atualizar_grafico(escolha))

col1, col2, col3, col4 = st.columns(4)

col1.metric(label=":green[Total]", value=f"R$ {restaurante['conta_total'].sum():.2f}")
col2.metric(label=":black[Gorjetas]", value=f"R$ {restaurante['gorjeta'].sum():,.2f}")
col3.metric(label=":blue[Homens]", value=restaurante['genero'].value_counts().loc["Homem"])  
col4.metric(label=":violet[Mulheres]", value=restaurante['genero'].value_counts().loc["Mulher"])   
