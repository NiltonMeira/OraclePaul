from app.database.connection import get_connection
from psycopg2.extras import execute_batch


def save_fixtures(fixtures):

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

    values = []

    for fixture in fixtures:
        values.append((
            fixture["fixture"]["id"],
            fixture["league"]["id"],
            fixture["league"]["season"],
            fixture["teams"]["home"]["name"],
            fixture["teams"]["away"]["name"],
            fixture["goals"]["home"],
            fixture["goals"]["away"],
            fixture["fixture"]["date"]
        ))

    execute_batch(cursor, query, values)

    conn.commit()
    cursor.close()
    conn.close()