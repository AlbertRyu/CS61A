from  ucb import trace
#Tree Recursion
@trace
def fib(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#Number of paths to get to the opposite corner of a n * m grid.
def path(n,m):
    if n == 1 or m == 1:
        return 1
    else:
        return path(n-1,m)+path(n,m-1)

#Knapsack: to see wether the digit of number n could add up to a number k
def knapsack(n,k):
    if n == 0:
        return False
    else:
        if k == 0:
            return True
        elif k < 0:
            return False
        else :
            return knapsack(n//10,k-n%10) or knapsack(n//10,k) 

# count the number of partitions of number n with its maximum part is numbre m
def count_partition(n,m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else: 
        return count_partition(n-m,m)+count_partition(n,m-1)

#all_nums, print all number within k digits using only 0 and 1
# all_nums(3) should print: 111,101,110,10,1,0
def all_nums(k):
    def form_str(k,str):
        if k == 0:
            print(int(str))
        else:
            form_str(k-1,str+'0') 
            form_str(k-1,str+'1')
    form_str(k,'')
    
#Remove unwanting digit:
'''
>>> remove(231,3) 
21
>>> remove(243132,2) 
4313
'''
def remove(n,digit):
    kept,digits=0,0
    while n != 0:
        n, last = n//10, n%10
        if last != digit:
            kept = kept + last * 10 ** digits
            digits += 1
    return kept 