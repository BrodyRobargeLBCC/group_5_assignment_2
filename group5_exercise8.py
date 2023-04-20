"""
Group 5, Exercise 8
Brody Robarge, Christian Davinci

This program prints all prime numbers up to a number that the user provides

"""
#ask the user for a number
n = int(input("Enter the maximum value to find primes up to: "))

#print statement before loop to help make output look nicer
print("Prime numbers up to", n, ":")
#creating for loop to iterate each number from 2 to n, inclusive
for i in range(2, n+1):
#intializing boolean True to each iteration of loop
    is_prime = True
#nested for loop to help check whether a number is prime or not, using
#the square root of j
    for j in range(2, int(i**0.5) + 1):
#if i is not exactly divisible by j, it is not prime, so break loop
        if i % j == 0:
            is_prime = False
            break
#if is_prime is still True after inner loop has finished, print that number        
    if is_prime:
        print(i)