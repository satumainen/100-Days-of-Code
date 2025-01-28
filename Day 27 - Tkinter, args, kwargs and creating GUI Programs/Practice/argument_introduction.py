"""
Unlimited Arguments *args
def add(*args):
    for n in args:
        print(n)

This function can accept any number of arguments

"""

def add(*args):
    """Takes in any number of arguments and adds them together"""
    #print(args[0]
    sum = 0
    for n in args: #looping the tuple
        sum += n
    print(sum)
    return sum

add(1,2,3,4,5)

"""
These are also called positional arguments, as the position of the 
arguments matter. But what if we want to access arguments by name, 
not by position?
"""

"""
Many Keyword Arguments **kwargs
Allows us to work with an arbitrary number of keywords
"""

def calculate(n, **kwargs):
    """Takes in normal positional argument and kwargs"""
    #print(kwargs) #prints a dictionary that represents each keyword argument and their values
    print(kwargs["add"]) #prints value of keyword add
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

#Let's create a class like **kw

class Car:
    def __init__(self, **kw):
        """Takes in optional kwargs when initializing a new object"""
        self.make = kw.get("make") #get makes sure None is returned if kw is left empty, instead of crashing the code
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Seat", model="Ibiza") #This will only show self: Car, **kw
print(my_car.color)


