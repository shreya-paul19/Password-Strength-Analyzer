import sqlite3

def create_db():

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER,
            strength TEXT,
            entropy REAL
        )
    ''')

    conn.commit()
    conn.close()


def save_result(score, strength, entropy):

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO history
        (score, strength, entropy)
        VALUES (?, ?, ?)
        ''',
        (score, strength, entropy)
    )

    conn.commit()
    conn.close()


def get_statistics():

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM history")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE strength='Weak'"
    )
    weak = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE strength='Medium'"
    )
    medium = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM history WHERE strength='Strong'"
    )
    strong = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "weak": weak,
        "medium": medium,
        "strong": strong
    }