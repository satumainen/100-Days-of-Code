"""
the four keywords for writing exceptions

try:
    #try to open this file
    file = open("a_file.txt", "r")
    #Try to print from this dictionary
    a_dictionary = {"key": "value"}
    #print(a_dictionary['this'])
except FileNotFoundError:
    #If there is an exception, open with write mode to create the file
    #Warning: the "except" clause is too broad, be more specific
    file = open("a_file.txt", "w")
    file.write("Hello World")
except KeyError as error_message:
    #Get hold of error message
    print(f"The {error_message} key does not exist")
else:
    #this is executed if the thing we are trying under try succeeds
    content = file.read()
    print(content)
finally:
    #Runs no matter what, not often used
    #raise can be used to raise own errors
    raise TypeError("This is an error I made up")

"""

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")


bmi = weight / height ** 2
print(f"Your BMI is {bmi}")

"""

fruits = ["Apple", "Pear", "Orange"]
 
# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")


 
make_pie(4)



"""
