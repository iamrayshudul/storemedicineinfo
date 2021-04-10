import sqlite3

def connect():
    conn=sqlite3.connect("medicines.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS medicine (id INTEGER PRIMARY KEY, name text, types text, quantity integer, price integer)")
    conn.commit()
    conn.close()

def insert(name,types,quantity,price):
    conn=sqlite3.connect("medicines.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO medicine VALUES (NULL,?,?,?,?)",(name,types,quantity,price))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("medicines.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM medicine")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",types="",quantity="",price=""):
    conn=sqlite3.connect("medicines.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM medicine WHERE name=? OR types=? OR quantity=? OR price=?", (name,types,quantity,price))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("medicines.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM medicine WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,types,quantity,price):
    conn=sqlite3.connect("medicines.db")
    cur=conn.cursor()
    cur.execute("UPDATE medicine SET name=?, types=?, quantity=?, price=? WHERE id=?",(name,types,quantity,price,id))
    conn.commit()
    conn.close()

connect()