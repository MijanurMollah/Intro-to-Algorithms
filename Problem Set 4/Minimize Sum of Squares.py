#
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the square of the difference
# between each element in L and x: SUM_{i=0}^{n-1} (L[i] - x)^2
# 
# Your code should run in Theta(n) time
# 

def minimize_square(L):
    x = 0
    # your code here
    summ = 0
    for elem in L:
        summ += elem
    number = len(L)
    x = (summ+0.0)/number
    return x
    
