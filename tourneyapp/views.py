from django.shortcuts import render
from django.template import loader
import requests
from os import getenv
from dotenv import load_dotenv
from .forms import MapDataForm
from django.http import HttpResponseRedirect

from .models import Mapdata

API_URL = 'https://osu.ppy.sh/api/v2'
TOKEN_URL = 'https://osu.ppy.sh/oauth/token'
load_dotenv()

def get_token():
    data = {
        'client_id': getenv('CLIENT_ID'),
        'client_secret': getenv('CLIENT_SECRET'),
        'grant_type': 'client_credentials',
        'scope': 'public'
    }

    response = requests.post(TOKEN_URL, data=data)

    return response.json().get('access_token')

def getMapInfo(data):
    token = get_token()

    # beatmap = 'https://osu.ppy.sh/beatmapsets/352570#osu/786018'
    beatmap = data
    if beatmap is None:
        return None
    map_id = beatmap[beatmap.rfind('/')+1:]

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    params = {
    }

    # response = requests.get(f'{API_URL}/beatmaps/'+map_id, params=params, headers=headers)
    response = requests.get(f'{API_URL}/beatmaps/'+map_id, params=params, headers=headers)
    
    beatmapset_full = response.json()

    m, s = divmod(beatmapset_full['total_length'], 60)
    time_string = '{:02d}:{:02d}'.format(m, s)
    beatmapset_data = [beatmapset_full['difficulty_rating'], beatmapset_full['bpm'], time_string,
                    beatmapset_full['cs'], beatmapset_full['ar'], beatmapset_full['accuracy'], beatmapset_full['id']]
    return(beatmapset_data)

def index(request):
    template = loader.get_template('tourneyapp/index.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        nm1_response = ""
        nm2_response = ""
        # create a form instance and populate it with data from the request:
        mapform = MapDataForm(request.POST)
        # check whether it's valid:
        if mapform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            nm1_link = mapform.cleaned_data['nm1_link']
            nm2_link = mapform.cleaned_data['nm2_link']
        try:
            if nm1_link != "":
                nm1_response = getMapInfo(nm1_link)
            if nm2_link != "":
                nm2_response = getMapInfo(nm2_link)
        except Exception as e:
            print("whoopsie")
    # if a GET (or any other method) we'll create a blank form
    else:
        mapform = MapDataForm()
        nm1_response = ""
        nm2_response = ""
    context = {
        'nm1': nm1_response,
        'nm2': nm2_response,
        'form': mapform,
    }
    return render(request, 'tourneyapp/index.html', context)
