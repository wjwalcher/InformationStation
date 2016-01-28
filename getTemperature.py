#!/usr/bin/python
import urllib.request
import re

def getWeather():
    urlWeather = 'http://forecast.weather.gov/MapClick.php?lat=44.97412689300046&lon=-93.50661848299967'
    reqWeather = urllib.request.Request(urlWeather)
    resp = urllib.request.urlopen(reqWeather)
    respWeather = resp.read()
    temperature = re.findall(r'<p class="myforecast-current-lrg">(.*?)</p>',str(respWeather)) 
    temperature = str(temperature)
    rep = re.sub(r'&deg;F', ' Degrees Farenheit', temperature, count=1)
    num = re.sub(r'&deg;F', 'Degrees', rep)
    print(num)

def getTime():
    urlTime = 'http://www.timeanddate.com/worldclock/usa/minneapolis'
    reqTime = urllib.request.Request(urlTime)
    resp = urllib.request.urlopen(reqTime)
    respTime = resp.read()
    time = re.findall(r'<span id=ct class=h1>(.*?)</span>',str(respTime)) 
    time = str(time)
    print(time)    
    
def getDate():
    urlDate = 'http://www.timeanddate.com/worldclock/usa/minneapolis'
    reqDate = urllib.request.Request(urlDate)
    resp = urllib.request.urlopen(reqDate)
    respDate = resp.read()
    date = re.findall(r'<span id=ctdat>(.*?)</span>',str(respDate)) 
    date = str(date)
    #rep = re.sub(r'&deg;F', ' Degrees Farenheit', temperature, count=1)
    #num = re.sub(r'&deg;F', 'Degrees', rep)
    print(date) 

def getStock(url):
    urlStock = url
    reqStock = urllib.request.Request(urlStock)
    resp = urllib.request.urlopen(reqStock)
    respStock = resp.read()
    stock = re.findall(r'<td class="wsod_last" nowrap="nowrap">(.*?)</td>',str(respStock)) 
    stock = str(stock)
    rep = re.sub(r'<div class="wsod_quoteLabel">','' , stock, count=1)
    rep = re.sub(r'</div>', ' ', rep, count=2)
    rep = re.sub(r'<div class="wsod_quoteLabel">&nbsp;</div>', ' ', rep, count=1)
    rep = re.sub(r'<div class="wsod_quoteLabel">&nbsp;', ' ', rep)
    rep = re.sub(r',', "", rep)
    company = re.findall(r'<h1 class="wsod_fLeft" style="margin-top:6px;">(.*?)</h1>', str(respStock))
    company = str(company)
    company = re.sub(r'<span class="wsod_smallSubHeading">(NASDAQ:AMZN)</span>', ' ', company)
    company = str(company)
    finalString = company + rep 
    #num = re.sub(r'&deg;F', 'Degrees', rep)
    print(finalString)    
    
AmazonStockURL = "http://money.cnn.com/quote/quote.html?symb=AMZN"
    
while(True):
    getWeather()
    getDate()
    getTime()
    getStock(AmazonStockURL)