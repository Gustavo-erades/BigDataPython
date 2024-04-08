import pandas as pd #type:ignore
csv_data = pd.read_csv("Cópia de Formulário de satisfação geral.csv", sep=",")
csv_data.to_json("test3.json", orient="columns")
--------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_json('test3.json')

#vamos contar o total de contas
total_contas = len(data)
print(f'Número de respostas totais: {total_contas}')

respostas=data['6. Já experimentou algum problema ou desconforto que te fez buscar outro consultório odontológico? Se sim, qual?']
for resposta in respostas:
  print(f"{resposta}\n")
opcao1=0
opcao2=0
opcao3=0
opcao4=0
respostasGrafico=data["4. O que você mais valoriza em um consultório odontológico?"]
for respostaGrafico in respostasGrafico:
  if(respostaGrafico=="Experiência do dentista"):
    opcao1+=1
  elif(respostaGrafico=="Qualidade dos tratamentos"):
    opcao2+=1
  elif(respostaGrafico=="Atmosfera geral do consultório"):
    opcao3+=1
  else:
    opcao4+=1
valores=[opcao1, opcao2, opcao3, opcao4]
label=["opção 1", "opção 2", "opção 3", "outra"]
explode = (0, 0.1, 0, 0)

plt.pie(valores, labels=label, autopct='%1.2f%%',shadow=True,colors=['#3794DB','#042940','#9FC131'],explode=explode)

plt.show()


'''
#vamos analisar o total de contas verificadas
contas_verificadas = data['verified_account'].sum()
print(f'Número de contas verificadas: {contas_verificadas}')

#obter a diferença entre contas verificadas e o total de contas para saber as contas não verificadas

contas_nao_verificadas = total_contas - contas_verificadas
print(f'Total de contas não verificadas: {contas_nao_verificadas}')


#Cria uma lista com numero de contas verificadas e não verificadas

contas = [ contas_verificadas, contas_nao_verificadas ]

rotulos = ['Verificados', 'Não verificados']

#criar um gráfico de pizza

plt.pie(contas, labels=rotulos, autopct='%1.2f%%')
plt.title('Contas verificadas e Não verificadas')
plt.show()
'''