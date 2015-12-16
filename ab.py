from bs4 import BeautifulSoup
import urllib2
import re
from PyGlow import PyGlow

pyglow = PyGlow()
pyglow.all(0)

url="http://www.aurora-service.eu/aurora-forecast/"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
kp = find_string = soup.body.findAll(text=re.compile('Kp'), limit=2)
#rank = soup.find("div", {"class": "rank-box"}).h6.contents
kpstring = str(kp)
kpstring = kpstring[34:]
kpstring = kpstring[:5]
kpvalue = float(kpstring)
print kpvalue
if kpvalue >=2:
	#pyglow.all(0)
	pyglow.color("green", 200)
elif (kpvalue <2) and (kpvalue > 1):
	#pyglow.all(0)
	pyglow.color("red", 200)
		
elif kpvalue <=1:
	pyglow.color("yellow", 200)


