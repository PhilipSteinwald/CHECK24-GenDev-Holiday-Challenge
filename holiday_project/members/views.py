from django.shortcuts import render
from members.models import Offers, Hotel
from datetime import datetime, timedelta, timezone
import pytz
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

#tests
def test_setup(request):
  return render(request, 'setup.html', context={'name': 'Offers', 'elements': Offers.objects.all().count()})

def test_resp(request):
  requestList = (str(request).split('?')[1]).split('&')
  #print(requestList)
  days = requestList[0].split('=')[1]
  firstDate = requestList[1].split('=')[1]
  secondDate = requestList[2].split('=')[1]
  print(firstDate)
  realFirstDate = datetime.strptime(firstDate[2:], '%y-%m-%d').date()
  realSecondDate = datetime.strptime(secondDate[2:], '%y-%m-%d').date()
  if (realSecondDate - realFirstDate).days < int(days):
    return render(request, 'index.html')
  airports = requestList[3].split('=')[1].split("%2C+")
  countAdults = requestList[4].split('=')[1].split('+')[0]
  countChildren = requestList[4].split('=')[1].split('+')[2]
  offers = Offers.objects.none()
  for i in range(0,len(airports)):
    offers = offers | Offers.objects.filter(countadults=countAdults, countchildren=countChildren, outbounddepartureairport=airports[i], startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
  offers = offers[0:100]
  temp_offers = []
  for offer in offers:
    temp_offers = temp_offers + [offer]
  for i in range(0,100):
    for h in range(i,100):
      if temp_offers[i].price > temp_offers[h].price:
        temp = temp_offers[i]
        temp_offers[i] = temp_offers[h]
        temp_offers[h] = temp
  ids = []
  for i in range(0,19):
    if temp_offers[i].hotelid not in ids:
      ids.append(temp_offers[i].hotelid)
    else:
      for h in range(i,99):
        temp_offers[h] = temp_offers[h+1]
  temp_offers = temp_offers[0:19]
  offers_list = []
  for offer in temp_offers:
    offers_list = offers_list + [[offer,Hotel.objects.filter(hotelid=offer.hotelid)[0]]]
  #print(offers_list)
  return render(request, 'response.html', context={'offer_list': offers_list, 'days': days, 'firstDate': firstDate, 'secondDate': secondDate, 'airports': requestList[3].split('=')[1], 'persons': requestList[4].split('=')[1]})

def test_result(request):
  requestList = (str(request).split('?')[1]).split('&')
  print(requestList)
  hotelID = requestList[0].split('=')[1]
  days = requestList[1].split('=')[1]
  firstDate = requestList[2].split('=')[1]
  secondDate = requestList[3].split('=')[1]
  realFirstDate = datetime.strptime(firstDate[2:], '%y-%m-%d').date()
  realSecondDate = datetime.strptime(secondDate[2:], '%y-%m-%d').date()
  airports = requestList[4].split('=')[1].split("%252C%2B")
  countAdults = requestList[5].split('=')[1].split('%2B')[0]
  countChildren = requestList[5].split('=')[1].split('%2B')[2]
  offers = Offers.objects.none()
  for i in range(0,len(airports)):
    offers = offers | Offers.objects.filter(hotelid=hotelID, countadults=countAdults, countchildren=countChildren, outbounddepartureairport=airports[i], startdate__range=[realFirstDate,(realSecondDate - timedelta(days=int(days)))], days=days)
  offers = offers[0:5]
  offer_list = []
  for offer in offers:
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
  print(offers)
  return render(request, 'result.html', context={'offer_list': offer_list, 'hotelname': hotel.hotelname, 'startdate': startDate, 'enddate': endDate})

def test_final(request):
  print("Final")
  return render(request, 'final.html')