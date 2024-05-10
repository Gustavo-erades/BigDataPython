import streamlit as st 
import pandas as pd
from graficoPizza import *
from estilos import *
st.title('Análise das respostas com python')
st.write('<h6 style="'+titulo_css+'">Os gráficos abaixo representam de maneira gráfica as respostas no formulário de satisfação geral</h6>',unsafe_allow_html=True)
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
#lê arquivo json com as respostas
dados = pd.read_json('./arquivos/respostasJSON_atualizado.json')
if checkbox_mostrar_tabela:
    #coloca as categorias para seleção
    st.sidebar.markdown('## Filtros para os gráficos')
    categorias = list(dados.keys())
    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico de pizza', options = categorias)
    st.write(f"## {categoria}")
    #gera os gráficos
    if(categoria!='Problemas/Desconfortos num consultório'):
        st.write(graficoPizza(dados, categoria))
    else:
        st.write('<span style="' + estilo_erro_css + '">Essa pergunta não possui um gráfico de pizza associado!</span>', unsafe_allow_html=True)
    st.write('<span style="'+estilo_info_css+'"> Nº de respostas: '+str(len(dados))+'</span>',unsafe_allow_html=True)
    
        
      
        
