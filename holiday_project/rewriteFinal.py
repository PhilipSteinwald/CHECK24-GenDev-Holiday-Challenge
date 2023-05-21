from datetime import datetime, timedelta, timezone
import csv

csvreader = csv.reader(open("offers.csv", 'r'))
csvwriterFirst = csv.writer(open("first.csv", 'w', newline=''))
csvwriterSecond = csv.writer(open("second.csv", 'w', newline=''))
next(csvreader)

firstLine = ["id","countadults","countchildren","startdate","days","hotelid","price"]
csvwriterFirst.writerow(["id","mealtype","oceanview","roomtype","price"])
csvwriterSecond.writerow(["id","mealtype","oceanview","roomtype","price","outbounddeparturedatetime","inbounddeparturedatetime","outboundarrivaldatetime","inboundarrivaldatetime"])

airports = []
offers = []

i = 0
n = 0
# extracting each data row one by one
for row in csvreader:
    meal = 9
    if row[12] == "NONE":
        meal = 0
    elif row[12] == "BREAKFAST":
        meal = 1
    elif row[12] == "HALFBOARD":
        meal = 2
    elif row[12] == "HALFBOARDPLUS":
        meal = 3
    elif row[12] == "FULLBOARD":
        meal = 4
    elif row[12] == "FULLBOARDPLUS":
        meal = 5
    elif row[12] == "ALLINCLUSIVE":
        meal = 6
    elif row[12] == "ALLINCLUSIVEPLUS":
        meal = 7
    elif row[12] == "ACCORDINGDESCRIPTION":
        meal = 8
    else:
        print(row)
    room = 99
    if row[14] == "ACCORDINGDESCRIPTION":
        room = 0
    elif row[14] == "SINGLE":
        room = 1
    elif row[14] == "DOUBLE":
        room = 2
    elif row[14] == "TRIPLE":
        room = 3
    elif row[14] == "FOURBEDROOM":
        room = 4
    elif row[14] == "JUNIORSUITE":
        room = 5
    elif row[14] == "SUITE":
        room = 6
    elif row[14] == "APARTMENT":
        room = 7
    elif row[14] == "STUDIO":
        room = 8
    elif row[14] == "SUPERIOR":
        room = 9
    elif row[14] == "ECONOMY":
        room = 10
    elif row[14] == "FAMILY":
        room = 11
    elif row[14] == "BUNGALOW":
        room = 12
    elif row[14] == "DELUXE":
        room = 13
    elif row[14] == "MULTISHARE":
        room = 14
    elif row[14] == "TWINROOM":
        room = 15
    elif row[14] == "VILLA":
        room = 16
    elif row[14] == "HOLIDAYHOUSE":
        room = 17
    elif row[14] == "DUPLEX":
        room = 18
    else:
        print(row)
    csvwriterFirst.writerow([str(i),meal,row[13],room,row[5]])
    csvwriterSecond.writerow([str(i),meal,row[13],room,row[5],row[1],row[2],row[11],row[8]])
    if row[10] not in airports:
        airports.append(row[10])
        temp = csv.writer(open(("offer" + row[10] + ".csv"), 'w', newline=''))
        temp.writerow(firstLine)
        offers.append([row[10],temp])
    for offer in offers:
        if offer[0] == row[10]:
            offer[1].writerow([str(i),row[3],row[4],row[1][:10],(datetime.strptime(row[2][2:10], '%y-%m-%d').date() - datetime.strptime(row[1][2:10], '%y-%m-%d').date()).days,row[0],row[5]])
    if i % 1000000 == 0:
        print(str(n*1) + "Mio.")
        n = n+1
    i = i+1


#['316', '2023-07-19T06:00:00+00:00', '2023-07-28T09:30:00+00:00', '2', '2', '4648', 'PMI', 'PMI', '2023-07-28T12:05:00+00:00', 'HAJ', 'HAJ', '2023-07-19T08:30:00+00:00', 'ALLINCLUSIVE', 'false', 'FAMILY']