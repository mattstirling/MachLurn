'''
Created on Aug 1, 2016

@author: Trader
'''

# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib,re
from BeautifulSoup import *

url_input = ['http://python-data.dr-chuck.net/comments_42.html'
       ,'http://python-data.dr-chuck.net/comments_304963.html'][1]

b_look_at_tags = 0

#url = raw_input('Enter - ' )
url = url_input
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')

cum_sum = 0
for tag in tags:
    
    if b_look_at_tags:
        # Look at the parts of a tag
        print 'TAG:',tag
        print 'URL:',tag.get('href', None)
        print 'Contents:',tag.contents[0]
        print 'Attrs:',tag.attrs
    
    match = re.search(r'>([0-9]*)<',str(tag))
    if match is not None: this_int = int(match.group(1))
    cum_sum += this_int 

print str(cum_sum)