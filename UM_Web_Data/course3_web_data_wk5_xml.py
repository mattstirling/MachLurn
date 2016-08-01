'''
Created on Aug 1, 2016

@author: Trader
'''
import urllib
import xml.etree.ElementTree as ET

url = ['http://python-data.dr-chuck.net/comments_42.xml'
       ,'http://python-data.dr-chuck.net/comments_304960.xml'][0]

html = urllib.urlopen(url)
data = html.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')

cum_sum = 0
for count in counts:
    cum_sum += int(count.text)

print cum_sum