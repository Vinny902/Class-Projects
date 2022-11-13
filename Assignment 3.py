name = input("What is your name: ") #Getting the users name
print(f'{name}, Welcome to my password program')

def valpasword(Password): #defining a function 

 # the code below sets instructional variables to false so the user's input is required to meet the requirement
    if (len(Password)) >= 8:
        lower_Case = False
        upper_Case = False
        number = False
        special_ch = False

#making sure the program checks that the user's input meets all instructions  
        for characters in Password:
            if (not characters.isalnum()):
                special_ch = True
            if (characters.isdigit()):
                number = True
            if (characters.islower()):
                lower_Case = True
            if (characters.isupper()):
                upper_Case = True
        return lower_Case and upper_Case and special_ch and number          
        
    else:
        print("Invalid Password!")

 
#printing out the instructions
instruction = print (
"\nThese are the requirements for a Strong Password must be: "
"\nMore than 8 characters"
"\nMust contain 1 upper case character"
"\nMust contain 1 lower case character"
"\nMust contain 1 digit"
"\nMust contain a special character (! @ # $ % & )")

Password = input("Create your new password: ") 
print(valpasword(Password))