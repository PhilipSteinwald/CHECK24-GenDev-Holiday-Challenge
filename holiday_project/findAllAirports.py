import csv

airports = []

csvreader = csv.reader(open("offers.csv", 'r'))
next(csvreader)
i = 0
n = 0
for row in csvreader:
    if row[10] not in airports:
        airports.append(row[10])
    if i % 1000000 == 0:
        print(str(n*1) + "Mio.")
        n = n+1
    i = i+1

print(airports)
# Ergebnis:
# ['FMO', 'STR', 'HAM', 'LEJ', 'NUE', 'CGN', 'FRA', 'PAD', 'HAJ', 'BER', 'FMM', 'DUS', 'SCN', 'DRS', 'BRE', 'DTM', 'MUC', 'VIE', 'NRN', 'BSL', 'HHN', 'FKB', 'ZRH', 'SZG', 'LUX', 'AMS', 'PRG', 'FDH', 'INN', 'KSF', 'LNZ', 'EIN', 'SXB', 'BLL', 'LBC', 'BRU', 'GRZ', 'GWT', 'CRL', 'CSO', 'WAW', 'GVA', 'ERF', 'KRK', 'BRN', 'RLG', 'KLU', 'RTM']