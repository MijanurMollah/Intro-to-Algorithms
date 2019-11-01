#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the absolute value of the difference
# between each element in L and x: SUM_{i=0}^{n-1} |L[i] - x|
# 
# Your code should run in Theta(n) time
#
import random

def minimize_absolute(L):
    x = 0
    # your code here
    index = len(L)/2 + 1
    x = find_k(L, index)
    return x

def organize(L, a):
    l = []
    s = []
    r = []
    for elem in L:
        if elem < a:
            l.append(elem)
        elif elem == a:
            s.append(elem)
        else:
            r.append(elem)
    return l, s, r

def find_k(L, k):
    a = random.randrange(len(L))
    a = L[a]
    l, s, r = organize(L, a)
    condition1 = (len(l) + len(s) > k) and len(l) < k
    condition2 = len(l) + len(s) == k
    condition3 = len(l) >= k
    if condition1:
        return a
    if condition2:
        return a
    if condition3:
        return find_k(l, k)
    new_index = k - len(s) - len(l)
    return find_k(r, new_index)

print minimize_absolute([1,2,3])
