def fib_iter(n):
    a = 0
    b = 1

    for i in range(n):
        a,b=b,a+b

    return a

def fib_rec(n):

    if n ==0 or n==1:
        return n

    else:
        return fib_rec(n-1) + fib_rec(n-2)