#Kayla Jackson
#07/02/24
#P4LAB2
#Write a program that asks the user to enter an integer.


def display_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            if user_input < 0:
                print("The program cannot accept negative values.")
            else:
                display_multiplication_table(user_input)
            
            run_again = input("Do you wish to run the program again? (yes/no): ").strip().lower()
            if run_again != 'yes':
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
