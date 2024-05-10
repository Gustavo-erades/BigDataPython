import streamlit as st 
from graficos import *
from estilos import *
def switch(dados,categoria):
    '''
    categoriasGraficoDispercao = ["Mais importante num consultório","O que mais é valorizado num consultório","O que te afasta de um consultório","Por que voltar a um consultório","Como melhorar um consultório","Melhores formas de pagamento","Melhores canais de comunicação"]
    '''
    if(categoria=="Mais importante num consultório"):
        categoriasGraficoDispercao = ["O que mais é valorizado num consultório"]
        categoriaDispercao = st.sidebar.selectbox('Selecione a categoria para relacionar as respostas', options = categoriasGraficoDispercao)
        st.write( '<h2 style="' + estilo_relacao_css + '">'+categoriaDispercao+' X '+categoria+'</h2>', unsafe_allow_html=True)
        return st.write(graficoDispercao(dados,categoriaDispercao,categoria))
    elif(categoria=="O que mais é valorizado num consultório"):
        categoriasGraficoDispercao = ["O que te afasta de um consultório","Por que voltar a um consultório"]
        categoriaDispercao = st.sidebar.selectbox('Selecione a categoria para relacionar as respostas', options = categoriasGraficoDispercao)
        st.write( '<h2 style="' + estilo_relacao_css + '">'+categoria+' X '+categoriaDispercao+'</h2>', unsafe_allow_html=True)
        return st.write(graficoDispercao(dados,categoria,categoriaDispercao))
    elif(categoria=="O que te afasta de um consultório"):
        categoriasGraficoDispercao = ["O que mais é valorizado num consultório"]
        categoriaDispercao = st.sidebar.selectbox('Selecione a categoria para relacionar as respostas', options = categoriasGraficoDispercao)
        st.write( '<h2 style="' + estilo_relacao_css + '">'+categoria+' X '+categoriaDispercao+'</h2>', unsafe_allow_html=True)
        return st.write(graficoDispercao(dados,categoriaDispercao,categoria))
    elif(categoria=="Por que voltar a um consultório"):
        categoriasGraficoDispercao = ["O que mais é valorizado num consultório"]
        categoriaDispercao = st.sidebar.selectbox('Selecione a categoria para relacionar as respostas', options = categoriasGraficoDispercao)
        st.write( '<h2 style="' + estilo_relacao_css + '">'+categoria+' X '+categoriaDispercao+'</h2>', unsafe_allow_html=True)
        return st.write(graficoDispercao(dados,categoriaDispercao,categoria))
    elif(categoria=="Como melhorar um consultório"):
        categoriasGraficoDispercao = ["O que mais é valorizado num consultório","Melhores formas de pagamento","Melhores canais de comunicação"]
        categoriaDispercao = st.sidebar.selectbox('Selecione a categoria para relacionar as respostas', options = categoriasGraficoDispercao)
        st.write( '<h2 style="' + estilo_relacao_css + '">'+categoria+' X '+categoriaDispercao+'</h2>', unsafe_allow_html=True)
        return st.write(graficoDispercao(dados,categoriaDispercao,categoria))
    else:
        st.write('<span style="' + estilo_erro_css + '">Essa pergunta não possui gráficos de dispersão associados!</span>', unsafe_allow_html=True)
        