# Welcome message
print("\nWelcome to the Health and Fitness Assistant!\nA BMI checker, Activity planner, and Body Fat Calculator all in one go where we help you with your health needs!\n")

# Get user input
name = input("Enter your Name: ")

while any(char.isdigit() for char in name):
    print("Invalid input. Please enter a name without numbers. \n")
    name = input("Enter your Name: ")

age = input("Enter your age: ")

while not age.isdigit() or int(age) <= 0:
    print("Invalid input. Please enter a valid age (a positive number).\n")
    age = input("Enter your age: ")

age = int(age)

weight_input = input("Enter your weight in kilograms: ")

while not weight_input.replace(".", "", 1).isdigit() or float(weight_input) <= 0:
    print("Invalid input. Please enter a valid number higher than 0 for weight.\n")
    weight_input = input("Enter your weight in kilograms: ")

weight = float(weight_input)

height_input = input("Enter your height in meters: ")

while not height_input.replace(".", "", 1).isdigit() or float(height_input) <= 0:
    print("Invalid input. Please enter a valid number higher than 0 for height.\n")
    height_input = input("Enter your height in meters: ")

height = float(height_input)

target_weight_input = input("Enter your target weight in kilograms: ")

while not target_weight_input.replace(".", "", 1).isdigit() or float(target_weight_input) <= 0:
    print("Invalid input. Please enter a valid number higher than 0 for target weight.\n")
    target_weight_input = input("Enter your target weight in kilograms: ")

target_weight = float(target_weight_input)

# Input and validation for daily activity level
while True:
    print("\n-----------------------\nSedentary = low amount of physical activity\n"
          "Light = low-intensity activity\n"
          "Moderate = more substantial level of physical exertion\n"
          "Heavy = involves high levels of physical effort\n-----------------------\n")

    activity_level = input("Enter your daily activity level (sedentary/light/moderate/heavy): ").lower()

    if activity_level in ["sedentary", "light", "moderate", "heavy"]:
        break
    else:
        print("Invalid input. Please enter one of the specified activity levels.")

# Dictionary mapping activity levels to suggested daily calorie intakes
calorie_intakes = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "heavy": 1.725}

# Calculate BMI using the formula: BMI = weight (kg) / (height (m) ^ 2)
bmi = weight / (height ** 2)

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
    advice = "It's important to ensure you're getting enough nutrients. Consider consulting with a nutritionist."
elif 18.5 <= bmi < 24.9:
    category = "Normal Weight"
    advice = "Congratulations! You're in a healthy weight range. Keep up the good work with a balanced diet and regular exercise."
elif 25.0 <= bmi < 29.9:
    category = "Overweight"
    advice = "Consider incorporating more physical activity and adopting a healthier diet to reduce the risk of associated health issues."

elif 30.0 <= bmi < 39.9:
        category = "Obese"
        advice = "It's recommended to consult with a healthcare professional to create a personalized plan for weight management."

else:
        category = "Extremely Obese"
        advice = "Immediate consultation with a healthcare professional is strongly advised. Obesity in this range poses serious health risks."

# Calculate suggested daily calorie intake based on activity level
if activity_level in calorie_intakes:
    suggested_calories = weight * 24 * calorie_intakes[activity_level]
else:
    suggested_calories = 0

# Calculate the weight difference needed to reach the target weight
weight_difference = target_weight - weight

# Display the results
print(f"\nHello, {name}!")
print(f"\nAt the age of {age}, your BMI is: {bmi:.2f}")
print(f"You are categorized as: {category}")
print(f"Health advice: {advice}")
print(f"\nTo reach your target weight of {target_weight} kg, you need to gain/lose {abs(weight_difference):.2f} kg.")
print(f"Suggested daily calorie intake is approximately {suggested_calories:.2f} calories based on a {activity_level} activity level.")