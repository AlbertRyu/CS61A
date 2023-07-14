def split(x):
    return x // 10, x % 10
 
def sum_digit(n):
    if n < 10:
        return n
    else:
        other, last  = split(n)
        return sum_digit(other)+last

def fac(n):
    k,result = 1,1
    while k<=n:
        result,k = result * k, k+1
    return result
#TESTTEST
def fac2(n):
    if n == 0: return 1
    else: return n * fac(n-1)

def Luhn_sum(n,result=0):
    other,last = split(n)
    result = result+last
    print(f'plus {last}, result is now {result}')
    if other<10:
        other = double(other)
        return result+other
    if other > 10:
        other2,last2 = split(other)
        last2 = double(last2)
        return Luhn_sum(other2,result)+last2

def double(x):
    if 2*x > 9:
        print(f'double of {x} exceed 9')
        x = sum(split(x*2))
        print(f'they are now change to {x}') 
        return x
    else:
        return 2*x 
