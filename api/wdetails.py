import requests
from bs4 import BeautifulSoup

#import time

#print(time.time())

def details(term):
    store={"temp":"","phase":""}

    result={}

    day={}
    night={"temp":""}

    URL="https://www.accuweather.com/web-api/three-day-redirect?key="+str(term)
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    #print(soup)

    newurl=soup.find(class_="cur-con-weather-card")
    URL="https://www.accuweather.com"+str(newurl).split('href="')[1].split('">')[0]

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    smalldetails=soup.find_all(class_="detail-item spaced-content")
    daycards=soup.find_all(class_="half-day-card")

    #print("DayCard:",daycards)

    days=str(daycards).split('class="title">')

    for i in range(0,1):
        try:
            if("Day" in days[1].split("</h2>")[0]):
                toclear=days[1].replace('\n','').replace('\t','').split('class="panels"')
                day_night=toclear[1].split('class="panel-item">')
                daytemp=days[1].replace('\n','').replace('\t','').split('class="temperature">')[1].split('</span>')[0]
                daytemp=daytemp.split('<span class="')

                night[daytemp[1].split('">')[0]]=daytemp[1].split('">')[1]
                day["temp"]=daytemp[0]

                for dn in range(1,len(day_night)):
                    dayname=day_night[dn].split('<span class="value">')[0]
                    
                    value=day_night[dn].split('<span class="value">')[1].split("</span>")[0]
                    day[dayname]=value

                toclear=days[2].replace('\n','').replace('\t','').split('class="panels"')
                day_night=toclear[1].split('class="panel-item">')
                
                nighttemp=days[1].replace('\n','').replace('\t','').split('class="temperature">')[1].split('</span>')[0]
                nighttemp=nighttemp.split('<span class="')

                night[nighttemp[1].split('">')[0]]=nighttemp[1].split('">')[1]
                night["temp"]=nighttemp[0]

                for dn in range(1,len(day_night)):
                    nightname=day_night[dn].split('<span class="value">')[0]

                    value=day_night[dn].split('<span class="value">')[1].split("</span>")[0]
                    night[nightname]=value
            else:
                toclear=days[1].replace('\n','').replace('\t','').split('class="panels"')

                day_night=toclear[1].split('class="panel-item">')
                nighttemp=days[1].replace('\n','').replace('\t','').split('class="temperature">')[1].split('</span>')[0]
                nighttemp=nighttemp.split('<span class="')
                night[nighttemp[1].split('">')[0]]=nighttemp[1].split('">')[1]
                night["temp"]=nighttemp[0]

                for dn in range(1,len(day_night)):
                    nightname=day_night[dn].split('<span class="value">')[0]
                    value=day_night[dn].split('<span class="value">')[1].split("</span>")[0]
                    night[nightname]=value
        except:
            pass

    findtemp=soup.find(class_="display-temp")
    temp=str(findtemp).replace('<div class="display-temp">','').replace('<span class="sub">','').replace("</span>","").replace("\n</div>","")

    store["temp"]=temp

    findphase=soup.find(class_="phrase")
    phase=str(findphase).replace('<div class="phrase">','').replace("</div>","")

    store["phase"]=phase
    smalldetails2=str(smalldetails).split("class=")

    for i in range(1,len(smalldetails2)):
        name=smalldetails2[i].split("<div>")[1].split("</div>\n")[0]
        detail=smalldetails2[i].split("<div>")[2].split("</div>\n")[0]
        store[name]=detail

    result={"temp":store,"day":day,"night":night}
    return result

    #print(time.time())

# print(details("GEO_75%2E757%2c26%2E905&amp;city=Jaipur&amp;postalCode=&amp;target="))
