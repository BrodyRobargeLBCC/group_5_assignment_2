"""
Group 5, Exercise 3
Brody Robarge, Christian Davinci

This program asks the user for their name and prints their name,
but only if their name is Alice or Bob.

"""

name = input("What is your name?")


if name == "Alice" or name == "Bob":
    print(f"Hello, {name}!")
else:
    print("Sorry, your name is not Alice or Bob.")