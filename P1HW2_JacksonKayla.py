#Kayla Jackson
#06/14/24
#P1HW2
#This assignment allows user to calculate and subtract total expenses on
# destination trip.



budget = float(input("Enter your budget: "))

destination = input("Enter your travel destination: ")

gas_expense = float(input("Amount you will spend on gas: "))

accommodation_expense = float(input("Amount you will spend on accommodation: "))

food_expense = float(input("Amount you will spend on food: "))


total_expenses = gas_expense + accommodation_expense + food_expense

budget
remaining_budget = budget - total_expenses


print(f"\nTravel Destination: {destination}")
print(f"{'Total Expenses:':<20} ${total_expenses:,.2f}")
print(f"{'Remaining Budget:':<20} ${remaining_budget:,.2f}")
