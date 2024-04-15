import matplotlib.pyplot as plt #gráficos

dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
vendas = [55, 70, 40, 85, 60, 90, 75]
plt.figure(figsize=(8, 6))
plt.hist(vendas, bins=10, edgecolor='black')
plt.xticks(range(10, 101, 10))
plt.title("Quantidade de Vendas Diárias")
plt.xlabel("Quantidade de Vendas")
plt.ylabel("Frequência")
plt.show()

path_img_temp='graficoHistograma.png' #nome da imagem 
fig = plt.gcf() #guarda a imagem que está no plt
plt.show() #mostra a imagem que está no plt
fig.savefig(path_img_temp, format='png', dpi=200) #salva a imagem que está no plt