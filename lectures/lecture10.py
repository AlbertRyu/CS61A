# Tree

#Box-and-Pointer Notation
odds = [3,5,7,9,11]

a = sum(odds,1)
# a = 36

b = sum([odds],[13])
# b = [3,5,7,9,11,13]

c = max(range(-5,5)) 
#c = 4
 
d = max(range(-5,5),key=lambda x: x**2)
#d = -5

e = all([1,1,1,1])
# e = True

f = all([1,1,1,0])
# f = False

def tree(label,branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be trees'
    return [label]+list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_Leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2),fib_tree(n-1)
        return tree(label(left)+label(right),[left,right])

def count_leaves(tree):
    if is_Leaf(tree):
       return 1
    else:
        branch_count = [count_leaves(b) for b in branches(tree)]
        return sum(branch_count)
    
def print_tree(tree,indention=0):
    print(' '*indention + str(label(tree)))
    for b in branches(tree):
        print_tree(b,indention+1)