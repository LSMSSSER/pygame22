import sqlite3

def saving():
    db = sqlite3.connect('commit.db')
    cur = db.cursor()
    res = cur.execute('''SELECT * FROM savepoint 
    WHERE max_level > 0''').fetchall()
    for i in res:
        return i[0]