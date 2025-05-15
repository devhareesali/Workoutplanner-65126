def get_positive_float(prompt):
    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                raise ValueError("Input cannot be empty.")
            value = float(value)
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as ve:
            print(f"Invalid input: {ve}")

# Get user inputs safely
weight = get_positive_float("Enter your weight in kg: ")
height = get_positive_float("Enter your height in cm: ")

# Calculate BMI
height_m = height / 100
bmi = weight / (height_m ** 2)
print(f"\nYour BMI is: {bmi:.2f}")

# Provide workout and diet suggestion
if bmi < 18.5:
    print("You're underweight. Suggested workout: 30 mins light exercise daily. Diet: High-protein meals.")
elif 18.5 <= bmi < 25:
    print("You're in the healthy range! Suggested workout: 45 mins of balanced workout. Diet: Maintain current diet.")
elif 25 <= bmi < 30:
    print("You're overweight. Suggested workout: 60 mins cardio daily. Diet: Low-carb, high-fiber meals.")
else:
    print("You're obese. Suggested workout: 90 mins guided workout daily. Diet: Strict low-fat diet, consult a nutritionist.")