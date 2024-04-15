from openpyxl import Workbook #planilhas
from openpyxl.drawing.image import Image #planilhas
from openpyxl import Workbook #planilhas
from openpyxl.drawing.image import Image #planilhas

workbook = Workbook() #cria um workbook
sheet = workbook.active #seleciona a planilha ativa no workbook (por padrão é 'sheet')
sheet['A1'] = 'Nome' #colocando dados aleatótirios (só de teste)
sheet['B1'] = 'Idade'
sheet['A2'] = 'João'
sheet['B2'] = 30
sheet['A3'] = 'Maria'
sheet['B3'] = 25
img = Image("caminho de alguma imagem.png")
sheet.add_image(img, 'F2')
workbook.save(filename='exemplo.xlsx')