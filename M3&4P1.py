#Weighted Exam Score Calculator"

# Obtain the exam scores from the user 
first_exam = float(input("Enter the first exam score: "))
second_exam = float(input("Enter the second exam score: "))

# Calculate the weighted total
total_score = (first_exam * 0.60) + (second_exam * 0.40)

# Displays the total
print("\nWeighted Total Score:", total_score)

