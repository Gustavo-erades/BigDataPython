import streamlit as st 
import pandas as pd
from graficos import *
from estilos import *
from trocaGrafDispercao import *
st.title('Análise das respostas com python')
st.write('<h6 style="'+titulo_css+'">Os gráficos representam as respostas no formulário de satisfação geral</h6>',unsafe_allow_html=True) 
checkbox_mostrar_tabela=st.sidebar.checkbox('Mostrar tabela')
checkbox_mostrar_graficos = st.sidebar.checkbox('Mostrar gráficos das respostas')
texto_sobre="Análise gráfica das respostas do formulário de satisfação em consultórios odontológicos no geral. O formulário ficou disponibilizado ao público durante o primeiro semestre de 2024."
#lê arquivo json com as respostas
dados = pd.read_json('./arquivos/respostasJSON_atualizado.json')
mostra_num_resp=False
num_resp=len(dados)
if checkbox_mostrar_tabela:
    st.write('<h3 style="'+estilo_titulo_tabela_css+'"> Tabela</h3>',unsafe_allow_html=True)
    mostra_num_resp=True
    st.sidebar.markdown('## Linhas na tabela')
    qntd_linhas=st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value=1, max_value=len(dados),step=1)
    st.write(dados.head(qntd_linhas))
    st.write('<span style="'+estilo_info_css+'">'+str(qntd_linhas)+' Linhas</span>',unsafe_allow_html=True)
if checkbox_mostrar_graficos:
    mostra_num_resp=True
    #coloca as categorias para seleção
    st.sidebar.markdown('## Filtros para os gráficos')
    categorias = list(dados.keys())
    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar graficamente as respostas', options = categorias)
    st.write('<h3 style="'+estilo_titulo_grafico_css+'">'+categoria+'</h3>',unsafe_allow_html=True)
    #gera os gráficos
    if(categoria!='Problemas/Desconfortos num consultório'):
        checkbox_mostrar_analises=st.sidebar.checkbox('Mostrar gráficos relacionados')
        grafPizza=graficoPizza(dados, categoria)
        st.write(grafPizza[0])
        st.write("<hr>",unsafe_allow_html=True)
        st.write("<ul>",unsafe_allow_html=True)
        for i in range(0, len(grafPizza[2])):
            if(grafPizza[1][i]!=0):
                st.write("<li>"+grafPizza[2][i]+": "+str(grafPizza[1][i])+" respostas</li>",unsafe_allow_html=True)
        st.write("<ul>",unsafe_allow_html=True)
        st.write(graficoPlotagem(dados, categoria))
        st.write("<hr>",unsafe_allow_html=True)
        st.write(graficoBarra(dados,categoria))
        st.write("<hr/>",unsafe_allow_html=True)
        if checkbox_mostrar_analises:
            switch(dados,categoria)
    else:
        #exibindo pergunta 6
        st.write('<ul>',unsafe_allow_html=True)
        num_resp=0
        num_prob=0
        for resposta in dados[categoria]:
            if(resposta!=None):
                if(len(resposta)>4) or resposta=='Sim':
                    st.write('<li>'+str(resposta)+'</li>',unsafe_allow_html=True)
                    num_prob+=1
                num_resp+=1
        st.write("</ul",unsafe_allow_html=True)
        st.write("<hr>",unsafe_allow_html=True)
        st.write('<h4> '+str(num_prob)+' pessoas informaram já ter tido problemas</h4>',unsafe_allow_html=True)
        st.write("<hr>",unsafe_allow_html=True)
        st.write('<h3 style="'+estilo_titulo_grafico_css+'">Problemas informados:</h3>',unsafe_allow_html=True)
        st.write("<ul>",unsafe_allow_html=True)
        for resposta in dados[categoria]:
            if (resposta!=None) and (len(resposta)>4):
                st.write('<li>'+resposta+'</li>',unsafe_allow_html=True)
        st.write("</ul>",unsafe_allow_html=True)
        st.write("<hr>",unsafe_allow_html=True)
        st.write('<span style="' + estilo_erro_css + '">Essa pergunta não possui gráficos associados!</span>', unsafe_allow_html=True)
if mostra_num_resp:
    st.write('<span style="'+estilo_info_css+'"> Nº de respostas: '+str(num_resp)+'</span>',unsafe_allow_html=True)
st.sidebar.html("<h1 style='"+styleTituloSobre+"'>sobre</h1>")
st.sidebar.html("<div style='"+styleDivSobre+"'><p style='"+styleConteudoSobre+"'>"+texto_sobre+"</p></div>")
      
        
