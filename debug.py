def debug(func):
    def wrapper(*args, **kwargs):
        print("the function is called " + str(args) + str(kwargs))
        func(*args, **kwargs)
    return wrapper
@debug
def add(a,b):
    print(a+b)
add(1,2)
