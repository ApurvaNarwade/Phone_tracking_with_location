import phonenumbers

import folium

from phonenumbers import timezone, geocoder, carrier

from opencage.geocoder import OpenCageGeocode

key = 'e413c8e12d174739bf17742b26341480'

number = input("Enter your phone number with country code : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')

print(phone)
print(time)
print(car)
print(reg)

geocoder = OpenCageGeocode(key)

query = str(reg)
result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = reg).add_to((myMap))

myMap.save("myLocation.html")