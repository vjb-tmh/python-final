#!/usr/bin/python

# COMMENTS
""" Multiline
    Comment """

# VARIABLES
x = 5
y = "wombat"
print x
print y

# variables can change type
x = "dragon"
print x

print("green " +  x)

# GET TYPE - type()
x = 1
y = 3.5
z = "foo"
print(type(x))
print(type(y))
print(type(z))

# CASTING -  int(), float(), str()
print int(2.7)
print float(1)
print str(88) + " hobbits"

# STRINGS - strip(), len(), upper(), lower(), replace(), split()
print 'hello' == "hello"
a = "elf"
print a[0]

# substring
a = "foobar"
print a[3:6]

# remove white space
a = "foo   "
print a.strip() + "bar"

# length
a = "foo"
print len(a)

# upper/lower
a = "fOoBaR"
print a.upper()
print a.lower()

# replace
a = "xxxzzz"
print a.replace('x','a')

a = "some funky phrase"
print a.replace('funky','monkey')

# split
a = '1|2|3|4|5'
print a.split('|')

# CMDLINE INPUT - raw_input(), input()
"""
x = raw_input('Enter your name: ')
print 'Your name is ' + x
"""

""" note that using input() won't work because it inteprets its input
    so it will return an int if an int is entered, or a variable
    if a name is entered. """

# EXPONENTIATION / FLOOR DIVISION - **, //
print 7.7 // 2
print 2 ** 3

# COMPARISON
if(5 != 7):
    print 'not equal'

# LOGICAL OPERATORS - and, or, not
a = 5
b = 5
c = 7
if(a == b and b != c):
    print 'a == b and b != c'

if(a != b or b != c):
    print 'a != b or b != c'

if(not(a == c and b == c)):
    print 'not the case that a == c and b == c'

# IDENTITY OPERATORS - is, is not
x = 7
y = x
z = 8
if(x is y):
    print 'x is y'

if(x is not z):
    print 'x is not z'

# MEMBERSHIP OPERATORS -  in, not in
x = ["one","two"]
print "one" in x


### COLLECTIONS ###
"""
LIST is an collection which is ordered and changeable. Allows duplicate members.

TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.

SET is a collection which is unordered and unindexed. No duplicate members.

DICTIONARY is a collection which is unordered, changeable and indexed. No duplicate members.
"""

# LISTS - [] append(),remove(),len()
l = ['a','b','foo']
print 'a' in l

l.append('bar')
print l

l.remove('foo')
print l

print len(l)

l = list((1,2,3)) # constructor initialization
print l

# TUPLE - () ordered and unchangeable
t = ('a','b','foo',7)
print 'tuple has members: ' + str(t) + ' with length ' + str(len(t))

"""
Note that operations like t[0] = 'c' will throw an error
"""

# SETS  - {} unordered and unindexed
#       - add(), remove()
s = {'a','b','c'}
s.add(7)
s.remove('a')
print 'Contents of set: ' + str(s) + ' with length ' + str(len(s))

# DICTIONARIES - {'key':'value'}, del()
d = {
    'green' : 'lizard',
    'red'   : 'flower',
    'blue'  : 'water'
}

print d['blue']

d['yellow'] = 'lemon'
print d

del(d['green'])
print d

print 'Dictionary length is: ' + str(len(d))

# CONDITIONS - if, elif, else
a = 'one'
b = 'two'
c = 'one'

if(a == b):
    print 'a == b'
elif(a == c):
    print 'a == c'
else:
    print 'b == c'

# LOOPING

i = 1
while i < 5:
    print i
    i += 1

i = 1
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    elif i == 7:
        break
    print i
    i += 1

l = ['sword','shield','wand','armor']
for e in l:
    print e

# print numbers in range [1,6)
for x in range(6):
    print x

# print numbers in range [2,8) incrementing by 2
for x in range(2,8,2):
    print x

# RECURSION

def tri_recursion(x):
    if x > 0:
        result = x + tri_recursion(x-1)
        print result
    else:
        result = 0
    return result

print '\nRecursion example:\n'
tri_recursion(6)
print

# FUNCTIONS

def fun(foo):
    print foo

fun('bar')

def fun(foo = 1, bar = 'baz'):
    print 'Default values: ' + str(foo) + ' ' + str(bar)

fun()

# LAMBDAS
fun = lambda i: i * 2
print fun(4)

fun = lambda x,y: x * y
print fun(4,12)

def myfunc(x):
    return lambda i: i * x

doubler = myfunc(2)
tripler = myfunc(3)
print doubler(10)
print tripler(10)
print

# FILE HANDLING - open(), r,a,w,x,t,b
f = open('myfile.txt','rt')
print 'file contents: \n' + f.read()

f = open('myfile.txt','rt')
print 'first five characters: ' + f.read(5)

f = open('myfile.txt','rt')
print 'first line: ' + f.readline()

# loop through all file lines
f = open('myfile.txt','rt')
for l in f:
    print(l)

f = open('newfile.txt','w')
for i in range(5):
    f.write('line' + str(i) + '\n')

f = open('newfile.txt','rt')
for l in f:
    print l

# DELETE FILES/DIRECTORIES - import os
import os
os.remove('newfile.txt')
print os.path.exists('newfile.txt')

os.rmdir('foodir')
os.mkdir('foodir')


