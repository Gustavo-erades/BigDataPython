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
def graficoPizza(dados, col):
    respostas = dados[col]
    lista = []
    for resposta in respostas:
        lista.append(resposta)
    label = list(set(lista))
    listaLabels=[]
    for i in range(0, len(lista)):
        for j in range(0, len(label)):
            if lista[i]==label[j]:
                rep= lista.count(label[j])
                if (rep==1):
                    listaLabels.append("outros")
                else:
                    listaLabels.append(lista[i])
    valuesLegenda=list(set(listaLabels))                  
    values=[]
    for i in range(0,len(valuesLegenda)):
        values.append(lista.count(valuesLegenda[i]))
    plt.pie(values,autopct='%.1f%%', shadow=False, colors=cores_grafico)
    plt.legend(valuesLegenda, loc="lower center")
    fig = plt.gcf()
    plt.close('all')
    return [fig, values, valuesLegenda]
def graficoPlotagem(dados, col):
    respostas = dados[col]
    lista = []
    for resposta in respostas:
        lista.append(resposta)
    label = list(set(lista))
    listaLabels=[]
    for i in range(0, len(lista)):
        for j in range(0, len(label)):
            if lista[i]==label[j]:
                rep= lista.count(label[j])
                if (rep==1):
                    listaLabels.append("outros")
                else:
                    listaLabels.append(lista[i])
    valuesLegenda=list(set(listaLabels))                  
    values=[]
    for i in range(0,len(valuesLegenda)):
        values.append(lista.count(valuesLegenda[i]))
    fig, ax = plt.subplots()
    ax.plot(values,valuesLegenda , color='red', linestyle='--', marker='o', label='dados')
    ax.set_xlabel('Quantidade de respostas')
    fig = plt.gcf()
    plt.close('all')
    return fig
