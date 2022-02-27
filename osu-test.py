import requests
from pprint import pprint
from os import getenv
from dotenv import load_dotenv


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

def main():
    token = get_token()

    beatmap = input("please enter the beatmap link from osu.ppy.sh: ")
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

    pprint(beatmapset_data, indent=2)


if __name__ == '__main__':
    main()