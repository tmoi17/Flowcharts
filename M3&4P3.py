# Student last name and total exam points

# Prompt student to enter their last name
last_name = input("Enter your last name: ")

# Prompt student to enter their midterm score
midterm_score = float(input("Enter your midterm score: "))
    
# Prompt student to enter their final exam score
final_exam = float(input("Enter your final exam score: "))

# Compute the total exam points
total_exam_points = (midterm_score * 0.40) + (final_exam * 0.60)

# Display result
print(f"{last_name}'s total exam points is: {total_exam_points:.1f}")



