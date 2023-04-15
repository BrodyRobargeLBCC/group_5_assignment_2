"""
Group 5, Exercise 5
Brody Robarge, Christian Davinci

This program asks the user for a number, n and prints the
sum of the numbers from 1 to n, but only considering multiples
of 3 or 5

"""

n = int(input("Please enter a number?"))

sum_multiples = sum(range(1,n+1))

if n % 3 == 0 or n % 5 == 0:
    print(f"the sum of the multiples of 3 or 5 from 1 to {n} is: {sum_multiples}")
else:
    print("Sorry, your number is not a multiple of 3 or 5.")
