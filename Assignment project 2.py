name=""
def greetings():
    # This is the greeting function 
    print("Hi my friend")
    global name

    name = input("what is your name? ") # collecting the user's name
    print("Nice to meet you " + name)

def sum(): # this fuction is the sum function
    print("This is the sum function")

# collecting the users input for addition
    number1 = float(input("Input first Number you want to add: ")) 
    number2 = float(input("input Second number you want to add: "))
    results = number1+ number2 # the sum of number1 and 2

    return results
    
def multiplication(): # This function is the multiplication function

    print("This is the multiplication function ")
# collecting the users input for multiplication
    number1 = float(input("Input first Number you want to multiply: "))
    number2 = float(input("input Second number you want to multiply: "))

    return number1* number2

def display():
    greetings() # calling the greeting function

    value = sum() # calling the sum function

    value2 = multiplication() # calling the multiplication function

# Printing the result
    print(name + " " + "your sum result is "+ str(value) + " and  your multiplication result is "+ str(value2)) 

display() # calling the display function
    






