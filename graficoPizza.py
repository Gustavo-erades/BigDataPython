import matplotlib.pyplot as plt 
from estilos import *
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
    return fig
