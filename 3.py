def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

n=int(input("enter the number"))
fibonacci_gen = fibonacci_sequence(n)
fibonacci_list = list(fibonacci_gen)
print(fibonacci_list)
"""
OUTPUT
enter the number100
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""
