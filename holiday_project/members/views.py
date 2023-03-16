from django.shortcuts import render
from members.models import Offers

def index(request):
  return render(request, 'index.html')

def resp(request):
  na = (str(request).split('?')[1])
  context = {'test_list': na[0:(len(na)-2)]}
  return render(request, 'response.html', context=context)

def test_setup(request):
  p = Offers(hotelid='90', depaturedate='2022-10-05T09:30:00+02:00', returndate='2022-10-12T08:35:00+02:00', countadults='1', countchildren='1', price='1243', inbounddepartureairport='PMI', inboundarrivalairport='DUS', inboundairline='LH', inboundarrivaldatetime='2022-10-12T14:40:00+02:00', outbounddepartureairport='DUS', outboundarrivalairport='PMI', outboundairline='LH', outboundarrivaldatetime='2022-10-05T14:25:00+02:00', mealtype='halfboard', oceanview='False', roomtype='double')
  p.save()