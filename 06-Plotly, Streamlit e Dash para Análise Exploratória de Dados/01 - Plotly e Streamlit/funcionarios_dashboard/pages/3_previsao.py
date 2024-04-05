from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

data = pd.read_csv("funcionarios.csv")


#import module
from sklearn.cluster import KMeans
# Filter data
left_emp =  data[['satisfaction_level', 'last_evaluation']][data.left == 1]
# Create groups using K-means clustering.
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(left_emp)

#import module
from sklearn.cluster import KMeans
# Filter data
left_emp =  data[['satisfaction_level', 'last_evaluation']][data.left == 1]
# Create groups using K-means clustering.
kmeans = KMeans(n_clusters=3, random_state=0, n_init=10).fit(left_emp)

#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
data['salary']=le.fit_transform(data['salary'])
data['Departments ']=le.fit_transform(data['Departments '])

#Spliting data into Feature and
X=data[['satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident',
       'promotion_last_5years', 'Departments ', 'salary']]
y=data['left']


# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # 70% training and 30% test

#Import Gradient Boosting Classifier model
from sklearn.ensemble import GradientBoostingClassifier

#Create Gradient Boosting Classifier
gb = GradientBoostingClassifier()

#Train the model using the training sets
gb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gb.predict(X_test)
len(y_pred)


def testando(a,b,c,d,e,f,g,h,i):

    novo_registro = {
        'satisfaction_level': [a],
        'last_evaluation': [b],
        'number_project': [c],
        'average_montly_hours': [d],
        'time_spend_company': [e],
        'Work_accident': [f],
        'promotion_last_5years': [g],
        'Departments ': [h],  # Departamento 'marketing'
        'salary': [i]  # Salário 'medium'
    }
    if novo_registro['promotion_last_5years'][0] == 'Sim':
       novo_registro['promotion_last_5years'] = 1
    elif novo_registro['promotion_last_5years'][0] == 'Não':
        novo_registro['promotion_last_5years'] = 0
    if novo_registro['Work_accident'][0] == 'Sim':
        novo_registro['Work_accident'] = 1
    elif novo_registro['Work_accident'][0] == 'Não':
        novo_registro['Work_accident'] = 0
    if novo_registro['salary'][0] == 'Baixo':
        novo_registro['salary'] = 1
    elif novo_registro['salary'][0] == 'Médio':
        novo_registro['salary'] = 2
    elif novo_registro['salary'][0] == 'Alto':
        novo_registro['salary'] = 0
    if novo_registro["Departments "][0] == 'Vendas':
        novo_registro["Departments "] = 0
    elif novo_registro["Departments "][0] == 'Contabilidade':
        novo_registro["Departments "] = 1
    elif novo_registro["Departments "][0] == 'RH':
        novo_registro["Departments "] = 2
    elif novo_registro["Departments "][0] == 'Tecnologia':
        novo_registro["Departments "] = 3
    elif novo_registro["Departments "][0] == 'Suporte':
        novo_registro["Departments "] = 4
    elif novo_registro["Departments "][0] == 'Gerência':
        novo_registro["Departments "] = 5
    elif novo_registro["Departments "][0] == 'TI':
        novo_registro["Departments "] = 6
    elif novo_registro["Departments "][0] == 'Ger. de Produto':
        novo_registro["Departments "] = 7
    elif novo_registro["Departments "][0] == 'Marketing':
        novo_registro["Departments "] = 8
    elif novo_registro["Departments "][0] == 'Pesq. e Des.':
        novo_registro["Departments "] = 9

    

    novo_df = pd.DataFrame(novo_registro)
    return gb.predict_proba(novo_df)[0]
testando(0.38,
         0.53,
         2,
         157,
         3,
         "Não",
         "Não",
         "Marketing",
         "Baixo")
def prever_saida(satisfacao, avaliacao, projetos, horas_mes, tempo_empresa, departamento, promocao, salario, acidente):
    if promocao == 'Sim':
        promocao = 1
    elif promocao == 'Não':
        promocao = 0
    if acidente == 'Sim':
        acidente = 1
    elif acidente == 'Não':
        acidente = 0
    if salario == 'Baixo':
        salario = 1
    elif salario == 'Médio':
        salario = 2
    elif salario == 'Alto':
        salario = 0
    if departamento == 'Vendas':
        departamento = 0
    elif departamento == 'Contabilidade':
        departamento = 1
    elif departamento == 'RH':
        departamento = 2
    elif departamento == 'Tecnologia':
        departamento = 3
    elif departamento == 'Suporte':
        departamento = 4
    elif departamento == 'Gerência':
        departamento = 5
    elif departamento == 'TI':
        departamento = 6
    elif departamento == 'Ger. de Produto':
        departamento = 7
    elif departamento == 'Marketing':
        departamento = 8
    elif departamento == 'Pesq. e Des.':
        departamento = 9
    resultado = testando(satisfacao, avaliacao, projetos, horas_mes, tempo_empresa, 0, promocao, departamento, salario)
    ficar = np.round(resultado[0], 3) * 100
    sair = np.round(resultado[1], 3) * 100
    if ficar > sair:
        return f"Previsão: Funcionário irá permanecer, probabilidade de {ficar}%"
    else:
        return f"Previsão: Funcionário vai sair, probabilidade de {sair}%"
# Nível de Satisfação no Trabalho
satisfacao = st.slider("Nível de Satisfação no Trabalho", min_value=0.0, max_value=1.0, step=0.1, value=0.5)

# Última Avaliação Recebida
avaliacao = st.slider("Última Avaliação Recebida", min_value=0.4, max_value=1.0, step=0.1, value=0.5)

# Número de Projetos em Andamento
projetos = st.slider("Número de Projetos em Andamento", min_value=2, max_value=7, step=1, value=4)

# Horas de Trabalho Mensais
horas_mes = st.slider("Horas de Trabalho Mensais", min_value=80, max_value=320, step=20, value=130)

# Tempo na Empresa
tempo_empresa = st.slider("Tempo na Empresa", min_value=2, max_value=10, step=1, value=6)

# Departamento
departamento = st.select_slider(
    "Departamento",
    options=["Vendas", "Contabilidade", "RH", "Tecnologia", "Suporte", "Gerência", "TI", "Ger. de Produto", "Marketing", "Pesq. e Des."],
    value="Vendas"
)

# Promoção nos últimos 5 anos?
promocao = st.selectbox("Promoção nos últimos 5 anos?", ["Sim", "Não"])

# Salário
salario = st.selectbox("Salário", ["Baixo", "Médio", "Alto"])

# Acidente no Trabalho?
acidente = st.selectbox("Acidente no Trabalho?", ["Sim", "Não"])

# Botão de previsão
if st.button("Prever Saída"):
    resultado_previsao = prever_saida(satisfacao, avaliacao, projetos, horas_mes, tempo_empresa, departamento, promocao, salario, acidente)
    st.write(resultado_previsao)
