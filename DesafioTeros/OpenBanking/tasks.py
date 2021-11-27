import requests
import json
from django.contrib import messages
from django.http import request, response
from django.contrib.auth.models import User
from time import sleep

def atualiza_bd():
    payload={}
    headers = {'Connection':'keep-alive'}
    response = requests.get('https://data.directory.openbankingbrasil.org.br/participants', headers=headers)
    json = response.json()
    for i in json:
        nome = i['OrganisationName']
        nome_server = i['AuthorisationServers'][0]['CustomerFriendlyName']
        # svg = requests.request("GET", i['AuthorisationServers'][0]['CustomerFriendlyLogoUri'], headers=headers,verify=False, data=payload, allow_redirects=False).text
        url = i['AuthorisationServers'][0]['OpenIDDiscoveryDocument']
