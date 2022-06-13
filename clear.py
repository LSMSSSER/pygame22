def dell():
    import sqlite3
    con = sqlite3.connect('commit.db')
    cur = con.cursor()
    res = cur.execute(f'''DELETE from record''').fetchall()
    con.commit()
    con.close()
