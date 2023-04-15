"""
Group 5, Exercise 8


"""
# Ask the user for a number
n = int(input("Enter a number: "))

# Print all prime numbers up to n
print("Prime numbers up to", n, ":")
for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)





# Write a program that prints all prime numbers. 
# (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)