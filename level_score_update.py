import sqlite3


def level_score_update(number_of_level, hs):
    con = sqlite3.connect('commit.db')
    cur = con.cursor()

    gg = cur.execute(f"""UPDATE films
                        SET highest_score = {hs}
                        WHERE id = {number_of_level}""")
    con.commit()
    con.close()
