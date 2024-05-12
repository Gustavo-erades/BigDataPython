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
    print(f"\tLISTA: {lista}")
    opcoes = []
    for i in range(0, len(lista)):
        opcoes.append(lista.count(lista[i]))
        print("****************\n")
        print(str(opcoes)+"\n")
        print("****************\n")
    print(f"\tOPÇÕES: {opcoes}")    
    values = list(set(opcoes))
    print(values)
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
    teste=list(set(listaLabels))
    print(f"TAMANHO:{len(values)}")
    if (len(values)>3):
        cores=cores_grafico_tam4
    else:
        cores=cores_grafico_tam3
    pie = plt.pie(values,autopct='%.1f%%', shadow=False, colors=cores)
    #plt.legend(pie[0], teste, loc="lower center")
    fig = plt.gcf()
    plt.close('all')
    return fig
