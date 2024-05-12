import requests
from bs4 import BeautifulSoup

def search(term):
    URL="https://www.accuweather.com/en/search-locations?query="+term
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    link=soup.find_all(class_="locations-list content-module")
    print(link)

    name=soup.find_all(class_="location-name")
    print("NAME:",name)

    longname=soup.find_all(class_="location-long-name")
    print("NAME:",name)

    #print(page)
    #print(soup)

    store={}

    for i in link:
        print("Name:",link)
        name2=str(link).split("?key=")
        print("Name2",name2)

    for i in range(1,len(name2)):
        print("From Here:",i)
        codes=name2[i].split('&amp;target=">')
        print(codes[0])
        names=codes[1].split("</a>")[0].replace("\n","").replace("\t","").replace("<span>",'').replace("</span>",'')
        print(names)
        store[codes[0]]=[]

    print(store)
    key=store.keys()

    links=[]

    for i in key:
        links.append(i)
    
    store={}

    for i in range(0,len(name)):
        store[links[i].split('&amp')[0]]={"name":str(name[i]).split('class="location-name">')[1].replace("</p>",''),"longname":str(longname[i]).split('class="location-long-name">')[1].replace("</p>",'')}
    '''
    for i in key:
        ccode=(store[i][::-1].split(",")[0][::-1])
        print(ccode.strip())
        # store[i]=store[i]+"-"+ccode.strip()
        print(i)
        store[i+"-"+ccode.strip()]=store[i]
        print(i)
        del store[i]

    #print(reversed("Hello"))'''

    return store
# search("New York")