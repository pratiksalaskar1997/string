
# find length of the string in 3 ways:
#1 len():
d = 'hello my name is pratik'
print(len(d))

#2 for loop:
d = 'hello my name is pratik'
c = 0
for i in d:
    c += 1
print(c)

#3 while loop:
#def findLen(str):
str = 'hello my name is pratik'
c = 0
while str[c:]:
    c += 1
#return c

print(c)
====================================================
#WAP to print even length word in a string:

for i in str.split():
    #print(len(i))
    if len(i)%2==0:
        print(i)

str = 'my name is pratik and i lived in sindhudurg'
print([i for i in str.split() if len(i)%2==1])
===================================================
# get uppercase of halfstring
str = 'sindhudurg'
print(str[0:len(str)//2]+str[len(str)//2:].upper())
========================================================

# WAP to check whether the string contains numeric and alphabets at least one:
f1 = False
f2 = False
str = 'salaskar1'
for i in str:
    if i.isalpha():
        f1 = True
    if i.isdigit():
        f2 = True
print(f1 and f2)
==========================================================
# WAP to accept the string if it contains all the vowels if not then print not accepted: 
str = 'perIotUuik'
v = 'AEIOU'
s = set(str.upper()).intersection(set(v))

if len(s) == len(v):
    print('accepted given string')
else:
    print('noy accepted')
    # WAP to remove all duplicates in a given string:
str1 = 'pratiksalaskarsalaskar'
s = set(str1)
print(sorted(s)) #for ascending order
==================================================

# WAP to get least frequent character in string:
str1 = 'geekforgeek'
s = {}
for i in str1:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
res = min(s, key= s.get)
print(res)
=================================================================
s = 'geeksfor$geeks'
chr = '[!@#$%^&*()_<>?/\|{}~:]'
z = set(s)
x = set(chr)
print(z)
print(x)
for i in x:
    if s.find(i) == -1:
        print('accepted')
else :
    print('not accepted')
===============================================================
# WAP to check whether the special character is present or not:

import re
s = 'geeksfor/geeks'
chr = re.compile('[!@#$%^&*()_<>?/\|{}~:]')
if chr.search(s) == None:
    print('accepted')
else:
    print('not accepted')

from collections import Counter
s = Counter('geeksforgeeks')
a = input('enter the string: ')
res = s[str(a)]
print(a, 'present', str(res),'times')

# number of vowels present in given string:


from collections import Counter

s = Counter('geeksforgeeks')
v = 'aeiou'
a = ''.join(v)
print(s)
count = 0
for i in a:
    if i in s:
        count += s[i]
print(count,'times')
# 2 method to find vowels in given string:
def v_count():
    count = 0
    v = set('aeiou')
    for i in s:
        if i in v:
            count += 1
    print(count,'times')
s = 'geeksforgeeks'
v_count()
=============================================================
# odd occurrences of given string

from collections import Counter
s = Counter('geeksforgeeks')
for i in s:
    if s[i] % 2 == 1:
        print(i, 'is the odd occurrence',s[i])

=================================================================================================
# WAP to check if entered chr is present or not and if present then how any occurrences are there:
from collections import Counter

# method 1:

str1 = 'geeksforgeeks'
s = Counter('geeksforgeeks')
print('original string is:', str1)
a = input('enter the word to search: ')

for j in a:
    if j in s:
        print(j, 'present', s[j], 'times')
    else:
        print(j, 'is not present')
        #method 2
from collections import Counter

str1 = 'geeksforgeeks'
a = input('enter the chracter: ')
res = {i:j for i,j in dict(Counter(str1)).items() if i in a }
print(res)

s = 'geeks1234555forgeeks'
d = '123456789'
count = 0
for i in s:
    for j in d:
        if j in i:
            count +=1

print(count)

