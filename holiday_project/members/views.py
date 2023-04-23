from django.shortcuts import render
from members.models import Offers, Hotel
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
  na = (str(request).split('?')[1])
  context = {'test_list': na[0:(len(na)-2)]}
  print(context)
  return render(request, 'response.html')

def test_result(request):
  print("Result")
  return render(request, 'result.html')

def test_final(request):
  print("Final")
  return render(request, 'final.html')