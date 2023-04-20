"""
Group 5, Exercise 6
Brody Robarge, Christian Davinci

This program asks the user for a number n and gives them the possibility
to choose between computing the sum and computing the product of 1,…,n.
"""
#asking user for an input which will be turned into an int
n = int(input("Please enter a number?"))
#assigning a string variable to the choice that the user will make after entering their number
user_choice = str(input("Would you like to compute the sum or the product of this number?"))

#creating if statement that will decide what to do with user_choice
if user_choice.lower() == 'sum':
#if user wants sum, find sum and print result
    sum_result = sum(range(1,n+1))
    print(f"the sum of the numbers from 1 to {n} is: {sum_result}")
#if user wants product, find product (using sum) and print result
elif user_choice.lower() == 'product':
    sum_result = 1
#for loop to calculate product
    for x in range (1, n+1):
        sum_result *= x
    print(f"the product of the numbers from 1 to {n} is: {sum_result}")
#if user did not choose either, return an error message
else:
    print("Error. Please enter either 'Sum or 'Product'.")
