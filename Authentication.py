username = "admin"
password = "jjl"
def authenticate(func):
    def wrapper(ีusername,password):
        if username == "admin" and password == "jjl":
            return func



@authenticate
def logging_in(username,password):
    return "you can enter"
