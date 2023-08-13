#Assertion
def fact(n):
    assert isinstance(n,int)
    assert n >= 0
    if n == 0:
        return 1 
    else:
        return n*fact(n-1)

def half_fact(n):
    return fact(n/2)

#Handling Error
try:
    #x = 1/0
    x
except NameError as e:
    print('handling a,', type(e))
    x = 1

def invert(x):
    y = 1/x
    print('never printed if x is 0')
    return y

def safe_invert(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled',type(e))
        return 0

#Reduce a Sequence to a Value
from operator import add,mul,truediv
def reduce(f,s,initial):
    if not s:
        return initial
    else:
        return reduce(f,s[1:],f(initial,s[0]))

def divide_all(n,ds):
    try:
        return reduce(truediv,ds,n)
    except ZeroDivisionError:
        return float('inf')