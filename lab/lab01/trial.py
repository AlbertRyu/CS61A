'''
positive = 28
while positive:
    print("positive?")
    positive -= 3


from math import pi
print(pi)

def area(r, shape_constant):
    assert r>0, "A length must be positive."
    return r* r * shape_constant
    
def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)
'''
def identity(k):
    return k

def cube_k(k):
    return pow(k,3)

def summation(n,term):
    '''
    >>> summation(5,identity) 
    15
    '''
    total, k = 0 , 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
"""
def sum_n(n):
    '''
    >>> sum_n(5) 
    15
    '''
    total, k = 0, 1
    while k<=n:
        total, k = total + k, k + 1
    return total

def sum_c(n):
    '''5
    >>> sum_c(5)
    225
    '''
    total, k = 0, 1
    while k<=n:
        total, k = total + pow(k,3), k+1
    return total

"""

def make_adder(n):
    """
    >>> add_three = make_adder(3) 
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder 

