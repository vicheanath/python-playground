def mydecorator(function):
    def wrapper(*args,**kwargs):
        print("I am decorating your function")
        return function(*args,**kwargs)
    return wrapper

@mydecorator
def hello_world(person):
    print(f"Hello {person}")
    

hello_world("Vichea")    

# mydecorator(hello_world)() same thing