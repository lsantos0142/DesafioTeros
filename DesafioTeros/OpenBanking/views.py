from django.shortcuts import render
from django.http import JsonResponse
from django_q.tasks import async_task

def index(request):
    json_payload = {"message": "hello world!"}
    async_task("OpenBanking.tasks.atualiza_bd")
    return JsonResponse(json_payload)