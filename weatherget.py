#-*-coding:utf-8-*-
from xml.dom.minidom import parseString as stringToXml
from requests import get as httpGet
from urllib import quote as urlQuote
from chardet import detect as codingDetect
# using service from "webxml.com.cn"
# Sorry,Only support the weather of China

def getWeatherByCityName(cityName='58367'):
    r=httpGet('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=%s' %urlQuote(cityName))
    if not r.status_code==200:
        raise Exception,'Can\'t access the server[%d]'%r.status_code
        raise SystemExit,1
    weatherInfo=[x.firstChild.data.strip().encode('utf8') for x in stringToXml(r.text.encode('utf8')).getElementsByTagName('string') if not x==None ]
    weatherInfo[1]=weatherInfo[1].decode(codingDetect(weatherInfo[1])['encoding'])
    weatherInfo[11]=weatherInfo[11].decode(codingDetect(weatherInfo[11])['encoding'])
    weatherInfo_d={
            'province':weatherInfo[0],
            'city':weatherInfo[1],
            'citycode':weatherInfo[2],
            'cityimage':weatherInfo[3],
            'publish_t':weatherInfo[4],
            'd0':{
                'temp':weatherInfo[5],
                'weather':weatherInfo[6],
                'wind':weatherInfo[7],
                'pic_am':weatherInfo[8],
                'pic_pm':weatherInfo[9],
                },
            'weather_now':weatherInfo[10],
            'marks':weatherInfo[11],
            'd1':{
                'temp':weatherInfo[12],
                'weather':weatherInfo[13],
                'wind':weatherInfo[14],
                'pic_am':weatherInfo[15],
                'pic_pm':weatherInfo[16]
                },
            'd2':{
                'temp':weatherInfo[17],
                'weather':weatherInfo[18],
                'wind':weatherInfo[19],
                'pic_am':weatherInfo[20],
                'pic_pm':weatherInfo[21],
                },
            'description':weatherInfo[22],
            }
    return weatherInfo_d
