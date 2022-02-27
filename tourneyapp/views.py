from django.shortcuts import render
from django.template import loader

from .models import Mapdata

def index(request):
    map_list = Mapdata.objects.all()
    template = loader.get_template('tourneyapp/index.html')
    context = {
        'map_list': map_list,
    }
    return render(request, 'tourneyapp/index.html', context)