'''
cfgfile:
section City for city code
section Weather for weather info

!!!Must create Config File First!!!
'''
import ConfigParser,optparse,os

def init():
    
    def getCityCfg():
        '''
        Howto:
        >>> import weathercfg
        >>> weathercfg.init()
        >>> weathercfg.getCityCfg()
        10000000
        
        Get the City in Config File
        '''
        return weatherCfg.get('City','city')
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
    weatherOptParser.add_option("-c","--city",action="store",type="string",dest="city")
    # TODO:Let temprature unit to be able to choice
    #weatherOptParser.add_option("-t","--temprature",action="store",type="choice",dest="tempratureUnit",choices=['C','F'])
    weatherOptParser.add_option("-d","--weatherday",action="store",type="int",dest="weatherDay")
    try:
        weatherOptParser.set_defaults(city=getCityCfg())
    except ConfigParser.NoOptionError:
        weatherOptParser.set_defaults(city='Beijing')
    except:
        pass
    
    # TODO:Let temprature unit to be able to choice
    #try:
    #    weatherOptParser.set_defaults(tempratureUnit=getWeatherCfg('temprature_unit'))
    #except ConfigParser.NoOptionError:
    #    weatherOptParser.set_defaults(tempratureUnit='C')
    #except:
    #    pass
    
    try:
        weatherOptParser.set_defaults(weatherDay=getWeatherCfg('weather_day'))
    except ConfigParser.NoOptionError:
        weatherOptParser.set_defaults(weatherDay=0)
    except:
        pass

    global weatherOpt
    weatherOpt=(weatherOptParser.parse_args())[0]

