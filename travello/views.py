from django.shortcuts import render
from .models import Destination


# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 690

    dest2 = Destination()
    dest2.name = 'Gulistan'
    dest2.desc = 'The city of people'
    dest2.img = 'destination_2.jpg'
    dest2.price = 579

    dest3 = Destination()
    dest3.name = 'Dhaka'
    dest3.desc = 'The city of worst everything'
    dest3.img = 'destination_3.jpg'
    dest3.price = 987

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests})

  
