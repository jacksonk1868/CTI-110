#Kayla Jackson
#06/26/24
#P3Lab
#Initial value of all dollars,and coins






dollars, quarters, dimes, nickels, pennies = [0] * 5

money = float(input('Enter an amount of money $:'))

total_pennies = money * 100

while total_pennies > 0:
    if total_pennies >= 100:
        dollars += int(total_pennies / 100)
        total_pennies %= 100
    elif total_pennies >= 25:
        quarters += int(total_pennies / 25)
        total_pennies %= 25
    elif total_pennies >= 10:
        dimes += int(total_pennies / 10)
        total_pennies %= 10
    elif total_pennies >= 5:
        nickels += int(total_pennies / 5)
        total_pennies %= 5
    else:
        pennies = int(total_pennies)
        total_pennies -= total_pennies

print("{} dollars".format(dollars))
print("{} quarters".format(quarters))
print("{} dimes".format(dimes))
print("{} nickels".format(nickels))
print("{} pennies".format(pennies))

