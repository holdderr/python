import sqlite3
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """ INSERT INTO expences(id, name) VALUES(1, 'Коммуналка') """
    query1 = """ INSERT INTO expences(id, name) VALUES(2, 'Интернет') """
    query2 = """ INSERT INTO expences(id, name) VALUES(3, 'Газ') """
    cursor.execute(query)
    cursor.execute(query1)
    cursor.execute(query2)
    db.commit()

db.close()


