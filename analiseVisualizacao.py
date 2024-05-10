import streamlit as st 
import pandas as pd
from graficos import *
from estilos import *
from trocaGrafDispercao import *
st.title('Análise das respostas com python')
st.write('<h6 style="'+titulo_css+'">Os gráficos abaixo representam de maneira gráfica as respostas no formulário de satisfação geral</h6>',unsafe_allow_html=True)
checkbox_mostrar_tabela=st.sidebar.checkbox('Mostrar tabela')
checkbox_mostrar_graficos = st.sidebar.checkbox('Mostrar gráficos das respostas')
#lê arquivo json com as respostas
dados = pd.read_json('./arquivos/respostasJSON_atualizado.json')
mostra_num_resp=False
if checkbox_mostrar_tabela:
    st.write('<h2 style="'+estilo_titulo_tabela_css+'"> Tabela</h2>',unsafe_allow_html=True)
    mostra_num_resp=True
    st.sidebar.markdown('## Linhas na tabela')
    qntd_linhas=st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value=1, max_value=len(dados),step=1)
    st.write(dados.head(qntd_linhas))
if checkbox_mostrar_graficos:
    mostra_num_resp=True
    #coloca as categorias para seleção
    st.sidebar.markdown('## Filtros para os gráficos')
    categorias = list(dados.keys())
    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar graficamente as respostas', options = categorias)
    st.write('<h2 style="'+estilo_titulo_grafico_css+'">'+categoria+'</h2>',unsafe_allow_html=True)
    #gera os gráficos
    if(categoria!='Problemas/Desconfortos num consultório'):
        checkbox_mostrar_analises=st.sidebar.checkbox('Mostrar gráficos relacionados')
        st.write(graficoPizza(dados, categoria))
        st.write(graficoBarra(dados,categoria))
        st.write("<hr/>",unsafe_allow_html=True)
        if checkbox_mostrar_analises:
            switch(dados,categoria)
    else:
        st.write('<span style="' + estilo_erro_css + '">Essa pergunta não possui gráficos associados!</span>', unsafe_allow_html=True)
if mostra_num_resp:
    st.write('<span style="'+estilo_info_css+'"> Nº de respostas: '+str(len(dados))+'</span>',unsafe_allow_html=True)
            
      
        
