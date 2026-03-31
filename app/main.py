from app.api.api_client import get_fixtures
from app.services.match_service import save_fixtures


def run():

    league_id = 71  # Brasileirão
    season = 2010

    data = get_fixtures(league_id, season)

    fixtures = data.get("response", [])

    if not fixtures:
        print("Nenhum jogo retornado da API")
        return

    save_fixtures(fixtures)

    print(f"{len(fixtures)} jogos processados com sucesso!")


if __name__ == "__main__":
    run()