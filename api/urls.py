from django.urls import path
from .views import searchlocations,weather,forecast,defaultpage

urlpatterns = [
    path('',defaultpage,name="defaultpage"),
    path('search/<str:query>',searchlocations,name="searchlocations"),
    path('weather/<str:query>',weather,name="weather"),
    path('forecast',forecast,name="forecast"),
]