import csv 
filename="grandesMestres.csv"
header=("Nome", "Rating", "Nacionalidade")
data=[
    ("Magnus Carlsen", 2985, "Noruega"),
    ("Ian Nepominiatch", 2885, "Rússia"),
    ("Ding Liren", 2880, "China"),
    ("Fabiano Caruana", 2976, "Estados Unidos")
]
def writer(header, data, filename):
    with open(filename, "w+", newline="") as csvfile:
        dt=csv.writer(csvfile)
        dt.writerow(header)
        for line in data:
            dt.writerow(line)
writer(header, data, filename)
        