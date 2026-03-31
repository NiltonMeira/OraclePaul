from app.database.connection import get_connection


def save_fixture(fixture):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO fixtures (
        fixture_id,
        league_id,
        season,
        home_team,
        away_team,
        home_goals,
        away_goals,
        match_date
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (fixture_id) DO NOTHING
    """

    cursor.execute(query, (
        fixture["fixture"]["id"],
        fixture["league"]["id"],
        fixture["league"]["season"],
        fixture["teams"]["home"]["name"],
        fixture["teams"]["away"]["name"],
        fixture["goals"]["home"],
        fixture["goals"]["away"],
        fixture["fixture"]["date"]
    ))

    conn.commit()
    cursor.close()
    conn.close()