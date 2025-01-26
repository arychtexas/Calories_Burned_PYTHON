# Calculate Calories Burned
"""
A website lists the calories expended by men and women during exercise as follows (source):
Men: Calories = [(Age × 0.2017) + (Weight × 0.09036) + (Heart Rate × 0.6309) — 55.0969] × Time / 4.184
Women: Calories = [(Age × 0.074) — (Weight × 0.05741) + (Heart Rate × 0.4472) — 20.4022] × Time / 4.184
"""

# Prompt the user for gender
gender = input("Are you male or female? Enter 'male' or 'female': ").strip().lower()

# Validate gender input
if gender not in ['male', 'female']:
    print("Invalid input for gender. Please enter 'male' or 'female'.")
else:
    # Get user inputs for age, weight, heart rate, and time
    age = int(input("Please enter your age (1-129): "))
    weight = int(input("Please enter your weight in pounds (1-1299): "))
    heart_rate = int(input("Please enter your average heart rate (1-300): "))
    time = int(input("Please enter your total workout time in minutes (1-99999): "))
    
    # Calculate calories burned based on gender
    if gender == 'male':
        calories = round(((age * 0.2017) + (weight * 0.09036) + (heart_rate * 0.6309) - 55.0969) * time / 4.184)
    else:  # Female calculation
        calories = round(((age * 0.074) - (weight * 0.05741) + (heart_rate * 0.4472) - 20.4022) * time / 4.184)
    
    # Output the result
    print(f"As a {gender}, you burned approximately {calories} calories during your workout.")
