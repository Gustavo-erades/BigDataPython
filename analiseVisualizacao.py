import streamlit as st 
import pandas as pd
from graficos import *
from estilos import *
st.title('Análise das respostas com python')
st.write('<h6 style="'+titulo_css+'">Os gráficos abaixo representam de maneira gráfica as respostas no formulário de satisfação geral</h6>',unsafe_allow_html=True)
checkbox_mostrar_tabela=st.sidebar.checkbox('Mostrar tabela')
checkbox_mostrar_graficos = st.sidebar.checkbox('Mostrar gráficos das respostas')
#lê arquivo json com as respostas
dados = pd.read_json('./arquivos/respostasJSON_atualizado.json')
mostra_num_resp=False
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
            categoriasGraficoDispercao = list(dados.keys())
            categoriaDispercao = st.sidebar.selectbox('Selecione a categoria para relacionar as respostas', options = categoriasGraficoDispercao)
            st.write( '<h2 style="' + estilo_relacao_css + '">'+categoriaDispercao+' X '+categoria+'</h2>', unsafe_allow_html=True)
            st.write(graficoDispercao(dados,categoriaDispercao,categoria))
    else:
        st.write('<span style="' + estilo_erro_css + '">Essa pergunta não possui gráficos associados!</span>', unsafe_allow_html=True)
if mostra_num_resp:
    st.write('<span style="'+estilo_info_css+'"> Nº de respostas: '+str(len(dados))+'</span>',unsafe_allow_html=True)
            
      
        
