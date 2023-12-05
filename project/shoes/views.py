from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Shoes


def index(request):
    list_shoes = Shoes.objects.order_by("id")
    output = list(map(lambda x: f'{x},',list_shoes.values_list()))
    return HttpResponse(output)

def detail(request, shoes_id):
    try:
        shoes = Shoes.objects.get(pk=shoes_id)
    except Shoes.DoesNotExist:
        raise Http404("Nao encontramos esse modelo")
    return HttpResponse("Info sobre o tenis %s."% shoes_id)