'''
# List
odd = [3,5,5,2,51]
len(odd)
odd[3] = getitem(odd,3)
# Concatenation
[2,7] + odd * 2
#add list
add([2,7],odd*2)

>>> digits = [12,4,5,16]
>>> 16 in digits
True

>>> 3 not in digits
True

>>> not(3 in digits)
True
'''
def count(s,value):
    '''
    how many times certain items appears in a sequence
    
    >>> digits = [1,2,4,5,6,6,6,8,8,9]
    >>> count(digits,6)
    3
    '''
    times, index = 0,0
    for i in s:
        if i == value:
            times += 1
    return times
    
    while index < len(s):
        element = s[index]
        if element == value:
            times += 1
        index += 1
    
# Sequence Unpacking
pairs = [[1,2],[2,2],[3,3],[3,2],[4,4]]
def samecount(list):
    '''
    >>> samecount(pairs)
    3
    '''
    times = 0
    for x,y in pairs:
        if x == y:
            times+=1
    return times

def sum_below(n):

    '''
    >>> list(range(-2,2))
    [-2, -1, 0, 1]

    >>> list(range(4))
    [0, 1, 2, 3]

    >>> sum_below(5)
    10
    '''
    total = 0
    for i in range(n):
        total = total + i
    return total

#List comprehension
def divisor(n):

    '''
    >>> odd = [1,3,5,7,9]
    >>> [x+1 for x in odd]
    [2, 4, 6, 8, 10]

    >>> divisor(8)
    [1, 2, 4]
    '''
    return [1]+[x for x in range(2,n) if n % x == 0]  

# string
city = 'berkeley'
print(len(city))
print(city[3])

#Data abstraction
from math import gcd # great common devisor
#Constructor and selector
def rational(n,d):
    common_devisor = gcd(n,d)
    def selector(name):
        if name == 'n':
            return n//common_devisor
        elif name == 'd':
            return d//common_devisor
    return selector
def numer(ration):
    return ration('n')
def denom(ration):
    return ration('d')

def mul_rat(x,y):
    return rational(numer(x)*numer(y),denom(x)*denom(y))
def add_rat(x,y):
    return rational((numer(x)*denom(y)+numer(y)*denom(x)),denom(y)*denom(x))

#Pairs
pair = [1,2]
x,y = pair

#Dictionary

