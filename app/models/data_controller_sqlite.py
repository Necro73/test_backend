import random
import sqlite3

from app.models.item import Item

class DataControllerSqlite:

    def __init__(self):
        self.pathDB = "data/test_backend_db.db"
    #    sessionDB = sqlite3.connect(pathDB, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
    #    cursorDB = sessionDB.cursor()
    #    
    #    for i in range(30):
    #        self.index += 1
    #        figureType = genRandFigureType()
    #        cursorDB.execute(f"INSERT INTO items (name, figure_type, color, price) VALUES ('{genRandName()} {figureType}', '{figureType}', '{genRandColor()}', {genRandPrice()})")
    #        sessionDB.commit()

    def getItemsDB(self):
        sessionDB = sqlite3.connect(self.pathDB, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
        cursorDB = sessionDB.cursor()
        cursorDB.execute("SELECT * FROM items")
        itemsTuple = cursorDB.fetchall()
        sessionDB.commit()
        return list(map(lambda tpl: Item(*tpl), itemsTuple))

    def addItemDB(self, item):
        sessionDB = sqlite3.connect(self.pathDB, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
        cursorDB = sessionDB.cursor()
        cursorDB.execute(f"INSERT INTO items (name, figure_type, color, price) VALUES ('{item.name}', '{item.figure_type}', '{item.color}', {item.price})")
        sessionDB.commit()

    def updateItemDB(self, item):
        sessionDB = sqlite3.connect(self.pathDB, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
        cursorDB = sessionDB.cursor()
        cursorDB.execute(f"UPDATE items SET name = '{item.name}', figure_type = '{item.figure_type}', color = '{item.color}', price = {item.price} WHERE item_id={item.item_id}")
        sessionDB.commit()

    def updateItemsDB(self, items = []):
        sessionDB = sqlite3.connect(self.pathDB, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
        cursorDB = sessionDB.cursor()
        for i in range(items.__len__):
            items[i] = (items[i].name, items[i].figure_type, items[i].color, items[i].price)
        cursorDB.execute("DELETE FROM items")
        cursorDB.executemany("INSERT INTO items (name, figure_type, color, price) VALUES (?, ?, ?, ?)", items)
        sessionDB.commit()

    def deleteItemDB(self, item):
        sessionDB = sqlite3.connect(self.pathDB, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
        cursorDB = sessionDB.cursor()
        cursorDB.execute(f"DELETE FROM items WHERE item_id={item.item_id}")
        sessionDB.commit()

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