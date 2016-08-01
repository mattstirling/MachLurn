'''
Created on Aug 1, 2016

@author: Trader
'''
import json, urllib

url = ['http://python-data.dr-chuck.net/comments_42.json'
       ,'http://python-data.dr-chuck.net/comments_304964.json'][1]

html = urllib.urlopen(url).read()

info = json.loads(html)
#print len(info)
#print json.dumps(info, indent=4, sort_keys=True)

cum_sum = 0
for comment in info['comments']:
    cum_sum += comment['count']

print cum_sum


input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]'''

'''
for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']
'''