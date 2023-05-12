import csv

stars = []

csvreader = csv.reader(open("hotels.csv", 'r', errors="ignore"))
next(csvreader)

for row in csvreader:
    row = row[0].split(';')
    if row[2] not in stars:
        stars.append(row[2])

print(stars)
# Ergebnis:
# ['4.0', '3.0', '5.0', '1.0', '2.0', '0.0']