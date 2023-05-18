from django.shortcuts import render
from members.models import Offers, Hotel
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
      h = Hotel(hotelid=int(row[0]), hotelname=row[1], hotelstars=row[2])
      h.save()
    else:
      bool = True
  return render(request, 'setup.html', context={'name': 'Hotel', 'elements': Hotel.objects.all().count()})

def test_setup(request):
  return render(request, 'setup.html', context={'name': 'Offers', 'elements': Offers.objects.all().count()})

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
  offers = Offers.objects.none()
  for i in range(0,len(airports)):
    offers = offers | Offers.objects.filter(countadults=countAdults, countchildren=countChildren, outbounddepartureairport=airports[i], startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
  offers = offers[0:100]
  
  #moving them into a list to make it sortable
  temp_offers = []
  for offer in offers:
    temp_offers = temp_offers + [offer]
  
  n = 100
  if len(temp_offers) < 100:
    n = len(temp_offers)
  
  #sorting them according to the lowest price
  for i in range(0,n):
    for h in range(i,n):
      if temp_offers[i].price > temp_offers[h].price:
        temp = temp_offers[i]
        temp_offers[i] = temp_offers[h]
        temp_offers[h] = temp
  
  n2 = 20
  
  #check for duplicates and remove them
  ids = []
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
  temp_offers = temp_offers[0:20]
  offers_list = []
  for offer in temp_offers:
    offers_list = offers_list + [[offer,Hotel.objects.filter(hotelid=offer.hotelid)[0]]]
  
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
  offers = Offers.objects.none()
  for i in range(0,len(airports)):
    offers = offers | Offers.objects.filter(hotelid=hotelID, countadults=countAdults, countchildren=countChildren, outbounddepartureairport=airports[i], startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
  offers = offers[0:5]
  
  #parsing the results
  offer_list = []
  for offer in offers:
    #changing the datetime format to present it in a nicer way :)
    tempList1 = str(offer.outbounddeparturedatetime).split('-')
    tempList2 = str(offer.inbounddeparturedatetime).split('-')
    tempList3 = str(offer.outboundarrivaldatetime).split('-')
    tempList4 = str(offer.inboundarrivaldatetime).split('-')
    temp1 = (tempList1[2][:2] + '.' + tempList1[1] + '.' + tempList1[0])
    temp2 = (tempList2[2][:2] + '.' + tempList2[1] + '.' + tempList2[0])
    temp3 = (tempList3[2][:2] + '.' + tempList3[1] + '.' + tempList3[0])
    temp4 = (tempList4[2][:2] + '.' + tempList4[1] + '.' + tempList4[0])
    offer_list.append([temp1,tempList1[2][3:8],temp2,tempList2[2][3:8],temp3,tempList3[2][3:8],temp4,tempList4[2][3:8],offer.roomtype,offer.mealtype,offer.oceanview,offer.price,offer.outbounddepartureairport])
  hotel = Hotel.objects.filter(hotelid=hotelID)[0]
  firstDateList = firstDate.split('-')
  secondDateList = secondDate.split('-')
  startDate = (firstDateList[2] + '.' + firstDateList[1] + '.' + firstDateList[0])
  endDate = (secondDateList[2] + '.' + secondDateList[1] + '.' + secondDateList[0])
  return render(request, 'result.html', context={'offer_list': offer_list, 'hotelname': hotel.hotelname, 'startdate': startDate, 'enddate': endDate})

def final(request):
  return render(request, 'final.html')