# Generator Function
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
        
for num in fibonacci(100):
    print(num)