import matplotlib.pyplot as plt #gráficos
from openpyxl import Workbook #planilhas
from openpyxl.drawing.image import Image #planilhas
import pandas as pd #mexer com os dados

fileName="teste3.json"
df = pd.read_json('teste3.json')
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

path_img_temp='teste200.png'
fig = plt.gcf()
plt.show()
fig.savefig('teste200.png', format='png', dpi=200)

workbook = Workbook()
sheet = workbook.active
img = Image(path_img_temp)
sheet.add_image(img, 'F2')
workbook.save(filename='exemplo.xlsx')