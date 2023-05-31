from decimal import Decimal
from django.shortcuts import render
from members.models import *
from datetime import datetime, timedelta
import csv

def index(request):
  return render(request, 'index.html')

def resp(request):
  requestList = (str(request).split('?')[1]).split('&')
  
  #parsing the request parameters
  days = requestList[0].split('=')[1]
  firstDate = requestList[1].split('=')[1]
  secondDate = requestList[2].split('=')[1]
  if firstDate.split('-')[0] != '2023' or firstDate.split('-')[0] != '2023':
    return render(request, 'error.html', context={'msg': "Es konnten keine Ergebnisse für diese Daten gefunden werden!"})
  realFirstDate = datetime.strptime(firstDate[2:], '%y-%m-%d').date()
  realSecondDate = datetime.strptime(secondDate[2:], '%y-%m-%d').date()
  if (realSecondDate - realFirstDate).days < int(days):
    return render(request, 'error.html', context={'msg': "Der gewählte Zeitraum ist zu klein für die gewünschte Anzahl an Tagen!"})
  airports = requestList[3].split('=')[1].split("%2C+")
  countAdults = requestList[4].split('=')[1].split('+')[0]
  countChildren = requestList[4].split('=')[1].split('+')[2]
  
  #searching for the records matching the parameters
  max = 50
  if len(airports) == 2:
    max = 30
  elif len(airports) == 3:
    max = 25
  elif len(airports) > 3:
    max = 20
  offers = []
  for i in range(0,len(airports)):
    if airports[i] == "AMS":
      offers.append([offerAMS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "BER":
      offers.append([offerBER.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "BLL":
      offers.append([offerBLL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "BRE":
      offers.append([offerBRE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "BRN":
      offers.append([offerBRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "BRU":
      offers.append([offerBRU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "BSL":
      offers.append([offerBSL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "CGN":
      offers.append([offerCGN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "CRL":
      offers.append([offerCRL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "CSO":
      offers.append([offerCSO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "DRS":
      offers.append([offerDRS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "DTM":
      offers.append([offerDTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "DUS":
      offers.append([offerDUS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "EIN":
      offers.append([offerEIN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "ERF":
      offers.append([offerERF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "FDH":
      offers.append([offerFDH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "FKB":
      offers.append([offerFKB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "FMM":
      offers.append([offerFMM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "FMO":
      offers.append([offerFMO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "FRA":
      offers.append([offerFRA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "GRZ":
      offers.append([offerGRZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "GVA":
      offers.append([offerGVA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "GWT":
      offers.append([offerGWT.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "HAJ":
      offers.append([offerHAJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "HAM":
      offers.append([offerHAM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "HHN":
      offers.append([offerHHH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "INN":
      offers.append([offerINN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "KLU":
      offers.append([offerKLU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "KRK":
      offers.append([offerKRK.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "KSF":
      offers.append([offerKSF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "LBC":
      offers.append([offerLBC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "LEJ":
      offers.append([offerLEJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "LNZ":
      offers.append([offerLNZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "LUX":
      offers.append([offerLUX.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "MUC":
      offers.append([offerMUC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "NRN":
      offers.append([offerNRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "NUE":
      offers.append([offerNUE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "PAD":
      offers.append([offerPAD.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "PRG":
      offers.append([offerPRG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "RLG":
      offers.append([offerRLG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "RTM":
      offers.append([offerRTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "SCN":
      offers.append([offerSCN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "STR":
      offers.append([offerSTR.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "SXB":
      offers.append([offerSXB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "SZG":
      offers.append([offerSZG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "VIE":
      offers.append([offerVIE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "WAW":
      offers.append([offerWAW.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    elif airports[i] == "ZRH":
      offers.append([offerZRH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)[:max]])
    else:
      print("Airport not found")
      return render(request, 'error.html', context={'msg': "Flughafen konnte nicht gefunden werden!"})
  
  final_offers = []
  for temp in offers:
    for offer in temp[0]:
      final_offers.append(offer)
  temp_offers = final_offers
  
  n = len(temp_offers)
  print(n)

  if n == 0:
    print("No Offers found")
    return render(request, 'error.html', context={'msg': "Für diese Suche konnten keine Ergebnisse gefunden werden!"})

  #sorting them according to the lowest price
  for i in range(0,n):
    for h in range(i,n):
      if temp_offers[i].price > temp_offers[h].price:
        temp = temp_offers[i]
        temp_offers[i] = temp_offers[h]
        temp_offers[h] = temp
  
  #check for duplicates and ignore them
  ids = []
  offers = []
  n2 = 20
  i = 0
  if len(temp_offers) < 20:
    n2 = len(temp_offers)
  while n2 > 0:
    if temp_offers[i].hotelid not in ids:
      ids.append(temp_offers[i].hotelid)
      offers.append(temp_offers[i])
      n = n-1
      n2 = n2-1
    else:
      n = n-1
      if n < n2:
        n2 = n2-1
    i = i+1

  #taking the best 20 records and put them together with their matching hotel into a list
  offers = offers[0:20]
  offers_list = []
  for offer in offers:
    offers_list = offers_list + [[first.objects.get(id=offer.id),Hotel.objects.filter(hotelid=offer.hotelid)[0]]]
  
  return render(request, 'response.html', context={'offer_list': offers_list, 'days': days, 'firstDate': firstDate, 'secondDate': secondDate, 'airports': requestList[3].split('=')[1], 'persons': requestList[4].split('=')[1]})

def result(request):
  requestList = (str(request).split('?')[1]).split('&')
  
  #parsing the request parameters
  hotelID = requestList[0].split('=')[1]
  days = requestList[1].split('=')[1]
  firstDate = requestList[2].split('=')[1]
  secondDate = requestList[3].split('=')[1]
  realFirstDate = datetime.strptime(firstDate[2:], '%y-%m-%d').date()
  realSecondDate = datetime.strptime(secondDate[2:], '%y-%m-%d').date()
  airports = requestList[4].split('=')[1].split("%252C%2B")
  countAdults = requestList[5].split('=')[1].split('%2B')[0]
  countChildren = requestList[5].split('=')[1].split('%2B')[2]
  
  #searching for the records matching the parameters
  #offers = Offers.objects.none()
  max = 10
  if len(airports) == 2:
    max = 5
  elif len(airports) == 3:
    max = 4
  elif len(airports) == 4:
    max = 3
  elif len(airports) > 4:
    max = 2
  offers = []
  for i in range(0,len(airports)):
    if airports[i] == "AMS":
      offers.append([offerAMS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "BER":
      offers.append([offerBER.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "BLL":
      offers.append([offerBLL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "BRE":
      offers.append([offerBRE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "BRN":
      offers.append([offerBRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "BRU":
      offers.append([offerBRU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "BSL":
      offers.append([offerBSL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "CGN":
      offers.append([offerCGN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "CRL":
      offers.append([offerCRL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "CSO":
      offers.append([offerCSO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "DRS":
      offers.append([offerDRS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "DTM":
      offers.append([offerDTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "DUS":
      offers.append([offerDUS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "EIN":
      offers.append([offerEIN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "ERF":
      offers.append([offerERF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "FDH":
      offers.append([offerFDH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "FKB":
      offers.append([offerFKB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "FMM":
      offers.append([offerFMM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "FMO":
      offers.append([offerFMO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "FRA":
      offers.append([offerFRA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "GRZ":
      offers.append([offerGRZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "GVA":
      offers.append([offerGVA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "GWT":
      offers.append([offerGWT.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "HAJ":
      offers.append([offerHAJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "HAM":
      offers.append([offerHAM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "HHN":
      offers.append([offerHHH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "INN":
      offers.append([offerINN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "KLU":
      offers.append([offerKLU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "KRK":
      offers.append([offerKRK.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "KSF":
      offers.append([offerKSF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "LBC":
      offers.append([offerLBC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "LEJ":
      offers.append([offerLEJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "LNZ":
      offers.append([offerLNZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "LUX":
      offers.append([offerLUX.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "MUC":
      offers.append([offerMUC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "NRN":
      offers.append([offerNRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "NUE":
      offers.append([offerNUE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "PAD":
      offers.append([offerPAD.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "PRG":
      offers.append([offerPRG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "RLG":
      offers.append([offerRLG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "RTM":
      offers.append([offerRTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "SCN":
      offers.append([offerSCN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "STR":
      offers.append([offerSTR.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "SXB":
      offers.append([offerSXB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "SZG":
      offers.append([offerSZG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "VIE":
      offers.append([offerVIE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "WAW":
      offers.append([offerWAW.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    elif airports[i] == "ZRH":
      offers.append([offerZRH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)[:max]])
    else:
      print("Airport not found")
      return render(request, 'error.html', context={'msg': "Flughafen konnte nicht gefunden werden!"})
  
  final_offers = []
  for temp in offers:
    for offer in temp[0]:
      final_offers.append(offer)
  #offers = offers[0:5]
  offers = final_offers

  #map them
  temp_offers = []
  for offer in offers:
    temp_offers = temp_offers + [second.objects.get(id=offer.id)]
  
  n = len(offers)
  print(n)

  #sorting them according to the lowest price
  for i in range(0,n):
    for h in range(i,n):
      if temp_offers[i].price > temp_offers[h].price:
        temp = temp_offers[i]
        temp_offers[i] = temp_offers[h]
        temp_offers[h] = temp
        temp = offers[i]
        offers[i] = offers[h]
        offers[h] = temp

  #parsing the results
  offer_list = []
  for i in range(0,len(offers)):
    #changing the datetime format to present it in a nicer way :)
    tempList1 = str(temp_offers[i].outbounddeparturedatetime).split('-')
    tempList2 = str(temp_offers[i].inboundarrivaldatetime).split('-')
    tempList3 = str(temp_offers[i].outboundarrivaldatetime).split('-')
    tempList4 = str(temp_offers[i].inbounddeparturedatetime).split('-')
    temp1 = (tempList1[2][:2] + '.' + tempList1[1] + '.' + tempList1[0])
    temp2 = (tempList2[2][:2] + '.' + tempList2[1] + '.' + tempList2[0])
    temp3 = (tempList3[2][:2] + '.' + tempList3[1] + '.' + tempList3[0])
    temp4 = (tempList4[2][:2] + '.' + tempList4[1] + '.' + tempList4[0])
    offer_list.append([temp1,tempList1[2][3:8],temp2,tempList2[2][3:8],temp3,tempList3[2][3:8],temp4,tempList4[2][3:8],temp_offers[i].roomtype,temp_offers[i].mealtype,temp_offers[i].oceanview,temp_offers[i].price,str(offers[i])[5:8]])
  hotel = Hotel.objects.filter(hotelid=hotelID)[0]
  firstDateList = firstDate.split('-')
  secondDateList = secondDate.split('-')
  startDate = (firstDateList[2] + '.' + firstDateList[1] + '.' + firstDateList[0])
  endDate = (secondDateList[2] + '.' + secondDateList[1] + '.' + secondDateList[0])
  #print(offer_list)
  return render(request, 'result.html', context={'offer_list': offer_list, 'hotelname': hotel.hotelname, 'startdate': startDate, 'enddate': endDate})

def final(request):
  return render(request, 'final.html')