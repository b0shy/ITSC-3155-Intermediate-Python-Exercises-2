import time
import random

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = random.randint(15, 35)

start = time.time()
result = fibonacci(n)
end = time.time()

elapsed_time = end - start
print(f"fib({n}) = {result}")
print(f"fin({n}) = {elapsed_time}")
