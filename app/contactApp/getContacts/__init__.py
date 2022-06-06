import logging
import azure.functions as func
import json
from json import JSONEncoder
import os
import pymongo
from bson.json_util import dumps

class Contact:
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message
        

class ContactEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

data = [
        Contact(name='Enoch Josh',
              email='enoch@josh.com',
              message= 'Mouelet Medical Center'),
        Contact(name='Lily Michele',
              email='lily@michele.org',
              message= 'TOKO LLC'),
        Contact(name='Laidry Arian',
              email='laidry@arian.edu',
              message= 'MabInvestment')
        ]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try :
        url = os.environ["CDBDbConnectionString"] 
        client = pymongo.MongoClient(url)
        database = client['alexeicosmos']
        collection = database['contacts'] 

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json")

    except ConnectionError:
        print("Could not connect to mongodb")
        return func.HttpResponse("Could not connect to mongodb", status_code=400)
