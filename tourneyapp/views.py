from django.shortcuts import render
from django.template import loader
import requests
from os import getenv
from dotenv import load_dotenv
from .forms import MapDataForm
from django.http import HttpResponseRedirect

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

def get_map_info(data):
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
    beatmmap_title = beatmapset_full['beatmapset']['artist'] + " - " + beatmapset_full['beatmapset']['title'] + " [" + beatmapset_full['version']+ "]" + " (" + beatmapset_full['beatmapset']['creator'] + ")"
    beatmapset_data = [beatmapset_full['difficulty_rating'], beatmapset_full['bpm'], time_string,
                    beatmapset_full['cs'], beatmapset_full['ar'], beatmapset_full['accuracy'], beatmapset_full['id'], beatmmap_title]
    #print(beatmapset_full['beatmapset']['covers']['card'])
    return(beatmapset_data)

def convert_to_hr(beatmap_data):
    return None

def convert_to_dt(beatmap_data):
    return None

def index(request):
    template = loader.get_template('tourneyapp/index.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        nm1_response = ""
        nm2_response = ""
        nm3_response = ""
        nm4_response = ""
        nm5_response = ""
        nm6_response = ""
        # HD
        hd1_response = ""
        hd2_response = ""
        hd3_response = ""
        # HR
        hr1_response = ""
        hr2_response = ""
        hr3_response = ""
        # DT
        dt1_response = ""
        dt2_response = ""
        dt3_response = ""
        dt4_response = ""
        # FM
        fm1_response = ""
        fm2_response = ""
        fm3_response = ""
        # TB
        tb_response = ""

        # create a form instance and populate it with data from the request:
        mapform = MapDataForm(request.POST)
        # check whether it's valid:
        if mapform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # NM
            nm1_link = mapform.cleaned_data['nm1_link']
            nm2_link = mapform.cleaned_data['nm2_link']
            nm3_link = mapform.cleaned_data['nm3_link']
            nm4_link = mapform.cleaned_data['nm4_link']
            nm5_link = mapform.cleaned_data['nm5_link']
            nm6_link = mapform.cleaned_data['nm6_link']
            # HD
            hd1_link = mapform.cleaned_data['hd1_link']
            hd2_link = mapform.cleaned_data['hd2_link']
            hd3_link = mapform.cleaned_data['hd3_link']
            # HR
            hr1_link = mapform.cleaned_data['hr1_link']
            hr2_link = mapform.cleaned_data['hr2_link']
            hr3_link = mapform.cleaned_data['hr3_link']
            # DT
            dt1_link = mapform.cleaned_data['dt1_link']
            dt2_link = mapform.cleaned_data['dt2_link']
            dt3_link = mapform.cleaned_data['dt3_link']
            dt4_link = mapform.cleaned_data['dt4_link']
            # FM
            fm1_link = mapform.cleaned_data['fm1_link']
            fm2_link = mapform.cleaned_data['fm2_link']
            fm3_link = mapform.cleaned_data['fm3_link']
            # TB
            tb_link = mapform.cleaned_data['tb_link']
            
        try:
            # NM
            if nm1_link != "":
                nm1_response = get_map_info(nm1_link)
            if nm2_link != "":
                nm2_response = get_map_info(nm2_link)
            if nm3_link != "":
                nm3_response = get_map_info(nm3_link)
            if nm4_link != "":
                nm4_response = get_map_info(nm4_link)
            if nm5_link != "":
                nm5_response = get_map_info(nm5_link)
            if nm6_link != "":
                nm6_response = get_map_info(nm6_link)
            # HD
            if hd1_link != "":
                hd1_response = get_map_info(hd1_link)
            if hd2_link != "":
                hd2_response = get_map_info(hd2_link)
            if hd3_link != "":
                hd3_response = get_map_info(hd3_link)
            # HR
            if hr1_link != "":
                hr1_response = get_map_info(hr1_link)
            if hr2_link != "":
                hr2_response = get_map_info(hr2_link)
            if hr3_link != "":
                hr3_response = get_map_info(hr3_link)
            # DT
            if dt1_link != "":
                dt1_response = get_map_info(dt1_link)
            if dt2_link != "":
                dt2_response = get_map_info(dt2_link)
            if dt3_link != "":
                dt3_response = get_map_info(dt3_link)
            if dt4_link != "":
                dt4_response = get_map_info(dt4_link)
            # FM
            if fm1_link != "":
                fm1_response = get_map_info(fm1_link)
            if fm2_link != "":
                fm2_response = get_map_info(fm2_link)
            if fm3_link != "":
                fm3_response = get_map_info(fm3_link)
            # TB
            if tb_link != "":
                tb_response = get_map_info(tb_link)
            
            context = {
                # NM
                'nm1': nm1_response,
                'nm2': nm2_response,
                'nm3': nm3_response,
                'nm4': nm4_response,
                'nm5': nm5_response,
                'nm6': nm6_response,
                # HD
                'hd1': hd1_response,
                'hd2': hd2_response,
                'hd3': hd3_response,
                # HR
                'hr1': hr1_response,
                'hr2': hr2_response,
                'hr3': hr3_response,
                # DT
                'dt1': dt1_response,
                'dt2': dt2_response,
                'dt3': dt3_response,
                'dt4': dt4_response,
                # FM
                'fm1': fm1_response,
                'fm2': fm2_response,
                'fm3': fm3_response,
                # TB
                'tb': tb_response,
                'form': mapform,
            }
        except Exception as e:
            print("whoopsie")
        return render(request, 'tourneyapp/test.html')
    # if a GET (or any other method) we'll create a blank form
    else:
        mapform = MapDataForm()
        context = {
            # NM
            'nm1': "",
            'nm2': "",
            'nm3': "",
            'nm4': "",
            'nm5': "",
            'nm6': "",
            # HD
            'hd1': "",
            'hd2': "",
            'hd3': "",
            # HR
            'hr1': "",
            'hr2': "",
            'hr3': "",
            # DT
            'dt1': "",
            'dt2': "",
            'dt3': "",
            'dt4': "",
            # FM
            'fm1': "",
            'fm2': "",
            'fm3': "",
            # TB
            'tb': "",
            'form': mapform,
        }
        return render(request, 'tourneyapp/index.html', context)
