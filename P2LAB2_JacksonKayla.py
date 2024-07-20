#Kayla Jackson
#06/18/24
#P2Lab2
#Using dictionary

car= { 'Camaro' :18.21, 'Prius' :52.36, 'Model S' :110, 'Silverado' :26}


car_keys = car.keys()

print(car_keys)

print (*car_keys, sep = ", ")


car_name = input("Enter a car: ")


car_mpg = car[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon.")


miles_driven = float(input(f"How many miles will you drive the {car_name}?"))



gallons_needed = miles_driven/car_mpg


print(f"{gallons_needed} gallon(s) of gas are needed ot drive the {car_name} {miles_driven} miles")






 
