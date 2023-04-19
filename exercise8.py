"""
Group 5, Exercise 8
Brody Robarge, Christian Davinci

This program prints all prime numbers up to a number that the user provides

"""
#ask the user for a number
n = int(input("Enter the maximum value to find primes up to: "))

#print all prime numbers up to n
print("Prime numbers up to", n, ":")
#for loop to find our prime numbers
#starting at two and ending on the number that
#the user provides
for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)