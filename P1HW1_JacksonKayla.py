# Kayla Jackson
#06/14/24
# P1HW1
#This assignment allows the user to calculate exponents, addition,
# and subtraction.


#Calculating Exponents
base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))



#Addition and Subtraction


num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

sum = num1 + num2

difference = num1 - num2

print("The sum of the two numbers is:", sum)

print("The difference of the two numbers is:", difference)
