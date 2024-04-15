# importanto da bibliotecas que serão usadas
import matplotlib.pyplot as plt #gráficos
from openpyxl import Workbook #planilhas
from openpyxl.drawing.image import Image #planilhas
import pandas as pd #mexer com os dados
import seaborn as sns #gráficos
import numpy as np #gráficos
'''
- csv-->json-->xls-->análise das planilhas e elaboração de relatórios
- primeiro, seleciona o arquivo .csv baixado das respostas do google
- segundo, traduz esse arquivo em formato json e altera os nomes para melhorar a análise
- terceiro, elabora gráficos, faz cálculos e adiquire todos os dados para a análise
- quarto, transforma tudo em uma planilha do excel que conterá todo o resultado
'''
#alterando nome das perguntas para facilitar a construção das colunas no excel e retirando a coluna referente a data de preenchimento
fileName="teste3.json"
df = pd.read_json('teste3.json')
'''
novas_keys={
    'Banana 1':"Resposta 1", 
    "Banana 2":'Resposta 2',
    "Banana 3":"Resposta 3",
    "4. O que você mais valoriza em um consultório odontológico?":"Resposta 4",
    "5. Quais canais de comunicação você prefere para agendar consultas ou receber informações do consultório?":"Resposta 5",
    "6. Já experimentou algum problema ou desconforto que te fez buscar outro consultório odontológico? Se sim, qual?":"Resposta 6",
    "7.  Qual das formas de pagamento abaixo deveriam ser obrigatoriamente oferecidas pelo consultório odontológico como opção?":"Resposta 7",
    "8.  Na sua opinião, o que mais te afastaria de um consultório e te levaria a buscar outro atendimento odontológico?":"Resposta 8"
}
df.rename(columns=novas_keys, inplace=True)
df=df.drop("Carimbo de data/hora", axis=1)
df.to_json(fileName, orient='records')
'''
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
plt.show()
#criando gráfico de barras
plt.figure(figsize=(10, 6))
sns.countplot(x=col, data=df, color='#007CDB')
plt.ylabel('quantidade de respostas')
plt.xlabel(col)
plt.title('Quantidade de respostas X respostas')
plt.grid(True)
plt.show()
'''
plt.bar(listaLabel, values, color='#007CDB')
plt.xlabel(col)
plt.ylabel('quantidade de respostas')
plt.title('Quantidade de respostas X respostas')
plt.grid(True)
plt.show()
'''
#criando gráfico de histograma
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
vendas = [55, 70, 40, 85, 60, 90, 75]
plt.figure(figsize=(8, 6))
plt.hist(vendas, bins=10, edgecolor='black')
plt.xticks(range(10, 101, 10))
plt.title("Quantidade de Vendas Diárias")
plt.xlabel("Quantidade de Vendas")
plt.ylabel("Frequência")
plt.show()
#criando gráfico de dispersão
tempo_entrega = [25, 40, 30, 20, 35, 50, 15, 45, 55, 28, 33, 22, 38, 17, 42]
nota_satisfacao = [8, 6, 9, 7, 5, 4, 10, 6, 2, 9, 7, 8, 5, 10, 6]
plt.scatter(tempo_entrega, nota_satisfacao, color='b', edgecolors='black')
plt.title("Tempo de Entrega vs. Nota de Satisfação")
plt.xlabel("Tempo de Entrega (minutos)")
plt.ylabel("Nota de Satisfação")
plt.grid(True)
plt.show()
#criando gráfico heatmap
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
pratos = ['Pizza', 'Hambúrguer', 'Sushi', 'Salada', 'Massa', 'Churrasco', 'Sobremesa']
satisfacao = np.array([
[4, 5, 3, 4, 5, 4, 3],
[3, 4, 4, 3, 5, 4, 4],
[5, 5, 5, 4, 3, 5, 5],
[4, 3, 4, 3, 4, 3, 4],
[3, 4, 3, 4, 3, 4, 3],
[5, 4, 5, 5, 4, 5, 4],
[4, 3, 4, 4, 3, 4, 4]
])
plt.figure(figsize=(8, 6))
plt.imshow(satisfacao, cmap='coolwarm', aspect='auto')
plt.title("Satisfação do Cliente por Prato e Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Prato")
plt.xticks(np.arange(len(dias_semana)), dias_semana)
plt.yticks(np.arange(len(pratos)), pratos)
plt.colorbar(label='Satisfação')
plt.show()

#criando planilha

# Crie um objeto Workbook
workbook = Workbook()
# Selecione a planilha ativa (padrão é 'Sheet')
sheet = workbook.active
# Adicione dados às células
sheet['A1'] = 'Nome'
sheet['B1'] = 'Idade'
sheet['A2'] = 'João'
sheet['B2'] = 30
sheet['A3'] = 'Maria'
sheet['B3'] = 25
# Inserir uma imagem
img = Image('caminho/para/sua/imagem.jpg')
sheet.add_image(img, 'C1')
# Salve o arquivo
workbook.save(filename='exemplo.xlsx')
#criando gráficos numa planilha (talves seja melhor?)
'''
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# Crie um objeto Workbook
workbook = Workbook()

# Selecione a planilha ativa (padrão é 'Sheet')
sheet = workbook.active

# Adicione dados às células
sheet['A1'] = 'Nome'
sheet['B1'] = 'Vendas'
sheet['A2'] = 'Produto A'
sheet['B2'] = 100
sheet['A3'] = 'Produto B'
sheet['B3'] = 150
sheet['A4'] = 'Produto C'
sheet['B4'] = 200

# Crie um objeto de referência para os dados
data = Reference(sheet, min_col=2, min_row=1, max_col=2, max_row=4)

# Crie um objeto de referência para as categorias
categories = Reference(sheet, min_col=1, min_row=2, max_row=4)

# Crie um objeto de gráfico de barras
chart = BarChart()

# Adicione os dados ao gráfico
chart.add_data(data, titles_from_data=True)

# Adicione as categorias ao gráfico
chart.set_categories(categories)

# Defina o título do gráfico
chart.title = 'Vendas por Produto'

# Adicione o gráfico à planilha
sheet.add_chart(chart, "D1")

# Salve o arquivo
workbook.save(filename='exemplo_com_grafico.xlsx')
'''
#fim
