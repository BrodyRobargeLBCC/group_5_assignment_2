"""
Group 5, Exercise 10
Brody Robarge, Christian Davinci

This program computes the sum of an alternating series where each element of the series 
is an expression of the form ((-1)**(k+1)) / (2*k-1) for each value of k from 1 to a million,
multiplied by 4.
"""
# initialize the sum variable
sum = 0 
# create a loop to iterate over values of k from 1 to 1 million
for k in range(1,100001): 
# calculate the value of the expression using the current value of k
    term = 4 * ((-1)**(k+1)) / (2*k-1)
#  add the calcualted value to the sum variable
    sum += term

print(sum)