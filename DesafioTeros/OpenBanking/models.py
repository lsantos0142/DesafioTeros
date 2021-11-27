from django.db import models

# Create your models here.
class Servers(models.Model):
    nome_empresa = models.CharField(max_length=200)
    nome_server = models.CharField(max_length=200,primary_key=True)
    svg_link = models.CharField(max_length=200)
    url_server = models.URLField(max_length=200)
    svg = models.BooleanField()