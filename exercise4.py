"""
Group 5, Exercise 4
Brody Robarge, Christian Davinci

This program asks the user for a number, n and prints the
sum of the numbers from 1 to n

"""

n = int(input("What's your number?"))

result = sum(range(1,n+1))
print(f"the sum of the numbers from 1 to {n} is: {result}")