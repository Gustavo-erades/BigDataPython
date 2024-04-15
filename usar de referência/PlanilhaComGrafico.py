#criando gráficos numa planilha, eu achei mais complicado, mas podemos usar também. Isso cria a planilha e cria um gráfico lá dentro já.
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