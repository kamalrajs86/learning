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



K = [[1,2,3],
     [4,5,6],
     [7,8,9]]

L = [[9,8,7],
     [6,5,4],
     [3,2,1]]


result = [[0,0,0],
          [0,0,0],
          [0,0,0]]


print("K is ", K)
print("K of 1,2 is ", K[1][2])


for i in range(len(K)):
    for j in range(len(K[0])):
        #result[i][j] = K[i][j] * L[i][j]
        #result[i][j] = K[i][j] + L[i][j]
        result[i][j] = K[i][j] - L[i][j]
        
        
for r in result:
    print(r)

str1 = "KamaK"
str2 = reversed(str1)
print(list(reversed(str1)))

if list(str1) == list(str2):
    print("its same")
    
import numpy as np
arr = np.array([[1,2,3],[4,5,6]],dtype=complex)

arr1= np.array([[1,2,3],[4,5,6]],dtype=int)
arr2 = arr * arr1
arr3 = arr2.transpose()


print(arr2)
print(arr3)

arr4 = arr3[1][-1]

print(arr4)

arr5 = arr3[1] # 2 row
arr5 = arr3[:1,] # 1 row all column
arr5 = arr3[:,1] # 1 column
arr5 = arr3[:1,:2] # 1 row 2 column

print(arr5)
'''
                    A
                /    \
                B      C
                /       /
            D    E    F
            /\
            K L
'''
graph = {
    "A":["B","C"],
    "B":['D','E'],
    "C":['F'],
    "D":['K','L'],
    "E":[],
    "F":[],
    "K":[],
    "L":[]
}
print(graph["D"])


visited = set()


#dfs(graph,start,node):
#    if node not in visited:
#        visted.append(node)
        


def dfs(visited,graph,node):
    if node not in visited:
        print(visited)  
        visited.add(node)
        
        for neigh in graph[node]:
            dfs(visited,graph,neigh)
        
dfs(visited,graph,'A')

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = grid1


count = 0

class Solution():
    

                        
    def dfssol(self,grid,i,j):
        
        if i < 0 or j < 0 or grid[i][j] != '1' or i >= len(grid) or j >= len(grid[0]):
            return
        #print("Hello")
        grid[i][j] = '#'
        #print("grid",grid[i][j])
        self.dfssol(grid,i+1,j)
        self.dfssol(grid,i-1,j)
        self.dfssol(grid,i,j+1)
        self.dfssol(grid,i,j-1)
        
    def number_of_island(self,grid):
        global clount
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(grid[i][j])
                if grid[i][j] == '1':
                    global count
                    self.dfssol(grid,i,j)
                    count += 1
                    print("total count is ", count)
        
if __name__ == '__main__':
    P = Solution()
    P.number_of_island(grid2)
    
    res = np.zeros([4,5],dtype = str)
    
    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            res[i][j] = grid2[i][j]
    
    for r in res:
        print("r is ",r)
