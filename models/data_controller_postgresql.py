import random
import psycopg2

from models.item import Item

class DataControllerPostgresql:

    def __init__(self):
        self.dbName = "test_backend_db"
        self.host = "127.0.0.1"
        self.user = "postgres"
        self.password = "kidGDEu3456uh"
        #sessionDB = psycopg2.connect(dbname=self.dbName, user=self.user, password=self.password, host=self.host)
        #cursorDB = sessionDB.cursor()
        #
        #for i in range(30):
        #    figureType = genRandFigureType()
        #    cursorDB.execute(f"INSERT INTO items (name, figure_type, color, price) VALUES ('{genRandName()} {figureType}', '{figureType}', '{genRandColor()}', {genRandPrice()})")
        #    sessionDB.commit()

    def getItemsDB(self):
        sessionDB = psycopg2.connect(dbname=self.dbName, user=self.user, password=self.password, host=self.host)
        cursorDB = sessionDB.cursor()
        cursorDB.execute("SELECT * FROM items")
        itemsTuple = cursorDB.fetchall()
        sessionDB.commit()
        cursorDB.close()
        sessionDB.close()
        return list(map(lambda tpl: Item(*tpl), itemsTuple))

    def addItemDB(self, item):
        sessionDB = psycopg2.connect(dbname=self.dbName, user=self.user, password=self.password, host=self.host)
        cursorDB = sessionDB.cursor()
        cursorDB.execute(f"INSERT INTO items (name, figure_type, color, price) VALUES ('{item.name}', '{item.figure_type}', '{item.color}', {item.price})")
        sessionDB.commit()
        cursorDB.close()
        sessionDB.close()

    def updateItemDB(self, item):
        sessionDB = psycopg2.connect(dbname=self.dbName, user=self.user, password=self.password, host=self.host)
        cursorDB = sessionDB.cursor()
        cursorDB.execute(f"UPDATE items SET name = '{item.name}', figure_type = '{item.figure_type}', color = '{item.color}', price = {item.price} WHERE item_id={item.item_id}")
        sessionDB.commit()
        cursorDB.close()
        sessionDB.close()

    def updateItemsDB(self, items = []):
        sessionDB = psycopg2.connect(dbname=self.dbName, user=self.user, password=self.password, host=self.host)
        cursorDB = sessionDB.cursor()
        for i in range(items.__len__):
            items[i] = (items[i].name, items[i].figure_type, items[i].color, items[i].price)
        cursorDB.execute("DELETE FROM items")
        cursorDB.executemany("INSERT INTO items (name, figure_type, color, price) VALUES (?, ?, ?, ?)", items)
        sessionDB.commit()
        cursorDB.close()
        sessionDB.close()

    def deleteItemDB(self, item):
        sessionDB = psycopg2.connect(dbname=self.dbName, user=self.user, password=self.password, host=self.host)
        cursorDB = sessionDB.cursor()
        cursorDB.execute(f"DELETE FROM items WHERE item_id={item.item_id}")
        sessionDB.commit()
        cursorDB.close()
        sessionDB.close()

# ====================================================================

def genRandName():
    i = random.randrange(0, 5)
    names = ("Обычный", "Большой", "Малый", "Ровный", "Дефектный")
    return names[i]

def genRandFigureType():
    i = random.randrange(0, 2)
    figureTypes = ("квадрат", "круг")
    return figureTypes[i]

def genRandColor():
    color = '0xFF'
    for i in range(3):
        colorPart = hex(random.randrange(0, 256)).removeprefix("0x")
        if colorPart.__len__() == 1:
            color = color + '0'
        color = color + colorPart
    color = color.upper()
    return color

def genRandPrice():
    i = random.randrange(0, 2000)
    return i * 5