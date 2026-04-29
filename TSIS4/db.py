import psycopg2

DB_NAME = "snake_db"
USER = "postgres"
PASSWORD = "your_password"
HOST = "localhost"

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST
    )

def get_or_create_player(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    player = cur.fetchone()

    if player:
        player_id = player[0]
    else:
        cur.execute("INSERT INTO players (username) VALUES (%s) RETURNING id", (username,))
        player_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return player_id


def save_game(player_id, score, level):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO game_sessions (player_id, score, level_reached)
        VALUES (%s, %s, %s)
    """, (player_id, score, level))

    conn.commit()
    cur.close()
    conn.close()


def get_top10():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON p.id = g.player_id
        ORDER BY g.score DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def get_personal_best(player_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT MAX(score) FROM game_sessions WHERE player_id=%s
    """, (player_id,))

    result = cur.fetchone()[0]
    cur.close()
    conn.close()

    return result if result else 0