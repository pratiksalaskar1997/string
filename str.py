
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
===================================================================
s = 'amaama'
if s[0:((len(s)//2))]== s[len(s)//2:]:
    print('string is symmetrical')
if s[0:((len(s) // 2))] == s[(len(s)-1) // 2::-1]:
    print('string is palindrome')
else:
    print('not symmetric as well palindrome')
======================================================================
# check if string is binary or not
s = set('101100h')
se = {'0', '1'}
if s == se or s == {'0'} or s == {'1'}:
    print('binary')
else:
    print('not binary')

=================================================================

# uncommon words from two string
method 1:

a  = 'geeks for geeks'
b = 'learning from geeks for geeks'
x = set(a.split())
y = set(b.split())
print(x.symmetric_difference(y))
========================================
#method2
def uncommon(a, b):
    un_comm = [i for i in ''.join(b).split() if i not in ''.join(a).split()]
    print(un_comm)
a = 'geeks for geeks'
b = 'learning from geeks for geeks'
uncommon(a,b)

a = str(input('enter the string: '))
x = a.replace(',','/')
y = x.replace('.',',')
z = y.replace('/','.')
print(z)

# permutation of a given string:
from itertools import permutations
def perm(s):

    z = permutations(s)
    for i in z:
        print(''.join(i))
s = 'abc'
perm(s)

# using recursion reverse the string:
str = 'geeks for geeks'
str = list(str)
l = []
===============================================
for i in range(len(str)):
    l.append(str[i])

for i in range(len(str)):
    str[i] = l.pop() # condition
print(''.join(str))
===============================================
# WAP to get addition of list of two element after reverse and concatenation:

s1 = [2,4,3]
s2 = [5,6,4]
x1=[]
x2=[]
x5 = []
x3 = ''
x4 = ''
for i in range(len(s1)):
    x1.append(s1.pop())

for j in range(len(s2)):
    x2.append(s2.pop())

for a in range(len(x1)):
    x3 += str(x1[a])
print(x3)
for b in range(len(x2)):
    x4 += str(x2[b])
print(x4)
z = int(x3)+int(x4)
print(z)
z1 = str(z)
for q in range(len(z1)):
    x5.append(int(z1[q]))
print(x5[::-1])
======================================
#input : n =[7,2,11,15] and target = t
#output : [0,1]
def IndCheck(n,t):
    for i in range(len(n)):
        for j in range(i+1,(len(n))):
            if n[i]+n[j] == t:
                return [i,j]
print(IndCheck([7,2,11,15],9))
============================================
# Python program to find the character position of Kth word from a list of strings
#Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21
#Output : 0
#Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.

s = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
k =22
a = 0
x = ''
for j in s:
    x += j
print(''.join(x))
x = x[k:k+1]
print('kth letter is -',x)
for i in range(len(s)):
     a += len(s[i])
     if a>k:
         y = s[i]
         break
print('kth index occure in - ',y)
print('which is,',y.index(x),'th element of word')
===========================================================
#Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2
#Output : [(4, 5, 5, 4)]

l = [(4, 5, 5, 4), (5, 4, 3)]
k = 5
n = 2

for i in l:
    if k in i:
        if  i.count(k) == n:
            print([i])

    else:
        print(l.clear())
==============================================================
#Remove punctuation from string

s = 'abc!dh#nf$'
for i in s:
    if i.isalpha() == True:
        print(i, end='')
        
 ==========================================================

# WAP to get string after the right and left shift operation:

s = 'geeksforgeeks'
r = 7
l = 10
t = (r-l) % len(s)
print(t)
res = s[t:len(s)]+s[:t]
print(res)

s = 'gfg, is, (best, for), geeks'
temp = ''
res = []
check = 0
for i in s:
    if i == '(':
        check += 1
    elif i == ')':
        check -= 1
    if i == ', ' and check == 0:
        if temp.strip():
            res.append(temp)
        temp = ''
    else:
        temp += i
if temp.strip():
    res.append(temp)
print(res)
==========================================================
# add string in list without comma:

s = 'gfg, is, (best, for), geeks'
a = [' '.join(s.split())]
print(a)
========================================================
# check range of number and print number which is divisible by 3:

s = (1, 10, 3)
res = [i for i in range(s[0],s[1]) if i%3==0]
print(res)
def leftOperator(s):


==========================================================
# as we see below if list of first elements shifted right by 1 and the number in second list same then 
print 'True' otherwise 'False':
# rightOperator([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])

s = ([1, 2, 3, 4, 5], [5, 5, 2, 3, 4])
#print(len(s))
l = 1
t =l%len(s)
a = s[0]
b = s[1]
res = b[t:len(a)]
if res == (a[:(len(a)-1)]):
    print('True')
else:
    print('false')
=========================================================================
# implement this: (["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

s = ['Adam', 'Sarah', 'Malcolm']
res = sorted(i[0] for i in s)
print(''.join(res))
==========================================================
#check isogram:

s =("AlgorismM s")
ss = set(s.lower())

if len(s) == len(ss):
    print('isogram')
elif ' ' in ss:
    print('not valid')
else:
    print('not isogram')
===========================================================
# WAP to check the string string is in sorted formate and if yes the print 'true' else 'false' 
also if string contains two words then it is not valid:
s = 'abc'
res = sorted(s)
print(type(res))
if s == '':
    print('entered some character')
elif list(s) == res:
    print('true')
else:
    print('false')
