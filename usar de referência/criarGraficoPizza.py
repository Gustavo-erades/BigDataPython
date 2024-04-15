import matplotlib.pyplot as plt #gráficos
import pandas as pd #mexer com os dados
fileName="arquivo.json"
df = pd.read_json('arquivo.json')
#criando gráfico de pizza 
print(f"Total de respostas: {len(df)}")
col='Resposta 4'
respostas=df[col]
lista=[]
for resposta in respostas:
    lista.append(resposta)
listaLabel=list(set(lista))
opcoes=[]
for i in range(0,len(listaLabel)):
    opcoes.append(lista.count(lista[i]))
values=opcoes
label=listaLabel
colors=['#E1002F','#007CDB','#E3BA14','#40DB9E']
explode = (0, 0, 0, 0)
plt.pie(values, labels=label, autopct='%1.2f%%', shadow=False, colors=colors, explode=explode)
plt.title(col)

path_img_temp='graficoPizza.png' #nome da imagem 
fig = plt.gcf() #guarda a imagem que está no plt
plt.show() #mostra a imagem que está no plt
fig.savefig(path_img_temp, format='png', dpi=200) #salva a imagem que está no plt