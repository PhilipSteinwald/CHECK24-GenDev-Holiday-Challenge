import csv

csvreader = csv.reader(open("offers.csv", 'r'))
csvwriter = csv.writer(open("testOffers.csv", 'w', newline=''))
firstLine = next(csvreader)
firstLine.insert(0,'id')
csvwriter.writerow(firstLine)

i = 0
n = 0
# extracting each data row one by one
for row in csvreader:
    row.insert(0,str(i))
    # writing the data rows
    csvwriter.writerow(row)
    if i % 1000000 == 0:
        print(str(n*1) + "Mio.")
        n = n+1
    i = i+1