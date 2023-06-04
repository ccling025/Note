def firstn_generator(n):
    for i in range(1, n+1):
        yield i

#print(sum(firstn_generator(10)))

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        yield a

f = fib(3) #1 1 2 3 5
print(list(f))
        