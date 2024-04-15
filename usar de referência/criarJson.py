import pandas as pd #baixa a biblioteca


df = pd.read_csv('arquivo.csv') #lê o arquivo .csv que é baixado do goole
json_data = df.to_json(orient='records') #passa o .csv para json
with open('arquivo.json', 'w') as f:
    f.write(json_data) #salva o arquivo .json
