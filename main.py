import requests
import os
import sys
        
os.system('cls||clear & mode 68,17')
os.system('title IP Info Tool')
  
def menu():
    print(f'''
                \u001b[38;5;45m╦╔═╗  ╦  ╔═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
                \u001b[38;5;51m║╠═╝  ║  ║ ║║  ╠═╣ ║ ║ ║╠╦╝
                \u001b[38;5;87m╩╩    ╩═╝╚═╝╚═╝╩ ╩ ╩ ╚═╝╩╚═
                            ''')

def ip_info():
  ip = input("\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mEnter IP\x1b[38;5;250m: ")
  r = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query') 
  data = r.json() 
  ipaddress = data['query']
  country = data['country']
  zipcode = data['zip']
  latt = data['lat']
  lonn = data['lon']
  ispp = data['isp']
  region = data['regionName']
  proxyy = data['proxy']
  hostingg = data['hosting'] 
  os.system('cls')
  print(f'\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mIP\u001b[38;5;45m: \x1b[38;5;250m{ipaddress}\n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mCountry\u001b[38;5;45m: \x1b[38;5;250m{country}\n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mZip Code\u001b[38;5;45m: \x1b[38;5;250m{zipcode}\n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mLatitude\u001b[38;5;45m: \x1b[38;5;250m{latt}\n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mLongitude\u001b[38;5;45m: \x1b[38;5;250m{lonn} \n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mRegion\u001b[38;5;45m: \x1b[38;5;250m{region} \n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mISP\u001b[38;5;45m: \x1b[38;5;250m{ispp}\n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mProxy\u001b[38;5;45m: \x1b[38;5;250m{proxyy}\n\u001b[38;5;45m[\x1b[38;5;250m>\u001b[38;5;45m] \x1b[38;5;250mHosting\u001b[38;5;45m: \x1b[38;5;250m{hostingg}')
  input()
  sys.exit()

menu()
ip_info()