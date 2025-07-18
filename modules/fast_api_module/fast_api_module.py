﻿import json
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

import os
import sys
sys.path.append(os.getcwd())

from models.data_controller_sqlite import DataControllerSqlite
from models.data_controller_postgresql import DataControllerPostgresql
from models.item import Item

app = FastAPI()
#dataController = DataControllerSqlite()
dataController = DataControllerPostgresql()

def convertListToJson(data = []):
    dataJson = []
    for item in data:
        dataJson.append(json.dumps(item.__dict__))
    return dataJson

def convertListToItem(data = Body()):
    jsonString = f"{data}".replace("\'", "\"")
    jsonLoads = json.loads(jsonString)
    return Item(**jsonLoads)

@app.get("/")
def root():
    return JSONResponse(content={"message": "Hello World!"})

@app.get("/testItems")
def testItems():
    items = dataController.getItemsDB()
    return JSONResponse(convertListToJson(items))

@app.get("/testItem/{id}")
def testItemId(id: int):
    return JSONResponse(content={"message": ""})

@app.post("/testItem")
def testItemAdd(data = Body()):
    newItem = convertListToItem(data)
    dataController.addItemDB(newItem)
    return JSONResponse(content=data)

@app.put("/testItem")
def testItemSet(data = Body()):
    newItem = convertListToItem(data)
    dataController.updateItemDB(newItem)
    return JSONResponse(content=data)

@app.delete("/testItem")
def testItemRemove(data = Body()):
    newItem = convertListToItem(data)
    dataController.deleteItemDB(newItem)
    return JSONResponse(content=data)
