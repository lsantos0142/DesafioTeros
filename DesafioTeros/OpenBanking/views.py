from django.shortcuts import render
from django.http import JsonResponse
from .models import Servers
from django_q.tasks import async_task

def index(request):
    if request.method == 'GET':
        objeto_list = Servers.objects.all().order_by('nome_empresa')
        async_task("OpenBanking.tasks.atualiza_bd")
    context = {'objeto_list':objeto_list}
    return render(request, "index.html",context)