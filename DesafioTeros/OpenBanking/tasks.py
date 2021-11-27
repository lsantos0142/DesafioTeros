import requests
import json
from django.contrib import messages
from .models import Servers
from django.http import request, response
from django.contrib.auth.models import User
from time import sleep
import re

def imageFile(str):
 
    # Regex to check valid image file extension.
    regex = "([^\\s]+(\\.(?i)(svg))$)"
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False

def atualiza_bd():
    payload={}
    headers = {'Connection':'keep-alive'}
    response = requests.get('https://data.directory.openbankingbrasil.org.br/participants', headers=headers)
    json = response.json()
    for i in json:
        nome = i['OrganisationName']
        nome_servidor = i['AuthorisationServers'][0]['CustomerFriendlyName']
        svg = i['AuthorisationServers'][0]['CustomerFriendlyLogoUri']
        url = i['AuthorisationServers'][0]['OpenIDDiscoveryDocument']
        if Servers.objects.filter(nome_server__iexact=nome_servidor):
            Servers.objects.filter(nome_server__iexact=nome_servidor).update(nome_empresa=nome,nome_server=nome_servidor,url_server=url,svg_link=svg,svg=imageFile(svg))
        else:
            Servers.objects.create(nome_empresa=nome,nome_server=nome_servidor,url_server=url,svg_link=svg,svg=imageFile(svg))