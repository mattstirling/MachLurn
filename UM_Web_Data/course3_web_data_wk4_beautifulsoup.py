'''
Created on Aug 1, 2016

@author: Trader
'''

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib, re
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = ['http://python-data.dr-chuck.net/known_by_Fikret.html'
       ,'http://python-data.dr-chuck.net/known_by_Roxy.html'][1]
position = 18 - 1
repeat = 7 

for i in xrange(repeat):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    url = tags[position].get('href', None)

match = re.search('by_(.*).html',url)
if match is not None: final_name = match.group(1)

print final_name

'''
# Retrieve all of the anchor tags
for tag in tags:
    print tag.get('href', None)
'''