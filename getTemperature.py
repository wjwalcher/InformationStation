#!/usr/bin/python
import urllib.request
import re

url = 'http://forecast.weather.gov/MapClick.php?lat=44.97412689300046&lon=-93.50661848299967'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

temperature = re.findall(r'<p class="myforecast-current-lrg">(.*?)</p>',str(respData)) 
temperature = str(temperature)

rep = re.sub(r'&deg;F', ' Degrees Farenheit', temperature, count=1)
num = re.sub(r'&deg;F', 'Degrees', rep)

print(num)
