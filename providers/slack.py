from typing import Dict
from flask import render_template


from .http import httpProvider



class slackProvider():

    webhook = None

    def __init__(self, webhook:str):
        print (webhook)
        self.webhook = webhook


    def send(self, template:str, variables:Dict):
        message = render_template(f'shared/slack/{template}.jnj', **variables)
        print (message)
        response = httpProvider().post(self.webhook, message, 'txt')
        print (response)
        return response

