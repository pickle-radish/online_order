from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models imposrt Shop, Menu, Order, Orderfood
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import SJONParser

def shop(request):
    if request.method = 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)

        return 
    elif request.method = 'POST':


# Create your views here.
