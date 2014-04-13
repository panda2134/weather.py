'''
cfgfile:
section City for city code
section Weather for weather info

!!!Must create Config File First!!!
'''
import ConfigParser,optparse,os

def init():
    
    def getCityCodeCfg():
        '''
        Howto:
        >>> import weathercfg
        >>> weathercfg.init()
        >>> weathercfg.getCityCodeCfg()
        10000000
        
        Get the Citycode in Config File
        '''
        return weatherCfg.getint('City','citycode')
    def getWeatherCfg(opt):
        '''
        Howto:
        >>> import weathercfg
        >>> weathercfg.init()
        >>> weathercfg.getWeatherCfg('weather_day')
        1

        Get the Weather Display Info in Config File
        '''
        return weatherCfg.get('Weather',opt)

    weatherCfg=ConfigParser.ConfigParser()
    # TODO:Change the path of weatherpy.ini
    if os.name=='nt':
        weatherCfg.read("weatherpy.ini")
            #weatherCfg.read(os.environ['HOMEPATH']+'weatherpy.ini')
    elif os.name=='posix':
        weatherCfg.read("weatherpy.ini")
            #weatherCfg.read(os.environ['HOME']+'.weatherpy/weatherpy.ini')
    else:
        weatherCfg.read("weatherpy.ini")
    
    weatherOptParser=optparse.OptionParser()
    weatherOptParser.add_option("-c","--citycode",action="store",type="int",dest="citycode")
    weatherOptParser.add_option("-t","--temprature",action="store",type="choice",dest="tempratureUnit",choices=['C','F'])
    weatherOptParser.add_option("-d","--weatherday",action="store",type="int",dest="weatherDay")
    try:
        weatherOptParser.set_defaults(citycode=getCityCodeCfg())
    except ConfigParser.NoOptionError:
        weatherOptParser.set_defaults(citycode=10100000)
        #        Search the Citycode of Beijing^^^^^^^^
    except:
        pass
    
    try:
        weatherOptParser.set_defaults(tempratureUnit=getWeatherCfg('temprature_unit'))
    except ConfigParser.NoOptionError:
        weatherOptParser.set_defaults(tempratureUnit='C')
    except:
        pass
    
    try:
        weatherOptParser.set_defaults(weatherDay=getWeatherCfg('weather_day'))
    except ConfigParser.NoOptionError:
        weatherOptParser.set_defaults(weatherDay=0)
    except:
        pass

    global weatherOpt
    weatherOpt=(weatherOptParser.parse_args())[0]

