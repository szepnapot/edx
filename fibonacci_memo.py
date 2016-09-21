def fibonacci_memo(n, d):
    if n in d:
        return d[n]
    else:
        fib = fibonacci_memo(n - 1, d) + fibonacci_memo(n - 2, d)
        d[n] = fib
        return fib

d = {1:1 , 2:2}

print(fibonacci_memo(1000, d))