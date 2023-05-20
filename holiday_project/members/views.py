from decimal import Decimal
from django.shortcuts import render
from members.models import *
from datetime import datetime, timedelta
import csv

def index(request):
  return render(request, 'index.html')

def hotel_setup(request):
  csvreader = csv.reader(open("hotels.csv", 'r', errors="ignore"))
  bool = False
  for row in csvreader:
    if bool:
      row = row[0].split(";")
      print(row[0])
      h = Hotel(hotelid=int(row[0]), hotelname=row[1], hotelstars=row[2][:1])
      h.save()
    else:
      bool = True
  return render(request, 'setup.html', context={'name': 'Hotel', 'elements': Hotel.objects.all().count()})

#def test_setup(request):
  #return render(request, 'setup.html', context={'name': 'Offers', 'elements': Offers.objects.all().count()})

def resp(request):
  requestList = (str(request).split('?')[1]).split('&')
  #print(requestList)
  
  #parsing the request parameters
  days = requestList[0].split('=')[1]
  firstDate = requestList[1].split('=')[1]
  secondDate = requestList[2].split('=')[1]
  realFirstDate = datetime.strptime(firstDate[2:], '%y-%m-%d').date()
  realSecondDate = datetime.strptime(secondDate[2:], '%y-%m-%d').date()
  if (realSecondDate - realFirstDate).days < int(days):
    return render(request, 'index.html')
  airports = requestList[3].split('=')[1].split("%2C+")
  countAdults = requestList[4].split('=')[1].split('+')[0]
  countChildren = requestList[4].split('=')[1].split('+')[2]
  
  #searching for the records matching the parameters
  offers = []
  for i in range(0,len(airports)):
    if airports[i] == "AMS":
      temp = offerAMS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "BER":
      temp = offerBER.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "BLL":
      temp = offerBLL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "BRE":
      temp = offerBRE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "BRN":
      temp = offerBRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "BRU":
      temp = offerBRU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "BSL":
      temp = offerBSL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "CGN":
      temp = offerCGN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "CRL":
      temp = offerCRL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "CSO":
      temp = offerCSO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "DRS":
      temp = offerDRS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "DTM":
      temp = offerDTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "DUS":
      temp = offerDUS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "EIN":
      temp = offerEIN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "ERF":
      temp = offerERF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "FDH":
      temp = offerFDH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "FKB":
      temp = offerFKB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "FMM":
      temp = offerFMM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "FMO":
      temp = offerFMO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "FRA":
      temp = offerFRA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "GRZ":
      temp = offerGRZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "GVA":
      temp = offerGVA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "GWT":
      temp = offerGWT.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "HAJ":
      temp = offerHAJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "HAM":
      temp = offerHAM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "HHN":
      temp = offerHHH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "INN":
      temp = offerINN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "KLU":
      temp = offerKLU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "KRK":
      temp = offerKRK.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "KSF":
      temp = offerKSF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "LBC":
      temp = offerLBC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "LEJ":
      temp = offerLEJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "LNZ":
      temp = offerLNZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "LUX":
      temp = offerLUX.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "MUC":
      temp = offerMUC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "NRN":
      temp = offerNRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "NUE":
      temp = offerNUE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "BER":
      temp = offerBER.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "PAD":
      temp = offerPAD.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "PRG":
      temp = offerPRG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "RLG":
      temp = offerRLG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "RTM":
      temp = offerRTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "SCN":
      temp = offerSCN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "STR":
      temp = offerSTR.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "SXB":
      temp = offerSXB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "SZG":
      temp = offerSZG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "VIE":
      temp = offerVIE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "WAW":
      temp = offerWAW.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    elif airports[i] == "ZRH":
      temp = offerZRH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
      temp = temp[:1000]
      offers.append([temp])
    else:
      print("Airport not found")
      render(request, 'index.html')
  
  final_offers = []
  for temp in offers:
    for offer in temp[0]:
      final_offers.append(offer)
  #offers = offers[0:1000]
  offers = final_offers

  #map them
  temp_offers = []
  temp_offers2 = []
  for offer in offers:
    temp_offers = temp_offers + [offer]
    temp_offers2 = temp_offers2 + [first.objects.filter(id=offer.id)[0]]
  
  #temp_offers = temp_offers[0:100]
  n = len(temp_offers)
  print(n)

  #sorting them according to the lowest price
  for i in range(0,n):
    for h in range(i,n):
      if temp_offers2[i].price > temp_offers2[h].price:
        temp = temp_offers[i]
        temp_offers[i] = temp_offers[h]
        temp_offers[h] = temp
        temp = temp_offers2[i]
        temp_offers2[i] = temp_offers2[h]
        temp_offers2[h] = temp
  
  #check for duplicates and remove them
  ids = []
  n2 = 20
  if len(temp_offers) < 20:
    n2 = len(temp_offers)
  for i in range(0,n2):
    if temp_offers[i].hotelid not in ids:
      ids.append(temp_offers[i].hotelid)
    else:
      for h in range(i,n-1):
        temp_offers[h] = temp_offers[h+1]
      n = n-1
      if n < n2:
        n2 = n2-1

  #taking the best 20 records and put them together with their matching hotel into a list
  offers = temp_offers[0:20]
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
  offers = []
  for i in range(0,len(airports)):
    if airports[i] == "AMS":
      temp = offerAMS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "BER":
      temp = offerBER.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "BLL":
      temp = offerBLL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "BRE":
      temp = offerBRE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "BRN":
      temp = offerBRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "BRU":
      temp = offerBRU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "BSL":
      temp = offerBSL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "CGN":
      temp = offerCGN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "CRL":
      temp = offerCRL.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "CSO":
      temp = offerCSO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "DRS":
      temp = offerDRS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "DTM":
      temp = offerDTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "DUS":
      temp = offerDUS.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "EIN":
      temp = offerEIN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "ERF":
      temp = offerERF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "FDH":
      temp = offerFDH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "FKB":
      temp = offerFKB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "FMM":
      temp = offerFMM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "FMO":
      temp = offerFMO.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "FRA":
      temp = offerFRA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "GRZ":
      temp = offerGRZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "GVA":
      temp = offerGVA.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "GWT":
      temp = offerGWT.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "HAJ":
      temp = offerHAJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "HAM":
      temp = offerHAM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "HHN":
      temp = offerHHH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "INN":
      temp = offerINN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "KLU":
      temp = offerKLU.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "KRK":
      temp = offerKRK.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "KSF":
      temp = offerKSF.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "LBC":
      temp = offerLBC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "LEJ":
      temp = offerLEJ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "LNZ":
      temp = offerLNZ.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "LUX":
      temp = offerLUX.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "MUC":
      temp = offerMUC.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "NRN":
      temp = offerNRN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "NUE":
      temp = offerNUE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "BER":
      temp = offerBER.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "PAD":
      temp = offerPAD.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "PRG":
      temp = offerPRG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "RLG":
      temp = offerRLG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "RTM":
      temp = offerRTM.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "SCN":
      temp = offerSCN.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "STR":
      temp = offerSTR.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "SXB":
      temp = offerSXB.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "SZG":
      temp = offerSZG.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "VIE":
      temp = offerVIE.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "WAW":
      temp = offerWAW.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    elif airports[i] == "ZRH":
      temp = offerZRH.objects.filter(countadults=countAdults, countchildren=countChildren, startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days, hotelid=hotelID)
      temp = temp[:10]
      offers.append([temp])
    else:
      print("Airport not found")
      render(request, 'index.html')
  
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
    tempList2 = str(temp_offers[i].inbounddeparturedatetime).split('-')
    tempList3 = str(temp_offers[i].outboundarrivaldatetime).split('-')
    tempList4 = str(temp_offers[i].inboundarrivaldatetime).split('-')
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
  print(offer_list)
  return render(request, 'result.html', context={'offer_list': offer_list, 'hotelname': hotel.hotelname, 'startdate': startDate, 'enddate': endDate})

def final(request):
  return render(request, 'final.html')