import matplotlib.pyplot as plt #gráficos

tempo_entrega = [25, 40, 30, 20, 35, 50, 15, 45, 55, 28, 33, 22, 38, 17, 42]
nota_satisfacao = [8, 6, 9, 7, 5, 4, 10, 6, 2, 9, 7, 8, 5, 10, 6]
plt.scatter(tempo_entrega, nota_satisfacao, color='b', edgecolors='black')
plt.title("Tempo de Entrega vs. Nota de Satisfação")
plt.xlabel("Tempo de Entrega (minutos)")
plt.ylabel("Nota de Satisfação")
plt.grid(True)
plt.show()

path_img_temp='graficoPizza.png' #nome da imagem 
fig = plt.gcf() #guarda a imagem que está no plt
plt.show() #mostra a imagem que está no plt
fig.savefig(path_img_temp, format='png', dpi=200) #salva a imagem que está no plt