import json
from django.http import JsonResponse, Body

from models.data_controller_sqlite import DataControllerSqlite
from models.data_controller_postgresql import DataControllerPostgresql
from models.item import Item

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

def testItemshello(request):
    return JsonResponse(data={"message": "Hello World!"})

def testItems(request):
    items = dataController.getItemsDB()
    return JsonResponse(convertListToJson(items))

def testItemId(request):
    return JsonResponse(data={"message": ""})