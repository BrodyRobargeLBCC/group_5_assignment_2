"""
Group 5, Exercise 7
Brody Robarge, Christian Davinci

This program prints a multiplication table for numbers up to 12

"""
#for loop to create our multiplication table
for i in range (1,13):
#nested for second range/axis of the table
    for j in range (1,13):
#multiplying our two variables to get the next line of the table
        k = j * i 
#print the header of the multiplication table from 1 to 12
        print(k, end="\t")
#printing the separator line for correct formatting
    print()
