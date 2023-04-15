"""
Group 5, Exercise 6

This program asks the user for a number n and gives them the possibility
to choose between computing the sum and computing the product of 1,…,n.
"""

n = int(input("Please enter a number?"))

user_choice = str(input("Would you like to compute the sum or the product of this number?"))


if user_choice.lower() == 'sum':
    sum_result = sum(range(1,n+1))
    print(f"the sum of the numbers from 1 to {n} is: {sum_result}")
elif user_choice.lower() == 'product':
    sum_result = 1
    for x in range (1, n+1):
        sum_result *= x
    print(f"the product of the numbers from 1 to {n} is: {sum_result}")
else:
    print("Error. Please enter either 'Sum or 'Product'.")
