# -*- coding: utf-8 -*-

import re

print('chapter1.3.4')
print('1-----------------------------')
m = re.match('foo', 'foo')
if m is not None: print(m.group())
print('2-----------------------------')
m = re.match('foo', 'bar')
if m is not None: print(m.group())
print('3-----------------------------')
m = re.match('foo', 'food on the table')
print(m.group())
print('4-----------------------------')
print(re.match('foo', 'food on the table').group())
print('5-----------------------------')
m = re.match('foo', 'seafood')
if m is not None: print(m.group())

print('chapter1.3.6')
print('6-----------------------------')
bt = 'bat|bet|bit'  # |或符号，表示多选一
m = re.match(bt, 'bat')
if m is not None: print(m.group())
print('7-----------------------------')
m = re.match(bt, 'blt')
if m is not None: print(m.group())
print('8-----------------------------')
m = re.match(bt, 'he bit me')
if m is not None: print(m.group())
print('9-----------------------------')
m = re.search(bt, 'he bit me')
if m is not None: print(m.group())

print('chapter1.3.7')
print('10-----------------------------')
anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None: print(m.group())
print('11-----------------------------')
m = re.match(anyend, 'end')
if m is not None: print(m.group())
print('12-----------------------------')
m = re.match(anyend, '\nend')
if m is not None: print(m.group())
print('13-----------------------------')
m = re.search('.end', 'The end.')
if m is not None: print(m.group())

print('14-----------------------------')
patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt, '3.14')
if m is not None: print(m.group())
print('15-----------------------------')
m = re.match(patt314, '3014')
if m is not None: print(m.group())
print('16-----------------------------')
m = re.match(patt314, '3.14')
if m is not None: print(m.group())

print('chapter1.3.8')
print('17-----------------------------')
m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None: print(m.group())
print('18-----------------------------')
m = re.match('[cr][23][dp][o2]', 'c2do')
if m is not None: print(m.group())
print('19-----------------------------')
m = re.match('r2d2|c3po', 'c2do')
if m is not None: print(m.group())
print('20-----------------------------')
m = re.match('r2d2|c3po', 'r2d2')
if m is not None: print(m.group())

print('chapter1.3.9')
print('21-----------------------------')
patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt, 'nobody@xxx.com').group())
print('21-2-----------------------------')
patt = '[A-Za-z0-9_]+@(\w+\.)?\w+\.com'
print(re.match(patt, 'nobody@xxx.com').group())
print('22-----------------------------')
# patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt, 'nobody@www.xxx.com').group())
print('23-----------------------------')
patt = '\w+@(\w+\.)*\w+\.com'
print(re.match(patt, 'nobody@www.xxx.yyy.zzz.com').group())
print('24-----------------------------')
m = re.match('\w\w\w-\d\d\d','abc-123')
if m is not None: print(m.group())
print('25-----------------------------')
m = re.match('\w\w\w-\d\d\d','abc-xyz')
if m is not None: print(m.group())

print('26-----------------------------')
m = re.match('(\w\w\w)-(\d\d\d)','abc-123')
print(m.group())
print('27-----------------------------')
print(m.group(1))
print('28-----------------------------')
print(m.group(2))
print('29-----------------------------')
print(m.groups())

print('30-----------------------------')
m = re.match('ab','ab')
print(m.group())
print('31-----------------------------')
print(m.groups())

print('32-----------------------------')
m = re.match('(ab)','ab')
print(m.group())
print('33-----------------------------')
print(m.group(1))
# print('34-----------------------------')
# print(m.group(2))
print('35-----------------------------')
print(m.groups())

print('36-----------------------------')
m = re.match('(a)(b)','ab')
print(m.group())
print('37-----------------------------')
print(m.group(1))
print('38-----------------------------')
print(m.group(2))
print('39-----------------------------')
print(m.groups())

print('40-----------------------------')
m = re.match('(a(b))','ab')
print(m.group())
print('41-----------------------------')
print(m.group(1))
print('42-----------------------------')
print(m.group(2))
print('43-----------------------------')
print(m.groups())


print('chapter1.3.10')
print('44-----------------------------')
m = re.search('^The','The end.')
if m is not None:print(m.group())

print('45-----------------------------')
m = re.search('^The','end. The')
if m is not None:print(m.group())

print('46-----------------------------')
m = re.search(r'\bthe','bite the dog')
if m is not None:print(m.group())

print('47-----------------------------')
m = re.search(r'\bthe','bitethe dog')
if m is not None:print(m.group())

print('48-----------------------------')
m = re.search(r'\Bthe','bitethe dog')
# print(m)
if m is not None:print(m.group())


print('chapter1.3.11')
print('49-----------------------------')
m = re.findall('car','car')
print(m)
print('50-----------------------------')
m = re.findall('car','scary')
print(m)
print('51-----------------------------')
m = re.findall('car','carry the barcardi to the car')
print(m)

print('52-----------------------------')
s = 'This and that.'
m = re.findall(r'(th\w+) and (th\w+)',s,re.I) # r''这个是表示不转义，使用真实字符 print(s = r'test\tddd') test\tddd
print(m)

# print('53-----------------------------')
# print(re.finditer(r'(th\w+) and (th\w+)',s,re.I).next().groups())
# print(m)



print('54-----------------------------')
data = 'winlogon.exe                   504 Console                    1      9,452 K'
data2 = ' of the apple    orange  '
print(re.split(r'\s',data2))
print(re.split('[\f\n\r\t\v]',data2))
print(re.split(r'\s\s',data2))
# print(re.split(r'\s|\t',data2))


print('55----------------------------')
data3 = 'This and that, these and those, th those'
m = re.search('^This',data3)
# print(m)
if m is not None:print(m.group())
m2 = re.search('those$',data3)
if m2 is not None:print(m2.group())
m3 = re.search('^This.*those$',data3)
if m3 is not None:print(m3.group())


print('56----------------------------')
data = 'cat'
data2 = 'mat'
data3 = 'zat'
data4 = 'zaat'
# m = re.search('^[a-z]at$',data)
# if m is not None:print(m.group())
# m = re.search('^[a-z]at$',data2)
# if m is not None:print(m.group())
# m = re.search('^[a-z]at$',data3)
# if m is not None:print(m.group())
m = re.search('^[a-z]at$',data4)
if m is not None:print(m.group())

print('57----------------------------')
data = 'gogle'
data2 = 'google'
data3 = 'goooooooooooooooogle'
data4 = 'goooooooooogle'
# m = re.search('^[a-z]at$',data)
# if m is not None:print(m.group())
# m = re.search('^[a-z]at$',data2)
# if m is not None:print(m.group())
# m = re.search('^[a-z]at$',data3)
# if m is not None:print(m.group())
m = re.search('^go+gle$',data4)
if m is not None:print(m.group())



print('58----------------------------')
data = 'Cat'
data2 = 'cat'
data5 = 'Mat'
data3 = 'zat'
data4 = 'zaat'
# m = re.search('^[A-Za-z]at$',data)
# if m is not None:print(m.group())
# m = re.search('^[A-Za-z]at$',data2)
# if m is not None:print(m.group())
# m = re.search('^[A-Za-z]at$',data3)
# if m is not None:print(m.group())
m = re.search('^[A-Za-z]at$',data5)
if m is not None:print(m.group())
# m = re.search('^[A-Za-z]at$',data5)
# if m is not None:print(m.group())

































