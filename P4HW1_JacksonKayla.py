#Kayla Jackson
#07/01/24
#P4HW1
#Ask user to enter for number of scores they would like to enter.


def get_valid_score():
    while True:
        try:
            score = float(input("Enter a score between 0 and 100: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    scores = []
    
    try:
        num_scores = int(input("How many scores would you like to enter? "))
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return
    
    for _ in range(num_scores):
        score = get_valid_score()
        scores.append(score)
    
    if scores:
        lowest_score = min(scores)
        scores.remove(lowest_score)
        average_score = sum(scores) / len(scores) if scores else 0
        
        if average_score >= 90:
            grade = 'A'
        elif average_score >= 80:
            grade = 'B'
        elif average_score >= 70:
            grade = 'C'
        elif average_score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"\nLowest score entered: {lowest_score}")
        print(f"Score List after dropping the lowest score: {scores}")
        print(f"Average of scores in modified list: {average_score:.2f}")
        print(f"Letter grade for the average score: {grade}")
    else:
        print("No valid scores were entered.")

if __name__ == "__main__":
    main()
