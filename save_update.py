import sqlite3


def save_update(level):
    db = sqlite3.connect('commit.db')
    cur = db.cursor()
    cur.execute(f"""UPDATE savepoint
                    SET max_level = {level}
                    WHERE max_level > 0 """)
    db.commit()
    db.close()