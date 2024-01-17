import math

#program should offer the user two options to enter input either bond or investment.
user_input = input("""Investment - to calculate the amount of interest you'll earn on your investment  
Bond - to calculate the amount you'll have to pay on a home loan

Enter either 'Investment' or 'Bond' from the menu above to proceed:  """)

#if user enters investment the program should then ask them to enter the amount of money they wish to invest, the rate, the number of years and the type of interest

if user_input.lower()== "investment":
    investment = float(input("Enter the amount of money you wish to deposit: "))
    interest_rate= float(input("Please enter your interest rate(no need to add %): ")) / 100
    years =int(input("How many years do you plan to invest?: "))
    interest = input("Do you want simple or compound interest?: ")
    if interest.lower() == "simple" : #after entering simple or compound the program should calculate the invest based on either ismple or compound interest
           total = str(investment * (1 +interest_rate*years))
           print(f"Your total after {years} years is: "+ (total))
    elif interest.lower() == "compound":
        total = str(investment*math.pow((1+interest_rate),years))
        print(f"Your total compound after {years} years is: " + total)
#if use enters bond the program should  ask the user to enter the value of the house, the interest rate, the number of months they plan to payback then give them the amount tehy need to pay each month          
elif user_input.lower() == "bond":
        house_value = int(input("How much is the current value of the current house? £"))
        interest_rate = float(input("Please enter interest rate(no need to add %): ")) / 100 /12
        
        months = int(input("How long in months do you plan to repay the bond? "))
        total = str((interest_rate * house_value) / (1- (1 + interest_rate)** (-months)))
        print(f"You will have to repay £{total} each month")
else:
        print("That is not an option please try again.")