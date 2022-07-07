from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os

load_dotenv()

cart_items=[]
cart_total={'total':0}
items=(
    {
        'item_id': '1',
        'name':'Can o\' Worms',
        'price':'2',
        'img':'/static/images/bait_1.jfif',
        'cart': 1
    },{
        'item_id': '2',
        'name':'Lil Guppy',
        'price':'5',
        'img':'/static/images/bait_2.jfif',
        'cart': 1
    },{
        'item_id': '3',
        'name':'Squidward',
        'price':'10',
        'img':'/static/images/bait_3.jfif',
        'cart': 1
    },{
        'item_id': '4',
        'name':'Reelomatic',
        'price':'40',
        'img':'/static/images/rod_3.png',
        'cart': 1
    },{
        'item_id': '5',
        'name':'Fishotron 2.0',
        'price':'200',
        'img':'/static/images/rod_2.png',
        'cart': 1
    },{
        'item_id': '6',
        'name':'Fishinater 3000',
        'price':'5000',
        'img':'/static/images/rod_1.jfif',
        'cart': 1
    },{
        'item_id': '7',
        'name':'Fish Basket',
        'price':'8',
        'img':'/static/images/net_1.jfif',
        'cart': 1
    },{
        'item_id': '8',
        'name':'Fish Net',
        'price':'10',
        'img':'/static/images/net_2.jfif',
        'cart': 1
    },{
        'item_id': '9',
        'name':'Cooler Fish Net',
        'price':'12',
        'img':'/static/images/net_3.jfif',
        'cart': 1
    }
)

categories= [{
    'name':'bait',
    'url':'/bait/',
    'items': items[0:3]
    },{
    'name':'rods',
    'url':'/rods/',
    'items': items[3:6]
    },{ 
    'name':'nets',
    'url':'/nets/',
    'items': items[6:]
}]
           
def index(request): 
    return render(request, "reel_deal_fishing_app/index.html")

def products(request):

    query = request.GET.get('query')
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
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
   
    purchase = request.POST.get('purchase', None)
    
    for item in items:
        if item['item_id'] == purchase:
            cart_total['total'] += int(item['price']) 
            if not any(d.get('item_id') == purchase for d in cart_items):
                cart_items.append(item)
            else:
                for cart_item in cart_items:
                    if cart_item['item_id'] == purchase:
                        cart_item['cart'] += 1                  

    data= {'cart':cart_items, 'total':cart_total['total']}  
        
    return render(request, "reel_deal_fishing_app/cart.html",data)
