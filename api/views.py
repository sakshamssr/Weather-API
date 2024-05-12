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