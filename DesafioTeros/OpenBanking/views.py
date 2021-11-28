from django.shortcuts import render
from django.http import JsonResponse
from .models import Servers
from django_q.tasks import async_task

def index(request):
    if request.POST.get('deletar_db'):
        Servers.objects.all().delete()
        objeto_list = None
    if request.method == 'GET':
        objeto_list = Servers.objects.all().order_by('nome_empresa')
    context = {'objeto_list':objeto_list}
    return render(request, "index.html",context)