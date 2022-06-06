import logging
import os
import azure.functions as func
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try :
        url = os.environ["MyDbConnection"] 
        client = pymongo.MongoClient(url)
        database = client['alexeicosmos']
        collection = database['notes'] 

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json")

    except ConnectionError:
        print("Could not connect to mongodb")
        return func.HttpResponse("Could not connect to mongodb", status_code=400)



