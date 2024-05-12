import requests
from bs4 import BeautifulSoup

#import time

#print(time.time())

def details():
    URL="https://www.accuweather.com/en/in/jaipur/205617/weather-forecast/205617"
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    dailylist=soup.find_all(class_="daily-list-item")

    print(dailylist)

print(details())