# importanto da bibliotecas que serão usadas
import pandas as pd #mexer com os dados
'''
- csv-->json-->xlsx-->análise das planilhas e elaboração de relatórios
- primeiro, seleciona o arquivo .csv baixado das respostas do google
- segundo, traduz esse arquivo em formato json e altera os nomes para melhorar a análise
- terceiro, elabora gráficos, faz cálculos e adiquire todos os dados para a análise
- quarto, transforma tudo em uma planilha do excel que conterá todo o resultado
'''
#alterando nome das perguntas para facilitar a construção das colunas no excel e retirando a coluna referente a data de preenchimento
fileName="arquivo.json"
df = pd.read_json(fileName)
novas_keys={
    'Pergunta do formulário 1':"Novo titulo", 
    'Pergunta do formulário 2':"Novo titulo", 
    'Pergunta do formulário 3':"Novo titulo", 
}
df.rename(columns=novas_keys, inplace=True)
#tira o campo de data/hora que vem por padrão, para facilitar 
df=df.drop("Carimbo de data/hora", axis=1)
df.to_json(fileName, orient='records')