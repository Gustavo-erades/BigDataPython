import matplotlib.pyplot as plt 
import seaborn as sns 
from estilos import *
def graficoDispercao(dados,colx,coly):
    print(dados)
    print("*******************")
    print(colx)
    print("*******************")
    print(coly)
    plt.scatter(dados[colx], dados[coly], color='red', edgecolors='red')
    plt.grid(True)
    fig = plt.gcf() 
    plt.close('all')
    return fig
def graficoBarra(dados,col):
    respostas = dados[col]
    lista = []
    for resposta in respostas:
        lista.append(resposta)
    label = list(set(lista))
    listaLabels=[]
    for i in range(0, len(lista)):
        print(f"primeiro loop for nº{i}")
        for j in range(0, len(label)):
            print(f"segundo loop for nº{j}")
            if lista[i]==label[j]:
                print(f"{lista[i]} é igual a {label[j]}, portanto vai entrar na variável rep para a condição")
                rep= lista.count(label[j])
                if (rep>1):
                    listaLabels.append(lista[i])
    graf_barras = sns.countplot(data=listaLabels, palette=cores_grafico)
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
    print(f"array lista: {lista}\narray label: {label}")
    for i in range(0, len(lista)):
        print(f"primeiro loop for nº{i}")
        for j in range(0, len(label)):
            print(f"segundo loop for nº{j}")
            if lista[i]==label[j]:
                print(f"{lista[i]} é igual a {label[j]}, portanto vai entrar na variável rep para a condição")
                lista.count(label[j])
                '''
                if (rep<=1):
                    print("Vai entrar na listaLabels como 'outros' ")
                    listaLabels.append("outros")
                else:
                '''
                print("Vai entrar na listaLabels normalmente")
                listaLabels.append(lista[i])
    print(f"listaLabels:{listaLabels}")
    valuesLegenda=list(set(listaLabels)) 
    print(f"valuesLegenda: {valuesLegenda}")                 
    values=[]
    #variável global --> cores | contar a quantidade de vezes que passa pelo loop e pela condição
    for i in range(0,len(valuesLegenda)):
        values.append(lista.count(valuesLegenda[i]))
    print(f"quantidade de 'outros' nas respostas {valuesLegenda.count('outros')}")
    plt.pie(values,autopct='%.1f%%', shadow=False, colors=cores_grafico)
    plt.legend(valuesLegenda, loc="lower center")
    fig = plt.gcf()
    plt.close('all'),
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
    ax.grid(True, color='gray', linewidth=0.5)
    ax.set_xlabel('Quantidade de respostas')
    fig = plt.gcf()
    plt.close('all')
    return fig
