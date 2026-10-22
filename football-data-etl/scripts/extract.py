import requests

def fetch_serie_a_matches(api_token: str):
    url = "https://api.football-data.org/v4/competitions/SA/matches"
    headers = {"X-Auth-Token": api_token}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['matches']
    else:
        raise Exception(f"Errore nel recupero dati: {response.status_code}")