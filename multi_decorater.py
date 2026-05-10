from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
        return func(*args, **kwargs)
    return wrapper
def boarder(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("*****")
        func(*args, **kwargs)
        print("*****")
        return func(*args, **kwargs)
    return wrapper
def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        password = "101"
        if password == "101":
            print("you are logged in")
            return func(*args, **kwargs)
        else:
            print("you are not logged in")
    return wrapper
@logger
@boarder
@authenticate
def check():
    print("you can enter")
check()

