import sqlite3
import uuid


conn = sqlite3.connect('homeless.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS giversTable(UniqueId TEXT , Fullname TEXT, Category TEXT, address TEXT, zipcode INTEGER , description TEXT)")

def dynamic_data_entry():

    UniqueId = str(uuid.uuid4())
    Fullname = input('Pls input your full name')
    Category = input('Pls input your category')
    address = input('Pls input your address')
    zipcode = int(input('Pls input your zip'))
    description = input('Pls describe what you have')

    c.execute("INSERT INTO giversTable (UniqueId, Fullname, Category, address, zipcode, description) VALUES (?, ?, ?, ?, ?, ?)",
              (UniqueId, Fullname, Category, address, zipcode, description))

    conn.commit()


def read_from_db(a,b):
    e = b - 500
    d = b + 500
    c.execute("SELECT UniqueId, Fullname, address, description FROM giversTable WHERE Category == '%s' and zipcode BETWEEN %d AND %d"% (a, e, d))
    data = c.fetchall()
    for row in data:
        print(row)



create_table()
dynamic_data_entry()
takers_category = input("What do you want?")
takers_zipcode = int(input("What is your zip code?"))
read_from_db(takers_category,takers_zipcode)
c.close()
conn.close()
