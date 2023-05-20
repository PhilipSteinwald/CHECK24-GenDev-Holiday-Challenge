import csv

price = 0

csvreader = csv.reader(open("offers.csv", 'r', errors="ignore"))
next(csvreader)
i = 0
n = 0
for row in csvreader:
    if int(row[5]) > price:
        price = int(row[5])
    if i % 1000000 == 0:
        print(str(n*1) + "Mio.")
        n = n+1
    i = i+1

print(price)
# Ergebnis: 380160