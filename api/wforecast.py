import requests
from bs4 import BeautifulSoup

result={}
temp=[]

today={}
night={}

tomorrow={}

def weatherforecast():
    URL="https://www.accuweather.com/en/in/jaipur/205617/weather-forecast/205617"
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title=soup.find_all(class_="weather-card")
    smalldetails=soup.find_all(class_="temp")

    for i in range(0,len(title)):
        a=str(title[i]).replace("\n","").replace("<svg","").replace("<span","").replace("<div>","").replace("</div>","").replace("</span>","").replace("<h2>","").replace("</h2>","").replace("<div","").split('class="')
        for ii in a:
            if("icon" in ii or "card weather-card content-module" in ii or "card-content" in ii or "forecast-container" in ii or "temp-container" in ii):
                pass
            else:
                if(" " in ii.split('">')):
                    pass
                else:
                    temp.append(ii.split('">')) 

    for i in range(0,len(temp)):
        if("TODAY" in temp[i][1]):
            for j in range(0,len(temp)):
                if("TONIGHT" in temp[j][1] or "TOMORROW" in temp[j][1]):
                    break
                else:
                    today[temp[j][0]]=temp[j][1]
        elif("TONIGHT" in temp[i][1]):
            for j in range(0,len(temp)):
                if("TODAY" in temp[j][1] or "TOMORROW" in temp[j][1]):
                    break
                else:
                    night[temp[j][0]]=temp[j][1]
        elif("TOMORROW" in temp[i][1]):
            #print(True)
            for j in range(0,len(temp)):
                if("TODAY" in temp[i][1] or "TONIGHT" in temp[i][1]):
                    break
                else:
                    tomorrow[temp[j][0]]=temp[j][1]

    results={"today":today,"tonight":night,"tomorrow":tomorrow}
    return results

print(weatherforecast())

