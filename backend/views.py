import json
from django.http import HttpResponse, JsonResponse

from app.models.data_controller_sqlite import DataControllerSqlite
from app.models.data_controller_postgresql import DataControllerPostgresql
from app.models.item import Item

from django.views.decorators.csrf import csrf_exempt

#dataController = DataControllerSqlite()
dataController = DataControllerPostgresql()

def debugInfo(label, data):
    print(f'== {label} ================'[0:26])
    print(data)
    print(f'==========================')

def convertListToJson(data = []):
    dataJson = []
    for item in data:
        dataJson.append(json.dumps(item.__dict__))
    return dataJson

def convertListToItem(data):
    jsonString = f"{data}".replace("\'", "\"")
    jsonLoads = json.loads(jsonString)
    return Item(**jsonLoads)

#====================================================

def root(request):
    return JsonResponse(json.dumps({"message": "Hello World!"}), safe=False)

def testItems(request):
    items = dataController.getItemsDB()
    return JsonResponse(convertListToJson(items), safe=False)

def testItemId(request):
    item = dataController.getItemDB(5)
    return JsonResponse(convertListToJson(item), safe=False)

@csrf_exempt
def testItem(request):
    if request.method == 'GET':
        pass
    else:
        newItemDict = json.loads(request.body.decode('utf-8'))
        newItem = Item(**newItemDict)
        if request.method == 'POST':
            dataController.addItemDB(newItem)
            return JsonResponse(newItemDict, safe=False)
        else:
            if request.method == 'PUT':
                dataController.updateItemDB(newItem)
                return JsonResponse(newItemDict, safe=False)
            else:
                if request.method == 'DELETE':
                    dataController.deleteItemDB(newItem)
                    return JsonResponse(newItemDict, safe=False)
