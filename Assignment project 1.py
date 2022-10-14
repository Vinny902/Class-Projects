# Loan Qualifier Program 

name = input("Hi dear, What is your name? ") # Asking the user for his/her name
print("Hello", name, "welcome to my program")

# Collecting the input from the user to know the amount of house they want to buy
print("Kindly enter your integer value without a comma")
cost_of_house = int(input("What is the cost of the house you are planing on buying with the loan? "))
print("GOOD JOB", name)


# Collecting the input from the user to know their salary amount and their credit score
salary = int(input("Kindly input your gross salary (gross salary is your pre-taxed salary): "))

#the code below checks if all conditions are met and prints the appropriate response
if salary >= 0.2 * cost_of_house:
    print(name, "YOU MAY BE ELIGIBLE FOR THIS LOAN")

    #Asking users for their credit score
    credit_score = int(input("Please input your credit score: "))
    #the code below checks if all conditions are met and prints the appropriate response
    if salary >= 0.2 * cost_of_house and credit_score >= 650:

        #Asking user for the number of years they have worked at their jobs
        years_at_job = int(input("How many years have you been working at your current job? "))
        #the code below checks if all conditions are met and prints the appropriate response
        if salary >= 0.2 * cost_of_house and credit_score >= 650 and years_at_job >= 3:
            print("Processing.......................................")
            print("This may may take up to 30 seconds to process")
            print("Processing.......................................")
            print("..................................................................................")
            print("..................................................................................")
            print("..................................................................................")
            print("CONGRATULATIONS", name, "You are qualified for this loan")
            print("Your loan will be disbursed to your account soon")
        #the esle statement below runs when the if statement above evaluates to false
        else:
            print(name, "Unfornately you are not eligible for this loan right now")
            print("You need to have worked at your current job for at least three years")
    #the esle statement below runs when the if statement above evaluates to false
    else:
        print(name, "Unfornately you are not eligible for this loan right now")
        print("Or you need to improve your credit score")
        print("A minimum of 650 is required")

#the esle statement below runs when the if statement above evaluates to false
else:
    print(name, "Unfornately you are not eligible for this loan right now")
    print("Your salary is not high enough to allow you qualify for this loan")





