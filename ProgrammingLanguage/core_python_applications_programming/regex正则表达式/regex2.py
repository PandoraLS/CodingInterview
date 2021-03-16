# -*- coding: utf-8 -*-
import re

print('chapter1.3.11')
print('54-----------------------------')
print(re.sub('X','Mr. Smith','attn: X\n\nDear X, \n'))
print('55-----------------------------')
print(re.subn('X','Mr. Smith','attn: X\n\nDear X, \n'))

print('56-----------------------------')
print(re.sub('[ae]','X','abcdef'))
print('57-----------------------------')
print(re.subn('[ae]','X','abcdef')) # subn()包含替换总数

print('58-----------------------------')
print(re.split(':','str1:str2:str3'))

print('chapter1.3.12')
print('58-----------------------------')
DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)
for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2}))', datum))
    
print('59-----------------------------')
















































































