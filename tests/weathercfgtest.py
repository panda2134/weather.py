import sys,os
sys.path.append('..')
os.chdir('..')
import weathercfg
weathercfg.init()
print weathercfg.weatherOpt  # @UndefinedVariable
#An error of pydev,it's defined yet
