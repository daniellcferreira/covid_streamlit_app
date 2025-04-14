# Importando as bibliotecas necessárias
import pandas as pd
import plotly.express as px
import streamlit as st

# Lendo o dataset atualizado de COVID-19 por estado do Brasil
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Renomeando colunas para facilitar a leitura no app
df = df.rename(columns={
  'newDeaths': 'Novos óbitos',
  'newCases': 'Novos casos',
  'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes',
  'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'
})

# Criando a lista de estados disponíveis no dataset
estados = list(df['state'].unique())

# Barra lateral para o usuário escolher o estado
state = st.sidebar.selectbox('Qual estado?', estados)

# Definindo as opções de colunas que o usuário pode escolher para visualizar
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']

# Barra lateral para o usuário escolher qual informação deseja visualizar
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

# Filtrando o DataFrame para mostrar apenas os dados do estado selecionado
df = df[df['state'] == state]

# Criando o gráfico de linha com a informação selecionada
fig = px.line(
  df,
  x="date",
  y=column,
  title=f"{column} - {state}"
)

# Personalizando o layout do gráfico
fig.update_layout(
  xaxis_title='Data',         # Título do eixo X
  yaxis_title=column.upper(), # Título do eixo Y em letras maiúsculas
  title={'x': 0.5}            # Centralizando o título
)

# Exibindo o título e descrição do app
st.title('DADOS COVID - BRASIL')
st.write(
  'Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação '
  'para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.'
)

# Exibindo o gráfico no app
st.plotly_chart(fig, use_container_width=True)

# Exibindo a fonte dos dados
st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
