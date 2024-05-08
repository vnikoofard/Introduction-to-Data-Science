from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.sidebar.markdown("Desenvolvido por [João Ricardo](https://github.com/Joao-Ricardo-Arcoverde)")

st.write("# Rotatividade de Funcionários! 👔")

st.markdown(
        """

        A rotatividade é a taxa na qual os funcionários entram e saem de uma empresa em um determinado período de tempo.

        Perder um funcionário é caro para uma empresa. Conseguir outro é um processo **caro e demorado**.

        Nosso objetivo aqui é entender as causas da rotatividade de funcionários e como podemos prever quem está mais propenso a sair da empresa, para que a empresa possa tomar medidas preventivas.  
    
            """)