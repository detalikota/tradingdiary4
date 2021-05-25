from django.shortcuts import render
from .models import Trades

def home(request):
    x = Trades.objects.all().values_list("priceB","priceS")
    array = []
    for i in x:
        y = i[0] + i[1]
        array.append(y)
        #z = Trades.objects.create(name='test')

    context = {
        'trades': Trades.objects.all(),
        'z': array,
    }
    return render(request, 'main/home.html', context)