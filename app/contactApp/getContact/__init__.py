import logging
import azure.functions as func
import json
from json import JSONEncoder
import os
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try :
        url = os.environ["CDBDbConnectionString"] 
        client = pymongo.MongoClient(url)
        database = client['alexeicosmos']
        collection = database['contacts'] 

        result = collection.find({'name' : req.params['name']})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json")

    except ConnectionError:
        print("Could not connect to mongodb")
        return func.HttpResponse("Could not connect to mongodb", status_code=400)
