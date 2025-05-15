# workout_time_planner.py

def calculate_bmi(weight, height_cm):
    """Calculates and returns BMI rounded to 2 decimals."""
    if weight <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive values.")
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_recommendation(bmi):
    """Returns workout and diet recommendation based on BMI."""
    if bmi < 18.5:
        return "Underweight", "30 mins light exercise", "High-protein meals"
    elif 18.5 <= bmi < 25:
        return "Healthy", "45 mins balanced workout", "Maintain current diet"
    elif 25 <= bmi < 30:
        return "Overweight", "60 mins cardio", "Low-carb, high-fiber meals"
    else:
        return "Obese", "90 mins guided workout", "Strict low-fat diet"

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

# Main interactive section
if __name__ == "__main__":
    weight = get_positive_float("Enter your weight in kg: ")
    height = get_positive_float("Enter your height in cm: ")

    bmi = calculate_bmi(weight, height)
    print(f"\nYour BMI is: {bmi}")

    category, workout, diet = get_recommendation(bmi)
    print(f"\nCategory: {category}")
    print(f"Workout Plan: {workout}")
    print(f"Diet Plan: {diet}")
