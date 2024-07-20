#Kayla Jackson
#07/02/24
#P4HW2
#Asks the user employee name






def calculate_pay(rate, hours):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
    else:
        regular_pay = hours * rate
        overtime_pay = 0
    gross_pay = regular_pay + overtime_pay
    return regular_pay, overtime_pay, gross_pay

def main():
    total_overtime_pay = 0
    total_regular_pay = 0
    total_gross_pay = 0
    employee_count = 0

    while True:
        employee_name = input("Enter employee name (or 'Done' to finish): ")
        if employee_name.lower() == 'done':
            break

        try:
            pay_rate = float(input(f"Enter pay rate for {employee_name}: "))
            hours_worked = float(input(f"Enter hours worked for {employee_name}: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for pay rate and hours worked.")
            continue

        regular_pay, overtime_pay, gross_pay = calculate_pay(pay_rate, hours_worked)

        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay
        employee_count += 1

        print(f"{employee_name}'s Regular Pay: ${regular_pay:.2f}")
        print(f"{employee_name}'s Overtime Pay: ${overtime_pay:.2f}")
        print(f"{employee_name}'s Gross Pay: ${gross_pay:.2f}\n")

    print("\nSummary:")
    print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
    print(f"Total Regular Pay: ${total_regular_pay:.2f}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Number of Employees Entered: {employee_count}")

if __name__ == "__main__":
    main()
