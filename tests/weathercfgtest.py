import sys,os
sys.path.append('../')
import weathercfg
os.chdir('..')
weathercfg.init()
print weathercfg.weatherOpt

