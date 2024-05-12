from requests import get
import pyfiglet
from colorama import Fore

banner=pyfiglet.figlet_format("IP LOOK UP")
print(Fore.GREEN+banner)

def iplookup(ip):
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
    a=get('https://ipapi.co/'+ip+'/json/',headers).json()
    print(Fore.BLUE+"IP Address:",ip)
    print(Fore.RED+"IP Version:",a.get("version"))
    print("City:",a.get("city"))
    print("Region:",a.get("region"))
    print("Country:",a.get("country_name"))
    print("Postal Code:",a.get("postal"))
    print("Timezone:",a.get("timezone"))
    print("Latitude:",a.get("latitude"))
    print("Longitude:",a.get("longitude"))
    print("ISP:",a.get("org"))
    print(Fore.GREEN+"")

while True:
    print("Select Your Choise:")
    print("1) Look Up For Your IP")
    print("2) Look Up For Another IP")
    print("3) Exit")
    ch=int(input("Enter Your Choice:"))
    if(ch==1):
        yip=get('https://api.ipify.org').content.decode('utf8')
        iplookup(yip)
    elif(ch==2):
        aip=str(input("Enter IP Address:"))
        iplookup(aip)
    elif(ch==3):
        print("See you soon!!")
        break
    else:
        print("Please Enter a Valid choice")
