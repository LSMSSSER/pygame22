def get_score(n, name=None):
    import sqlite3
    con = sqlite3.connect('commit.db')
    cur = con.cursor()
    res = cur.execute(f'''SELECT * from record''').fetchall()
    for i in res:
        res[res.index(i)] = (i[0], i[n])
    con.close()
    res.sort(key=lambda z: z[1], reverse=True)
    if name is not None:
        for i in res:
            if name in i:
                return i
    return res[:10]