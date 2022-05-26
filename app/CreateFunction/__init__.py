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


data = []


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == 'GET':
        return func.HttpResponse(json.dumps(data, cls=ContactEncoder))
    else:
        contact = Contact(req.form['name'],
                        req.form['email'],
                        req.form['message'])
        data.append(contact)
        return func.HttpResponse(json.dumps(data, cls=ContactEncoder))

   



