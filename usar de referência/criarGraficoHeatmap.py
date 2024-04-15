import matplotlib.pyplot as plt #gráficos
import numpy as np #gráficos

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

path_img_temp='graficoPizza.png' #nome da imagem 
fig = plt.gcf() #guarda a imagem que está no plt
plt.show() #mostra a imagem que está no plt
fig.savefig(path_img_temp, format='png', dpi=200) #salva a imagem que está no plt