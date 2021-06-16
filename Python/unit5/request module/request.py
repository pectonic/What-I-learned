'''bugun yemekte onemli bi konu var, requests iyidir neyse lezgo'''

import requests

forces_URL = 'https://data.police.uk/api/forces'

response = requests.get(forces_URL)

#print(help(response))#buradan yardim alabiliriz

#print(response.status_code)# bu bize requestten donen aciklama kodunu yollar.(kodlar hakkinda bilgi https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

#print(response.url) #anladin sen url iste

#print(response.text) #nize icerigi gosteriyor ama okunakli degil di mi? o zaman sunu kullan
bolgeler = response.json()

bolgeler_liste = []
for bolge in bolgeler:
    bolgeler_liste.append(bolge.get('id'))

print(bolgeler_liste) #bu daha okunakli olacaktir

'''simdi katagori altinda nasil aliyoruz ona bakalim'''

#https://data.police.uk/api/crime-categories?date=2011-08 bak ?date=2011-08 dedigi payload

crimes_URL = 'https://data.police.uk/api/crime-categories?date=2011-08'
keyload = {"date":"2021-01"}
responsescrimes = requests.get(crimes_URL, params = keyload)
#print(response.status_code) #evet bir problem yok 
#print(response.json()) #amk vs code yuzunden duzgun gozukmuyor x(

'''simdi birden fazla parametreler nasil oluyor bakalim'''

#https://data.police.uk/api/crimes-no-location?category=all-crime&force=leicestershire&date=2017-03

crimes_no_locations_URL = 'https://data.police.uk/api/crimes-no-location?category=all-crime&force=leicestershire&date=2017-03'
keyload = {
    "category":"all-crime",
    "force":"leicestershire",
    "date":"2021-01"
}
response_crimes_no_locations = requests.get(crimes_no_locations_URL, params=keyload)
#print(response_crimes_no_locations.status_code) #tarih geride olunca hata verdi, guncel tarihli kery load babus




