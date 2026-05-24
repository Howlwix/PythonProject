def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
x = fibonacci()
for num in range(12):
    print(next(x))
