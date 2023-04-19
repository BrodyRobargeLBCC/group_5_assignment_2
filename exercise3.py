"""
Group 5, Exercise 3
Brody Robarge, Christian Davinci

This program asks the user for their name and prints their name,
but only if their name is Alice or Bob.

"""

#asking for input from user
name = input("What is your name?")

#simple if statement
#printing the users name but only if their name is Alice or Bob
if name == "Alice" or name == "Bob":
    print(f"Hello, {name}!")
else:
    print("Sorry, your name is not Alice or Bob.")