import urllib

u=urllib.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
data=u.read()
f=open('rt22.xml','wb')
f.write(data)
f.close()

amithsLatidue=  41.98062
amits_Longitude=-87.668452

from _elementtree import parse
doc=parse('rt22.xml')
for bus in doc.findall('bus'):
    lat=float(bus.findtext('lat'))
    if lat>amithsLatidue:
        if bus.findtext('d').startswith("North"):
            print bus.findtext('id'), lat



















