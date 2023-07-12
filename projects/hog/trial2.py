def outer():
    a = 2
    print("here is outer!")
    def inner(a,b):
        print(a+b)
        print("here is inner!")
        return outer
    return inner

def both(f,g):
    def say(a,b):
        return both(f(a,b),g(a,b))
    return say

def f(a,b):
    print(a+b)

def g(a,b):
    print(a*b)