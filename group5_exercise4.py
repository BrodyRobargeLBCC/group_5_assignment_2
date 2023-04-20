"""
Group 5, Exercise 4
Brody Robarge, Christian Davinci

This program asks the user for a number, n and prints the
sum of the numbers from 1 to n

"""
#asking user for an input which will be turned into an int
n = int(input("What's your number?"))

#finding the sum of numbers from 1 all the way to the number that the user enters
result = sum(range(1,n+1))
#printing the result
print(f"the sum of the numbers from 1 to {n} is: {result}")