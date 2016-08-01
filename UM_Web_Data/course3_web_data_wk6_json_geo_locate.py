'''
Created on Aug 1, 2016

@author: Trader
'''
import json, urllib

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = ['South Federal University'
           ,'University of Michigan'][1]

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

html = urllib.urlopen(url).read()

info = json.loads(html)
#print len(info)
#print json.dumps(info, indent=4, sort_keys=True)
print info['results'][0]['place_id']
