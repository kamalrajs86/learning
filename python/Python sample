#import math as m
from math import pi,e
import numpy as np
import pandas
import sys
import os
import imp

def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

#1*2*3*4*5*6 = 720
'''
dfasdfas
'''

def fact(num):
    y = 1
    for i in range(1,num+1):
        y = i * y
    return y

print("The answer is ", fact(4))

Flag = 'Y'
mul = 1

def fact (num):
    num1 = num -1
    global Flag
    global mul
    if Flag == 'Y':
        mul = num*num1
        #print(mul)
        Flag = 'N'
    else:
        #print(mul)
        mul = mul*num1
        #print(mul)
    if num1 != 1:
        fact(num1)
    else:
        print(mul)
    return(mul)
       
    

print("ans is", fact(3))

def factor(num):
    if num == 1:
        return 1
    else:
        return(num*factor(num-1))

num =5
print("factorial is ", factor(5))

my_list = [1,4,6,3]
print(list(map(lambda x : x*5, my_list)))

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

x = 10
def foo():
    
    x = 20
    
    def bar():
        global x
        x = 25
        print("inside bar  ", x)
        
        
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()

print("x in main: ", x)

#print(math.pi)
print(pi,e)
print(sys.path)
print(dir(pi))
print(pi.is_integer())
print(__name__)

c = 5 + 8j
print(c)
print(type(c))
a = 5

print(type(a))

print(type(5.0))


# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10)

# Output: 13
print(0o15)


from decimal import Decimal as D

print(D('1.1') + D('2.2'))

print(D('1.2') * D('2.50'))

import fractions

print(fractions.Fraction(1.5))

print(fractions.Fraction(5))

print(fractions.Fraction(1,3))

from fractions import Fraction as F

print(F(1, 3) + F(1, 3))

import math

print(math.factorial(6),math.log10(10000))

import random

OO = [2,4,31,3243,31]
print(random.choice(OO),random.shuffle(OO),random.randrange(100,300,9))

my_list = [1,3,5,7,24,6,8,"dafasd",32,"awe"]
print("sl;icing", my_list[0:4]) # 0 is index 4 is number + till that number, - excluding that number
print("slicing", my_list[0:-7]) 

my_list.append("hello")
print(my_list)
my_list.extend([4,5,6])
print(my_list)
my_list.insert(1,2)
print(my_list)
my_list.remove("awe")
print(my_list)
my_list.pop(0)
print(my_list)
my_list.pop(-1)
print(my_list)
print(my_list.index(3))
print(my_list.count(5))
#my_list.sort()
my_list.reverse()
print(my_list)
print(my_list.copy())
my_list.clear()
print(my_list)

pow2 = [2**x for x in range(10) if x > 5]
print(pow2)

print(256 in pow2)
for numbe in ['1','3','5']:
    print(" hello " , numbe)
    print(" hello " + numbe)
    

#Tuple/string - cannot delete or remove items , delete or reassign entire tuple
#add items or remove items are not available with tuple

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  

print('a' in my_tuple) #membershipt test
for name in ('a', 'p', 'p', 'l', 'e',): #iterate for 
    print(" hello" + name)

#tuple for immutable/heterogenous data/fast compare with list (list mostly for homo,handle hetero data as wel)
i = 0
for name in "Hello":
    if (name == 'l'):
        i +=1
        print ("letter found")#iterate for 
print(" count of l", i)
print("l" in "Hello")


strtest = "Hello world to coder to pad"

print("enumerage", list(enumerate(strtest)))
print("length", len(strtest))
print(strtest.isnumeric())
print(strtest.lstrip("H"))
print(strtest.upper())
print(strtest.casefold())
print(strtest.join(" online"))
print(strtest.find("to"))
print(strtest.replace("to","for",1))

print("Hello \n world \" wonder")
print(r"Hello \n world \" wonder")
defa = "{} wo {} ewer  {}".format("Hi","How","Are")
print(defa)

pos = "{1} {0} {2}".format("Kamal","Dhan","Rama")
print(pos)


key = "{dad} {mom} {kid}".format(dad = "Kamal",kid = "Dhan",mom = "Rama")            
print(key)

print("One third is: {0:.3f}".format(1/3))
print("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham'))
x = 12
print('The value of x is %3.2f' %x)

os.getcwd()
print(os.getcwd())
print(os.getcwdb())
print(os.listdir())
#print(os.chdir("/home/coderpad"))
#import shutil
#shutil.rmtree()
#print(pandas.arr0ay())
print(dir(locals()['__builtins__']))

try:
    n=1/0
except Exception as e:
    print (e.__class__,"occured")

try:
    #n=1/0
    #assert 4%2 == 0
    raise MemoryError("This is raise error")
except ValueError as V:
    print(V.__class__, "Value error")
#except (TypeError,ZeroDivisionError):
#    print("Type or division error")
except MemoryError as he:
    print(he)
else:
    print("needs to execute after try clause, not got to exception")
finally:
    print("anycase execute try/except")

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')

    
