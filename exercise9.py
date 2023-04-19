"""
Group 5, Exercise 9
Brody Robarge, Christian Davinci

This program is a guessing game where the user has to guess a secret number.
"""
# importing random module so we can use true random
import random
# generate a random secret number between 1 and 10
secret_number = random.randint(1,10)
# set the initial number of lives
lives= 5
prev_guess = None
#prompt user the about the game and ask the question
while lives > 0:
    print("Let's play a game")
    print("I'm thinking of a number between 1 and 10")
    print("Can you guess the number?")
    break
# run the loop until the user run out of lives or guess the correct secret number.
while True:
    try:
# converting input into and interger
        guess = int(input("Enter your guess: ")) 
        if 1 <= guess <= 10: # check if user enter a valid input range between 1 and 10
            if guess != prev_guess:

                if guess < secret_number:
                    print(f"too small! You have {lives} lives left.")
                    lives -= 1
                elif guess > secret_number:
                    print(f"too large! You have {lives} lives left.")
                    lives -= 1
                else:
                    print(f"Congratulations! you guessed it! The secret number was {secret_number} and you had {lives} lives left.")
                    break # exit loop when the number is guess correctly
            else:
                print("You already guessed that number.")
            prev_guess = guess

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10")
    
    if lives == 0:
        print(f"Sorry you're out of lives! The secret number was {secret_number}")

    if guess == secret_number:
        break














# Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. 
# At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.