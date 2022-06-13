def update(n, score, name):
    import sqlite3
    from get_score import get_score
    a = get_score(n, name)
    if str(a[1]) >= str(score):
        return
    n = str(n)
    con = sqlite3.connect('commit.db')
    cur = con.cursor()
    flag = False
    nm = cur.execute('''SELECT name FROM record''').fetchall()
    for i in nm:
        if name in i:
            flag = True
    if flag:
        res = cur.execute(f'''UPDATE record SET '{n}' = ? WHERE name = ?''', (score, name))
    else:
        res = cur.execute(f'''INSERT INTO record(name, '1', '2', '3', '4', 
        '5', '6', '7') VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (name, 0, 0, 0, 0,
                                                           0, 0, 0)).fetchall()
        res = cur.execute(f'''UPDATE record SET '{n}' = ? WHERE name = ?''', (score, name))
    con.commit()
    con.close()


if __name__ == '__main__':
    update(7, 1000, 'Я')