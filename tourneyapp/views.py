from django.shortcuts import render
from django.template import loader
import requests
from pprint import pprint
from os import getenv
from dotenv import load_dotenv

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

def getMapInfo():
    token = get_token()

    beatmap = 'https://osu.ppy.sh/beatmapsets/352570#osu/786018'
    map_id = beatmap[beatmap.rfind('/')+1:]
    print(map_id)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    params = {
    }

    # response = requests.get(f'{API_URL}/beatmaps/'+map_id, params=params, headers=headers)
    response = requests.get(f'{API_URL}/beatmaps/'+map_id, params=params, headers=headers)
    
    beatmapset_data = response.json()

    # pprint(beatmapset_data, indent=2)
    return(beatmapset_data['beatmapset']['creator'])

def index(request):
    map_list = Mapdata.objects.all()
    template = loader.get_template('tourneyapp/index.html')
    context = {
        'map_list': map_list,
        'getMapInfo': getMapInfo,
    }
    return render(request, 'tourneyapp/index.html', context)