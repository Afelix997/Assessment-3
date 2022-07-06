from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import requests
from requests_oauthlib import OAuth1
import os

categories= [{
    'name':'bait',
    'url':'/bait/',
    'items': [{
        'name':'Can o\' Worms',
        'price':'$2.00',
        'img':'/static/images/bait_1.jfif'
    },{
        'name':'Lil Guppy',
        'price':'$5.00',
        'img':'/static/images/bait_2.jfif'
    },{
        'name':'Squidward',
        'price':'$10.00',
        'img':'/static/images/bait_3.jfif'
    }]
    },{
    'name':'rods',
    'url':'/rods/',
    'items':[{
        'name':'Reelomatic',
        'price':'$40.00',
        'img':'/static/images/rod_3.png'
    },{
        'name':'Fishotron 2.0',
        'price':'$200.00',
        'img':'/static/images/rod_2.png'
    },{
        'name':'Fishinater 3000',
        'price':'$5000.00',
        'img':'/static/images/rod_1.jfif'
    }]
    },{
    'name':'nets',
    'url':'/nets/',
    'items':[{
        'name':'Fish Basket',
        'price':'$8.00',
        'img':'/static/images/net_1.jfif'
    },{
        'name':'Fish Net',
        'price':'$10.00',
        'img':'/static/images/net_2.jfif'
    },{
        'name':'Cooler Fish Net',
        'price':'$12.00',
        'img':'/static/images/net_3.jfif'
    }]
}]


def index(request):
    
    return render(request, "reel_deal_fishing_app/index.html")
def products(request):

    # GET requests can't have a body. We have to look for the data in the URL. 
    print(request.GET.get('query'))
    query = request.GET.get('query')

    auth = OAuth1('2e274f1e31cf4ebb93a29f9b3f49aeb2', '461503dab42f42e383b97aea4d47c87b')
    endpoint = f"http://api.thenounproject.com/icon/{query}"

    API_response = requests.get(endpoint, auth=auth)
    print(API_response.content)
    JSON_API_response = json.loads(API_response.content)
    image_url = JSON_API_response['icon']['preview_url']
    return JsonResponse({'url': image_url })

def search(request):
    return render(request, "reel_deal_fishing_app/search.html")
def bait(request):
    data= {'products':categories[0]['items']}
    return render(request, "reel_deal_fishing_app/bait.html",data)
def rods(request):
    data= {'products':categories[1]['items']}
    return render(request, "reel_deal_fishing_app/rods.html",data)
def nets(request):
    data= {'products':categories[2]['items']}
    return render(request, "reel_deal_fishing_app/nets.html",data)
def cart(request):
    return render(request, "reel_deal_fishing_app/cart.html")
