from django.http import JsonResponse
from .search_location import search
from .wdetails import details
from .wforecast import weatherforecast
# Create your views here.

def searchlocations(request,query):
    return JsonResponse(search(query))

def weather(request,query):
    return JsonResponse(details(query))

def forecast(request):
    return JsonResponse(weatherforecast)

def defaultpage(request):
    store={"Message":"Hello From SSR!","Correct Way":"https://weather-api.vercel.app/search/{query}"}
    return JsonResponse(store)

def error404(request,exception):
    store={"Message":"Hello From SSR!","Message":"Not Found"}
    return JsonResponse(store)