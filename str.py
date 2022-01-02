'''
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
'''
