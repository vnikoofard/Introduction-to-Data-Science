from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

funcionarios = pd.read_csv("funcionarios.csv")
funcionarios = funcionarios.rename(columns={
    'satisfaction_level': 'Nível de Satisfação',
    'last_evaluation': 'Última Avaliação',
    'number_project': 'Número de Projetos',
    'average_montly_hours': 'Média de Horas Mensais',
    'time_spend_company': 'Tempo na Empresa',
    'Work_accident': 'Acidente de Trabalho',
    'left': 'Deixou a Empresa',
    'promotion_last_5years': 'Promoção nos Últimos 5 Anos',
    'Departments ': 'Departamentos',
    'salary': 'Salário'
})

funcionarios["Deixou a Empresa"] = funcionarios["Deixou a Empresa"].astype("str")
funcionarios["Promoção nos Últimos 5 Anos"] = funcionarios["Promoção nos Últimos 5 Anos"].astype("str")
funcionarios['Deixou a Empresa'] = funcionarios['Deixou a Empresa'].replace({'0': 'Não', '1': 'Sim'})

mapeamento_departamentos = {
    'sales': 'Vendas',
    'accounting': 'Contabilidade',
    'hr': 'Recursos Humanos',
    'technical': 'Tecnologia',
    'support': 'Suporte',
    'management': 'Gerência',
    'IT': 'TI',
    'product_mng': 'Gerenciamento de Produto',
    'marketing': 'Marketing',
    'RandD': 'Pesquisa e Desenvolvimento'
}

mapa_cores = {
    "Não":"#04BF9D",
    "Sim":"#F27457"
}

# Aplicando o mapeamento à coluna 'Departamento'
funcionarios['Departamentos'] = funcionarios['Departamentos'].map(mapeamento_departamentos)

funcionarios['Promoção nos Últimos 5 Anos'] = funcionarios['Promoção nos Últimos 5 Anos'].replace({'0': 'Não', '1': 'Sim'})

funcionarios['Salário'] = funcionarios['Salário'].replace({'low': 'Baixo', 'medium': 'Médio', 'high': 'Alto'})

def fig1_agrupar_ou_nao(agrupar):
    
    if agrupar == "Não":
        chancedesair = funcionarios.groupby('Deixou a Empresa').size().reset_index(name='counts')
        fig1 = px.bar(chancedesair, x="Deixou a Empresa", y="counts", color="Deixou a Empresa", color_discrete_map=mapa_cores, text_auto=True, range_y=[0, 14e3])
        fig1.update_layout(title='Rotatividade de Funcionários da Empresa',
                           xaxis_title='Saiu da Empresa',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="array", categoryarray=["Alta", "Média", "Pouca"])
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)

        return fig1
    else:
        chancedesair = funcionarios.groupby(['Deixou a Empresa']).size().reset_index(name='counts')
        fig1 = px.bar(chancedesair, x="Deixou a Empresa", y="counts", color="Deixou a Empresa", color_discrete_map=mapa_cores, text_auto=True, range_y=[0, 14e3])
        fig1.update_layout(title='Rotatividade de Funcionários da Empresa',
                           xaxis_title='Saiu da Empresa',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')
        fig1.update_traces(showlegend=False)

        fig1.update_xaxes(categoryorder="array", categoryarray=["Alta", "Média", "Pouca"])
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        return fig1
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fig2_agrupar_ou_nao(agrupar):
    
        if agrupar == "Não":
            chancedesair = funcionarios.groupby('Departamentos').size().reset_index(name='counts')
            fig1 = px.bar(chancedesair, x="Departamentos", y="counts", color="Departamentos", color_discrete_sequence=px.colors.qualitative.Bold ,text_auto=True, range_y=[0, 4500])
            fig1.update_layout(title='Departamentos da Empresa e Número de Funcionários',	
                            xaxis_title='Departamentos',
                            yaxis_title='Número de Funcionários', 
                            plot_bgcolor='white',
                            paper_bgcolor='white',
                            font_color='black')

            fig1.update_xaxes(categoryorder="total descending", tickangle = 45)
            fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
            fig1.update_traces(showlegend=False)

            return fig1
        else:
            chancedesair = funcionarios.groupby(['Departamentos', 'Deixou a Empresa']).size().reset_index(name='counts')
            fig1 = px.bar(chancedesair, x="Departamentos", y="counts", color="Deixou a Empresa", color_discrete_map=mapa_cores,text_auto=True, range_y=[0, 4500])
            fig1.update_layout(title='Departamentos da Empresa e Número de Funcionários',
                            xaxis_title='Departamentos',
                            yaxis_title='Número de Funcionários', 
                            plot_bgcolor='white',
                            paper_bgcolor='white',
                            font_color='black')

            fig1.update_xaxes(categoryorder="total descending", tickangle = 45)
            fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
            fig1.update_traces(showlegend=False)


            return fig1    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mapa_cores2 = {
    "Não":"#026873",
    "Sim":"#03A688"
}

def fig3_agrupar_ou_nao(agrupar):
    
    if agrupar == "Não":
        chancedesair = funcionarios.groupby('Promoção nos Últimos 5 Anos').size().reset_index(name='counts')
        fig1 = px.bar(chancedesair, x="Promoção nos Últimos 5 Anos", y="counts", color="Promoção nos Últimos 5 Anos", color_discrete_map=mapa_cores2, text_auto=True, range_y=[0, 15e3])
        fig1.update_layout(title='Funcionários que Obtiveram Aumento nos Últimos 5 Anos',
                           xaxis_title='Aumento',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
    else:
        chancedesair = funcionarios.groupby(['Promoção nos Últimos 5 Anos', 'Deixou a Empresa']).size().reset_index(name='counts')
        fig1 = px.bar(chancedesair, x="Promoção nos Últimos 5 Anos", y="counts", color="Deixou a Empresa", color_discrete_map=mapa_cores, text_auto=True, range_y=[0, 15e3])
        fig1.update_layout(title='Funcionários que Obtiveram Aumento nos Últimos 5 Anos',
                           xaxis_title='Aumento',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mapa_cores3 = {
    "Baixo":"#347355",
    "Médio":"#60BF81",
    "Alto":"#93D94E"
}

def fig4_agrupar_ou_nao(agrupar):
    
    if agrupar == "Não":
        chancedesair = funcionarios.groupby('Salário').size().reset_index(name='counts')
        fig1 = px.bar(chancedesair, x="Salário", y="counts", color="Salário", color_discrete_map=mapa_cores3, text_auto=True, range_y=[0, 8e3])
        fig1.update_layout(title='Nível do Salário dos Funcionários',
                           xaxis_title='Nível do Salário',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
    else:
        chancedesair = funcionarios.groupby(['Salário', 'Deixou a Empresa']).size().reset_index(name='counts')
        fig1 = px.bar(chancedesair, x="Salário", y="counts", color="Deixou a Empresa",color_discrete_map=mapa_cores, text_auto=True, range_y=[0, 8e3])
        fig1.update_layout(title='Nível do Salário dos Funcionários',
                           xaxis_title='Nível do Salário',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1    
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df_notas = funcionarios['Nível de Satisfação'].apply(lambda x: round(x * 10) / 10).reset_index(name='Nível de Satisfação')
notas_agrups = df_notas.groupby('Nível de Satisfação').size().reset_index(name='counts')


mapa_cores4 = {
    0.1:"red",
    1:"green"
}

def fig5_agrupar_ou_nao(agrupar):
    if agrupar == "Não":
        fig1 = px.bar(notas_agrups, x="Nível de Satisfação", y="counts", color="Nível de Satisfação", color_continuous_scale="RdYlGn", text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Nível de Satisfação dos Funcionários',
                           xaxis_title='Nível de Satisfação',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending", dtick=0.1)
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        fig1.update_traces(showlegend=False)
        fig1.update_coloraxes(showscale=False)
        return fig1
    else:
        fig1 = px.histogram(funcionarios, x="Nível de Satisfação", color="Deixou a Empresa", color_discrete_map=mapa_cores,nbins=10, text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Nível de Satisfação dos Funcionários',
                           xaxis_title='Nível de Satisfação',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending", dtick=0.1)
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
    
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
df_perf = funcionarios['Última Avaliação'].apply(lambda x: round(x * 10) / 10).reset_index(name='Última Avaliação')
perf_agrups = df_perf.groupby('Última Avaliação').size().reset_index(name='counts')


def fig6_agrupar_ou_nao(agrupar):
    if agrupar == "Não":
        fig1 = px.bar(perf_agrups, x="Última Avaliação", y="counts", color="Última Avaliação", color_continuous_scale="RdYlGn", text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Nota de Desempenho dos Funcionários',
                           xaxis_title='Nota de Desempenho',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        fig1.update_coloraxes(showscale=False)
        return fig1
    else:
        fig1 = px.histogram(funcionarios, x="Última Avaliação", color="Deixou a Empresa", color_discrete_map=mapa_cores, nbins=10, text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Nota de Desempenho dos Funcionários',
                           xaxis_title='Nota de Desempenho',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending", dtick=0.1)
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
agrup_projs = funcionarios.groupby('Número de Projetos').size().reset_index(name='counts')

def fig7_agrupar_ou_nao(agrupar):
    if agrupar == "Não":
        fig1 = px.bar(agrup_projs, x="Número de Projetos", y="counts", color="Número de Projetos", color_continuous_scale="agsunset", text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Número de Projetos em Andamento dos Funcionários',
                           xaxis_title='Número de Projetos em Andamento',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        fig1.update_coloraxes(showscale=False)
        return fig1
    else:
        fig1 = px.histogram(funcionarios, x="Número de Projetos", color="Deixou a Empresa", color_discrete_map=mapa_cores, nbins=6, text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Número de Projetos em Andamento dos Funcionários',
                           xaxis_title='Número de Projetos em Andamento',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def fig8_agrupar_ou_nao(agrupar):
    if agrupar == "Não":
        fig1 = px.histogram(funcionarios, x="Média de Horas Mensais", nbins=12, color_discrete_sequence=["#93BFB7"], text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Média de Horas Trabalhadas no Mês pelos Funcionários',
                           xaxis_title='Média de Horas Trabalhadas no Mês',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
    else:
        fig1 = px.histogram(funcionarios, x="Média de Horas Mensais", color="Deixou a Empresa", color_discrete_map=mapa_cores, nbins=20, text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Média de Horas Trabalhadas no Mês pelos Funcionários',
                           xaxis_title='Média de Horas Trabalhadas no Mês',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fig9_agrupar_ou_nao(agrupar):
    if agrupar == "Não":
        fig1 = px.histogram(funcionarios, x="Tempo na Empresa", color_discrete_sequence=["#93BFB7"], text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Tempo de Trabalho dos Funcionários na Empresa',
                           xaxis_title='Tempo de Trabalho dos Funcionários (anos)',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
    else:
        fig1 = px.histogram(funcionarios, x="Tempo na Empresa", color="Deixou a Empresa", color_discrete_map=mapa_cores, text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Tempo de Trabalho dos Funcionários na Empresa',
                           xaxis_title='Tempo de Trabalho dos Funcionários (anos)',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
funcionarios['Acidente de Trabalho'] = funcionarios['Acidente de Trabalho'].replace({0: 'Não Acidentados', 1: 'Acidentados'})

mapa_cores6 = {
    "Não Acidentados":"#89D99D",
    "Acidentados":"#F23030"
}

def fig10_agrupar_ou_nao(agrupar):
    if agrupar == "Não":
        fig1 = px.histogram(funcionarios, x="Acidente de Trabalho", color="Acidente de Trabalho", color_discrete_map=mapa_cores6, text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Quantidade de Funcionários Acidentados',
                           xaxis_title='Acidente',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1
    else:
        fig1 = px.histogram(funcionarios, x="Acidente de Trabalho", color="Deixou a Empresa", color_discrete_map=mapa_cores, text_auto=True).update_layout(bargap=0.05)
        fig1.update_layout(title='Quantidade de Funcionários Acidentados',
                           xaxis_title='Acidente',
                           yaxis_title='Número de Funcionários', 
                           plot_bgcolor='white',
                           paper_bgcolor='white',
                           font_color='black')

        fig1.update_xaxes(categoryorder="total descending")
        fig1.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='#D9D9D9')
        fig1.update_traces(showlegend=False)
        return fig1

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="Rotatividade", #titulo
                    page_icon="👔", #icone
                      layout="wide") #esticar a tela

st.title('Visualização de Funcionários')

col3, col4 = st.columns(2)

col3.subheader("Gráfico de Variáveis Categóricas")
col4.subheader("Gráfico de Variáveis Numéricas")

    

# Chama a função correspondente ao gráfico selecionado
def mudar_graf1(dado, agrupar):
  if dado == "SDE" and agrupar == "Não agrupar":
    return fig1_agrupar_ou_nao("Não")
  elif dado == "SDE" and agrupar == "Agrupar":
    return fig1_agrupar_ou_nao("Não")
  elif dado == "DEPS" and agrupar == "Não agrupar":
    return fig2_agrupar_ou_nao("Não")
  elif dado == "DEPS" and agrupar == "Agrupar":
    return fig2_agrupar_ou_nao("Sim")
  elif dado == "PNU5A" and agrupar == "Não agrupar":
    return fig3_agrupar_ou_nao("Não")
  elif dado == "PNU5A" and agrupar == "Agrupar":
    return fig3_agrupar_ou_nao("Sim")
  elif dado == "NDS" and agrupar == "Não agrupar":
    return fig4_agrupar_ou_nao("Não")
  elif dado == "NDS" and agrupar == "Agrupar":
    return fig4_agrupar_ou_nao("Sim")
  elif dado == "ANT" and agrupar == "Não agrupar":
    return fig10_agrupar_ou_nao("Não")
  elif dado == "ANT" and agrupar == "Agrupar":
    return fig10_agrupar_ou_nao("Sim")
  
def mudar_graf2(dado, agrupar):
  
  if dado == "NST" and agrupar == "Não agrupar":
    return fig5_agrupar_ou_nao("Não") 
  elif dado == "NST" and agrupar == "Agrupar":
    return fig5_agrupar_ou_nao("Sim")

  elif dado == "UAR" and agrupar == "Não agrupar":
    return fig6_agrupar_ou_nao("Não")
  elif dado == "UAR" and agrupar == "Agrupar":
    return fig6_agrupar_ou_nao("Sim")

  elif dado == "NPEA" and agrupar == "Não agrupar":
    return fig7_agrupar_ou_nao("Não")
  elif dado == "NPEA" and agrupar == "Agrupar":
    return fig7_agrupar_ou_nao("Sim")

  elif dado == "HDTM" and agrupar == "Não agrupar":
    return fig8_agrupar_ou_nao("Não")
  elif dado == "HDTM" and agrupar == "Agrupar":
    return fig8_agrupar_ou_nao("Sim")

  elif dado == "TNE" and agrupar == "Não agrupar":
    return fig9_agrupar_ou_nao("Não")
  elif dado == "TNE" and agrupar == "Agrupar":
    return fig9_agrupar_ou_nao("Sim")

    
# Layout em duas colunas
col1, col2 = st.columns(2)

# Dropdown e botão de seleção para a primeira coluna
with col1:
    grafico_escolhido1 = st.selectbox("Escolha o gráfico:", ["SDE", "DEPS", "PNU5A", "NDS", "ANT"])
    agrupar1 = st.radio("Agrupar ou Não Agrupar?:", ("Não agrupar", "Agrupar"), key="agrupar1")  # Adicionando uma chave única

# Dropdown e botão de seleção para a segunda coluna
with col2:
    grafico_escolhido2 = st.selectbox("Escolha o gráfico:", ["NST", "UAR", "NPEA", "HDTM", "TNE"])
    agrupar2 = st.radio("Agrupar ou Não Agrupar?:", ("Não agrupar", "Agrupar"), key="agrupar2")  # Adicionando uma chave única

# Exibição dos gráficos
with col1:
    st.plotly_chart(mudar_graf1(grafico_escolhido1, agrupar1))

with col2:
    st.plotly_chart(mudar_graf2(grafico_escolhido2, agrupar2))
