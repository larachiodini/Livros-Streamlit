import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide") #deixa o layout da página mais largo

try:
    top_100= pd.read_csv("datasets/Top-100 Trending Books.csv", encoding="utf-8")  
      
except Exception as e: #caso nao leia a tabela o programa não morre na hora
    st.error(f"Erro ao ler CSV: {e}")

#le o preço maximo
preço_max = top_100["book price"].max()

#le o preço mínimo
preço_min  = top_100["book price"].min()

#le a avaliação max
rating_max =top_100["rating"].max()

#le a avaliaçao min
rating_min =top_100["rating"].min()

#slider da tabela top100 - preços
slider_preço = st.sidebar.slider("Intervalo de Preço:", preço_min, preço_max, preço_max) #cria uma linha de preços no sidebar começando pelo max

#slider da tabela top100 - ratings
slider_rating= st.sidebar.slider("Intervalo de Avaliações:", rating_max, rating_min, rating_max)

#cria um flitro q quando passa o slider muda a o intervalo de preço e o de avaliaçoes 
df_geral= top_100[
    (top_100["book price"] <=slider_preço) & 
    (top_100["rating"] <=slider_rating)]

#chama a tabela
st.title("Top100 Livros:")
df_geral

#grafico de barras dos anos de publicação dos livros top100
fig = px.bar(df_geral["year of publication"].value_counts()) #crio o bar(barras) e conto os valores

#grafico histograma preço dos livros
fig_2= px.histogram(df_geral["book price"])

#deixo os graficos em duas colunas (lado a lado, n um embaixo do outro)
col1, col2 =st.columns(2)

col1.title("Ano de Publicação dos Livros: ")
col1.plotly_chart(fig) #chamo o chart(grafico) com a variavel das barras

col2.title("Preço dos Livros:")
col2.plotly_chart(fig_2) #chamo o chart(grafico) com a variavel do histograma


