#-*-coding:utf-8-*-
from xml.dom.minidom import parseString as stringToXml
from requests import get as httpGet
from urllib import quote as urlQuote
from chardet import detect as codingDetect
# using service from "webxml.com.cn"
# Sorry,Only support the weather of China
#TODO:API:
#province
#city
#citycode
#cityimage
#publish time
#today's temprature
#today's weather
#today's wind
#picture ->a.m.
#picture ->p.m.
#the weather now
#wearing,sensitiveness,sports,washCar,dry,trip,road,comfort,air,UV mark
#tomorrow's temprature
#tomorrow's weather
#tomorrow's wind
#picture ->a.m.
#picture ->p.m.
#the day after tomorrow's temprature
#the day after tomorrow's weather
#the day after tomorrow's wind
#picture ->a.m.
#picture ->p.m.
#desciption of the city
def getWeatherByCityName(cityName='58367'):
    r=httpGet('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=%s' %urlQuote(cityName))
    if not r.status_code==200:
        raise Exception,'Can\'t access the server[%d]'%r.status_code
        raise SystemExit,1
    weatherInfo=[x.firstChild.data.strip().encode('utf8') for x in stringToXml(r.text.encode('utf8')).getElementsByTagName('string') if not x==None ]
    weatherInfo[1]=weatherInfo[1].decode(codingDetect(weatherInfo[1])['encoding'])
    weatherInfo[11]=weatherInfo[11].decode(codingDetect(weatherInfo[11])['encoding'])
    return weatherInfo
