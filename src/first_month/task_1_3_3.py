#Task 1.3.3
# 1.Write a Python function which returns factorial value of given number n.
def factorial(n):
    if n==0 or n==1:
        return  1
    else:
        return factorial(n-1) * n

# 2.Write a Python function which returns the n-th element of the fibonacci series.

def fibonaci(n):
    if n==1:
        return  0
    elif n==2:
        return  1
    else:
        return fibonaci(n-2) + fibonaci(n-1)

print(fibonaci(1))
print(fibonaci(2))
print(fibonaci(3))
print(fibonaci(4))
print(fibonaci(5))


