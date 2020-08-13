from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML



## api_url = 'http://maps.googleapis.com/maps/api/geocode/xml?'




address = input('Enter location: ')
if len(address) < 1:
    address = "Warsaw, Poland"

url = api_url + ENCODE({'sensor': 'false', 'address': address})



print ('Retrieving', url)
data = OPEN(url).read()



print ('Retrieved',len(data),'characters')
tree = XML.fromstring(data)




res = tree.findall('result')


lat = res[0].find('geometry').find('location').find('lat').text

lng = res[0].find('geometry').find('location').find('lng').text

lat = float(lat)
lng = float(lng)
if lat < 0:
    lat_c = '°S'
else:
    lat_c = '°N'
if lng < 0:
    lng_c = '°W'
else:
    lng_c = '°E'
# format the coordinates to a more appealing form

location = res[0].find('formatted_address').text
# location holds the geomap unit found by API, based on user input

print("==>", location, "<==")
print('Latitude: {0:.3f}{1}'.format(abs(lat), lat_c))
print('Longitude: {0:.3f}{1}'.format(abs(lng), lng_c))
