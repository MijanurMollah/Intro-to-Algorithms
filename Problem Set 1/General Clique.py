# Write a function, `count`
# that returns the units of time
# where each print statement is one unit of time
# and each evaluation of range also takes one unit of time

def count(n):
    # Your code here to count the units of time
    # it takes to execute clique
    total_print = 1
    for i in range(n):
        total_print += i
        print total_print
    total_outerFor = 1
    total_innerFor = n
    total_count = total_innerFor + total_print + total_outerFor
    return total_count

def clique(n):
    print "in a clique..."
    for j in range(n):
        for i in range(j):
            print i, "is friends with", j

print count(4)


