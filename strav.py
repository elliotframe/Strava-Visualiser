import urllib3
import requests
import login

auth_url = 'https://www.strava.com/oauth/token'
base_url = 'https://www.strava.com/api/v3/athlete/'
activities_url = base_url + 'activities'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

payload = {
    'client_id': f'{login.client_id}',
    'client_secret': f'{login.client_secret}',
    'refresh_token': f'{login.refresh_token}',
    'grant_type': 'refresh_token',
    'f': 'json'
}

print('Requesting Token...\n')
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']

header = {'Authorization': 'Bearer ' + access_token}

page = 1
get_strava = requests.get(activities_url, headers=header, params={'per_page': 1, 'page': f'{page}'}).json()
print(get_strava[0]["name"])
get_strava = requests.get(base_url, headers=header).json()
print(get_strava)