import random

from django.http import HttpResponse
from django.shortcuts import render
from .models import SaveCoin
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def about(request):
    return HttpResponse("About us")

def coin(request):
    rnd_coin = random.choice(["Орел","Решка"])
    save_coin = SaveCoin(coin_var=rnd_coin)
    save_coin.save()
    return HttpResponse(rnd_coin)

def get_all_coin(request):
    return HttpResponse(SaveCoin.get_n(4))