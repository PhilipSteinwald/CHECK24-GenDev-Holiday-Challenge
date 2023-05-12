from datetime import datetime, timedelta, timezone
import csv

csvreader = csv.reader(open("offers.csv", 'r'))
csvwriter = csv.writer(open("newTestOffers.csv", 'w', newline=''))
firstLine = next(csvreader)
firstLine.insert(0,'id')
firstLine.append('startdate')
firstLine.append('enddate')
firstLine.append('days')
csvwriter.writerow(firstLine)

i = 0
n = 0
# extracting each data row one by one
for row in csvreader:
    row.insert(0,str(i))
    row.append(row[2][:10])
    row.append(row[3][:10])
    row.append((datetime.strptime(row[3][2:10], '%y-%m-%d').date() - datetime.strptime(row[2][2:10], '%y-%m-%d').date()).days)
    csvwriter.writerow(row)
    if i % 1000000 == 0:
        print(str(n*1) + "Mio.")
        n = n+1
    i = i+1