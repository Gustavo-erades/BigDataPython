import matplotlib.pyplot as plt 
import seaborn as sns 
from estilos import *
def graficoDispercao(dados,colx,coly):
    plt.scatter(dados[colx], dados[coly], color='red', edgecolors='red')
    plt.grid(True)
    fig = plt.gcf() 
    plt.close('all')
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
def graficoPizza(dados, col): #ERRO AQUI, AJUSTAR CÁLCULO
    respostas = dados[col]
    lista = []
    for resposta in respostas:
        lista.append(resposta)
    listaLabel = list(set(lista))
    print(f"\tLISTA: {listaLabel}")
    listaLabel2=[]
    j=len(listaLabel)-1
    for i in reversed(listaLabel):
        listaLabel2.append(listaLabel[j])
        j-=1
    print(f"\tLISTA 2: {listaLabel2}")
    opcoes = []
    for i in range(0, len(listaLabel2)):
        opcoes.append(lista.count(lista[i]))
    print(f"\tOPÇÕES: {opcoes}")    
    values = opcoes
    label = listaLabel2
    colors = cores_grafico
    pie = plt.pie(values, autopct='%1.2f%%', shadow=False, colors=colors)
    plt.legend(pie[0], label, loc="lower center")
    fig = plt.gcf()
    plt.close('all')
    return fig
