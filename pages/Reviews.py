import streamlit as st
import pandas as pd

st.set_page_config(layout="wide") #deixa o layout da página mais largo

try:
    ratings= pd.read_csv("datasets/customer reviews.csv", encoding="utf-8")
    top_100= pd.read_csv("datasets/Top-100 Trending Books.csv", encoding="utf-8")  

except Exception as e: #caso nao leia a tabela o programa não morre na hora
    st.error(f"Erro ao ler CSV: {e}")

#caixa de seleção:
livros = top_100["book title"].unique() #faz uma lista lendo cada um de maneira separada
livro = st.sidebar.selectbox("Livros", livros) #cria uma caixa de seleção p cada livro

df_livro= top_100[top_100["book title"]== livro] #faz o filtro pra mostrar apenas o livro selecionado
df_reviews= ratings[ratings["book name"]== livro] #faz o filtro pra mostrar apenas as avaliações do livro selecionado

#separa cada info do livro
titulo_livro= df_livro["book title"].iloc[0]
genero_livro= df_livro["genre"].iloc[0]
preço_livro= f"${df_livro['book price'].iloc[0]}" #f pra por o cifrão
rating_livro= df_livro["rating"].iloc[0]
ano_livro= df_livro["year of publication"].iloc[0]

#título e genero do livro
st.title(titulo_livro)
st.subheader(genero_livro)

#cria 3 colunas lado a lado
col1,col2,col3=st.columns(3)
col1.metric("Preço", preço_livro)
col2.metric("Avaliação", rating_livro)
col3.metric("Ano de Publicação", ano_livro)

st.divider() #cria uma linha de separação

#mostra as avaliações do livro selecionado
for row in df_reviews.values:  #row=linha 
   message = st.chat_message(f"{row[4]}")
   titulo_review=message.write(f"**{row[2]}**")#2 seleciona a coluna 2 que é do titulo
   review=message.write(row[5])#5 seleciona a coluna 5 que é da descrição

