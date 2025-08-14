from typing import ItemsView
from pydantic import Json
import pytest
import json
import requests
from app.models.item import Item
import app.modules.fast_api_module.fast_api_module as fastApiModule

def test_convertListToJson():
    assert type(fastApiModule.convertListToJson() == type(Json))

def test_convertListToItem():
    assert type(fastApiModule.convertListToItem('{}')) == type(Item())
    
def test_root():
    assert json.loads(fastApiModule.root().body)["message"] == "Hello World!"

def test_testItems():
    data1 = []
    for jsonItem in json.loads(fastApiModule.testItems().body.decode('utf-8')):
        data1.append(json.loads(jsonItem))
    data2 = [obj.__dict__ for obj in fastApiModule.dataController.getItemsDB()]
    assert data1 == data2

def test_testItemId():
    assert json.loads(fastApiModule.testItemId(1).body.decode('utf-8'))["message"] == ""

def test_testItemAdd():
    assert fastApiModule.testItemAdd('{}') != fastApiModule.convertListToItem('{}')

def test_testItemSet():
    assert fastApiModule.testItemSet('{}') != fastApiModule.convertListToItem('{}')