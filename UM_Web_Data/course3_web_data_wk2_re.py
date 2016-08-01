'''
Created on Jul 31, 2016

@author: Trader
'''
import re

filename = ['regex_sum_42.txt'
            ,'regex_sum_304958.txt'][1]

cum_sum = 0
for line in open(filename):
    for str_int in re.findall('[0-9]+', line):
        cum_sum += int(str_int)
    
print cum_sum

print sum( [ int(i) for i in re.findall('[0-9]+',open(filename).read()) ] )