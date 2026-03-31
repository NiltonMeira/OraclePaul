import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_FOOTBALL_KEY")

headers = {
    "x-apisports-key": API_KEY
}

BASE_URL = "https://v3.football.api-sports.io"


def get_fixtures(league_id, season):

    url = f"{BASE_URL}/fixtures"

    params = {
        "league": league_id,
        "season": season
    }

    response = requests.get(url, headers=headers, params=params)

    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    return response.json()