import matplotlib.pyplot as plt #gráficos
import pandas as pd #mexer com os dados
import matplotlib.pyplot as plt #gráficos
import pandas as pd #mexer com os dados
import seaborn as sns #gráficos
fileName="arquivo.json"
df = pd.read_json('arquivo.json')
col='Resposta 4' #uma coluna qualquer, ou seja, uma chave qualquer do arquivo.json
#criando gráfico de barra
plt.figure(figsize=(10, 6))
sns.countplot(x=col, data=df, color='#007CDB')
plt.ylabel('quantidade de respostas')
plt.xlabel(col)
plt.title('Quantidade de respostas X respostas')
plt.grid(True)
plt.show()
#esse código comentado abaixo faz a mesma coisa, mas o de cima pareceu mais correto (se usar o código abaixo tem que verificar a lógica para evitar erros.)
'''
plt.bar(listaLabel, values, color='#007CDB')
plt.xlabel(col)
plt.ylabel('quantidade de respostas')
plt.title('Quantidade de respostas X respostas')
plt.grid(True)
plt.show()
'''
path_img_temp='graficoBarra.png' #nome da imagem 
fig = plt.gcf() #guarda a imagem que está no plt
plt.show() #mostra a imagem que está no plt
fig.savefig(path_img_temp, format='png', dpi=200) #salva a imagem que está no plt