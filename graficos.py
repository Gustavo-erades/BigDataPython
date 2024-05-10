import matplotlib.pyplot as plt 
import seaborn as sns 
from estilos import *
def graficoDispercao(dados):
    tempo_entrega = dados["O que mais é valorizado num consultório"]
    nota_satisfacao = dados["O que te afasta de um consultório"]
    plt.scatter(tempo_entrega, nota_satisfacao, color='b', edgecolors='black')
    plt.grid(True)
    fig = plt.gcf() 
    return fig
def graficoBarra(dados,col):
    graf_barras = sns.countplot(data=dados[col], palette=cores_grafico)
    graf_barras.set_facecolor('white')
    graf_barras.set(ylabel='')
    plt.xlabel('Quantidade de respostas')
    plt.grid(True)
    fig = plt.gcf()
    plt.close('all')
    return fig
def graficoPizza(dados, col):
    respostas = dados[col]
    lista = []
    for resposta in respostas:
        lista.append(resposta)
    listaLabel = list(set(lista))
    print(f"\tLISTA: {listaLabel}")
    opcoes = []
    for i in range(0, len(listaLabel)):
        opcoes.append(lista.count(lista[i]))
    print(f"\tOPÇÕES: {opcoes}")    
    values = opcoes
    label = listaLabel
    colors = cores_grafico
    pie = plt.pie(values, autopct='%1.2f%%', shadow=False, colors=colors)
    plt.legend(pie[0], label, loc="lower center")
    fig = plt.gcf()
    plt.close('all')
    return fig
