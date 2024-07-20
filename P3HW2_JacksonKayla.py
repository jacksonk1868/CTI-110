#Kayla Jackson
#06/26/24
#P3HW2



def main():
    
    employee_name = input("Enter the name of the employee: ")
    hours_worked = float(input("Enter the number of hours the employee worked this week: "))
    pay_rate = float(input("Enter the employee's pay rate: "))

 regular_hours = 40
    overtime_rate = 1.5


    if hours_worked > regular_hours:
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * pay_rate * overtime_rate
        regular_pay = regular_hours * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay


    print("\nEmployee Pay Details")
    print("--------------------")
    print(f"Employee Name: {employee_name}")
    print(f"Pay Rate: ${pay_rate:.2f}")
    print(f"Hours Worked: {hours_worked:.2f}")
    print(f"Overtime Hours: {overtime_hours:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Pay for Regular Hours: ${regular_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")

if __name__ == "__main__":
    main()
