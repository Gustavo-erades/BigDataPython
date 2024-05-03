import pandas as pd 
from openpyxl import Workbook
df_csv = pd.read_csv('./arquivos/respostasCSV.csv') 
json_data = df_csv.to_json(orient='records')
with open('./arquivos/respostasJSON.json', 'w') as f:
    f.write(json_data)
fileName="respostasJSON.json"
df_json = pd.read_json('./arquivos/'+fileName)
novas_keys={
    "1. O que você considera mais importante ao escolher um consultório odontológico para atendimento?":"Mais importante num consultório", 
    "2. Quais fatores mais influenciam sua decisão de retornar ao mesmo consultório odontológico para tratamentos futuros?":"Por que voltar a um consultório", 
    "3. Que serviços adicionais ou comodidades você gostaria de ver sendo oferecidos em consultórios odontológicos para melhorar sua experiência?":"Como melhorar um consultório",
    "4. O que você mais valoriza em um consultório odontológico?":"O que mais é valorizado num consultório",
    "5. Quais canais de comunicação você prefere para agendar consultas ou receber informações do consultório?":"Melhores canais de comunicação",
    "6. Já experimentou algum problema ou desconforto que te fez buscar outro consultório odontológico? Se sim, qual?":"Problemas/Desconfortos num consultório",
    "7.  Qual das formas de pagamento abaixo deveriam ser obrigatoriamente oferecidas pelo consultório odontológico como opção?":"Melhores formas de pagamento",
    "8.  Na sua opinião, o que mais te afastaria de um consultório e te levaria a buscar outro atendimento odontológico?":"O que te afasta de um consultório",
    "9. Como conheceu os consultórios odontológicos nos quais já foi ou é atendido(a)":"Como conhecer um consultório",
}
df_json.rename(columns=novas_keys, inplace=True) 
df_json=df_json.drop("Carimbo de data/hora", axis=1)
df_json.to_json('./arquivos/respostasJSON_atualizado.json', orient='records')
workbook=Workbook()
sheet=workbook.active
sheet['A1']="Mais importante num consultório"
sheet['B1']="Por que voltar a um consultório"
sheet['C1']="Como melhorar um consultório"
sheet['D1']="O que mais é valorizado num consultório"
sheet['E1']="Melhores canais de comnunicação"
sheet['F1']="Problemas/Desconfortos num consultório"
sheet['G1']="Melhores formas de pagamento"
sheet['H1']="O que te afasta de um consultório"
sheet['I1']="Como conhecer um consultório"
workbook.save('./arquivos/formularioGeral_respostas.xlsx')
df_json_atualizado = pd.read_json('./arquivos/respostasJSON_atualizado.json')
planilha_existente = pd.read_excel('./arquivos/formularioGeral_respostas.xlsx')
planilha_atualizada = pd.concat([planilha_existente,df_json_atualizado ], ignore_index=False)
nome_arquivo_atualizado = 'formularioGeral_respostasAtualizado.xlsx'
planilha_atualizada.to_excel('./arquivos/'+nome_arquivo_atualizado, index=False)
print(f'Dados adicionados com sucesso em {nome_arquivo_atualizado}')