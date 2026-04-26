def limit(n):
    def decorator(func):
        count = 0
        def wrapper(*args,**kwargs):
            nonlocal count
            if count < n:
                count += 1
                return func(*args,**kwargs)
            else:
                print("reached limit")
        return wrapper
    return decorator
@limit(3)
def sum1(a,b):
    print(a,b)
    return a+b
sum1(2,3)
sum1(3,4)
sum1(4,5)
sum1(5,6)