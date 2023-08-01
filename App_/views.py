from django.shortcuts import render

# Create your views here.
def converter(request):
    num = int(request.POST['num'])
    binval = bin(num)
    return render(request, 'converter.html', {'binval':binval})
def index(request):
    return render(request, 'index.html' )
