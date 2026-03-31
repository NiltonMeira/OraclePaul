from app.api.api_client import get_fixtures
from app.services.match_service import save_fixture


def run():

    league_id = 71  # Brasileirão
    season = 2024

    data = get_fixtures(league_id, season)

    fixtures = data["response"]

    for fixture in fixtures:
        save_fixture(fixture)

    print("Dados salvos com sucesso!")


if __name__ == "__main__":
    run()