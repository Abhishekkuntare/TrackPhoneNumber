import phonenumbers
from text import number

from phonenumbers import geocoder 
ch_nmber = phonenumbers.parse(number, "CH")  #C for country, H for Histroy
print(geocoder.description_for_number(ch_nmber, "en"))

from phonenumbers import carrier #Use to the servise provider name means sim card name
service_nmber = phonenumbers.parse(number , "RO")
print(carrier.name_for_number(service_nmber, "en"))

