import pandas as pd #baixa a biblioteca
df = pd.read_csv('arquivo.csv') #lê o arquivo .csv que é baixado do goole
json_data = df.to_json(orient='records') #passa o .csv para json
with open('arquivo.json', 'w') as f:
    f.write(json_data) #salva o arquivo .json
#alterando nome das perguntas para facilitar a construção das colunas no excel 
#e retirando a coluna referente a data de preenchimento
fileName="arquivo.json"
df = pd.read_json(fileName)
novas_keys={
    '1. O que você considera mais importante ao escolher um consultório odontológico para atendimento?':"Mais importante num consultório", 
    '2. Quais fatores mais influenciam sua decisão de retornar ao mesmo consultório odontológico para tratamentos futuros?':"Por que voltar a um consultório", 
    '3. Que serviços adicionais ou comodidades você gostaria de ver sendo oferecidos em consultórios odontológicos para melhorar sua experiência':"Como melhorar um consultório",
    '4. O que você mais valoriza em um consultório odontológico?':'O que mais é valorizado num consultório',
    '5. Quais canais de comunicação você prefere para agendar consultas ou receber informações do consultório?':'Melhores canais de comnunicação',
    '6. Já experimentou algum problema ou desconforto que te fez buscar outro consultório odontológico? Se sim, qual?':'Problemas/Desconfortos num consultório',
    '7.  Qual das formas de pagamento abaixo deveriam ser obrigatoriamente oferecidas pelo consultório odontológico como opção':'Melhores formas de pagamento',
    '8.  Na sua opinião, o que mais te afastaria de um consultório e te levaria a buscar outro atendimento odontológico?':'O que te afasta de um consultório',
    '9. Como conheceu os consultórios odontológicos nos quais já foi ou é atendido(a)':'Como conhecer um consultório',
}
df.rename(columns=novas_keys, inplace=True)
#tira o campo de data/hora que vem por padrão, para facilitar 
df=df.drop("Carimbo de data/hora", axis=1)
df.to_json(fileName, orient='records')
