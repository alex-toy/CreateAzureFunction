import logging
import azure.functions as func
import json
from json import JSONEncoder
import os

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

    if req.method == 'GET':

        return func.HttpResponse(json.dumps(data, cls=ContactEncoder))
    else:
        name = req.params['name']
        email = req.params['email']
        message = req.params['message']
        contact = Contact(name, email, message)
        data.append(contact)
        return func.HttpResponse(json.dumps(data, cls=ContactEncoder))
