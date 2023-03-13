from django.shortcuts import render

def index(request):
  return render(request, 'index.html')

def resp(request):
  na = (str(request).split('?')[1])
  context = {'test_list': na[0:(len(na)-2)]}
  return render(request, 'response.html', context=context)