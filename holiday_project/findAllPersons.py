import csv

adults = []
children = []

csvreader = csv.reader(open("offers.csv", 'r', errors="ignore"))
next(csvreader)
i = 0
n = 0
for row in csvreader:
    if row[3] not in adults:
        adults.append(row[3])
    if row[4] not in children:
        children.append(row[4])
    if i % 1000000 == 0:
        print(str(n*1) + "Mio.")
        n = n+1
    i = i+1

print(adults)
# Ergebnis:
# ['2', '1', '3', '4', '6', '8', '10', '5', '9', '7', '12', '18', '15', '13', '20', '24', '11', '14', '16', '22', '17']
print()
print(children)
# Ergebnis:
# ['0', '1', '2', '3', '5', '4', '6', '18', '8', '9', '7']