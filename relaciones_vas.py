import numpy as np
from scipy.stats import bernoulli
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

# Parámetros para gráficos
plt.style.use('seaborn-darkgrid')

plt.rcParams.update({'font.size': 25})      
plt.rc('axes', labelsize=20)
plt.rc('legend', fontsize=18)  
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 
plt.rcParams['axes.titlesize'] = 25
plt.rcParams["figure.figsize"] = (15,6)


st.title('Simulaciones y Conductas Limites')
st.header('La Urna de Polya')
st.write("Simulación de la Urna de Polya para el curso MA3403-1")
st.write('En la siguiente sección podrá simular la urna de polya segun los parametros iniciales que se elijan')

st.header('Simulación')
st.write('Selecciona los valores iniciales de la simulación moviendo las perillas')

st.image("img/histograma.gif",
         use_column_width='always')
st.image("img/histograma_poisson.gif",
         use_column_width='always')
st.header('Notas')
st.markdown(
    """
- Creador de la app: Francisco Vasquez Leiva
- Mail: fvasquez at dim.uchile.cl
""")

st.write('Las tildes fueron eliminadas a proposito')

