def calculate_bmi(weight, height_cm): height_m = height_cm / 100; return weight / (height_m ** 2)

def get_workout_and_diet_plan(bmi): 
    if bmi < 18.5: return "30 minutes/day", "High-protein diet with more calories."
    elif 18.5 <= bmi < 25: return "45 minutes/day", "Balanced diet with all nutrients."
    elif 25 <= bmi < 30: return "45 minutes/day", "Avoid fatty foods. Include fruits and vegetables."
    else: return "60 minutes/day", "Strict diet. Consult a nutritionist."

def recommend_workout_place(bmi): 
    if bmi < 18.5: return "🏠 Home workouts with light exercises are recommended."
    elif 18.5 <= bmi < 25: return "🏡 You can work out at home or go to the gym — both are suitable."
    elif 25 <= bmi < 30: return "💪 Gym workouts with a focus on cardio are recommended."
    else: return "🏋️ Gym workouts with professional guidance are strongly recommended."

if __name__ == "__main__":
    try:
        weight_input = input("Enter your weight in kg: ").strip()
        height_input = input("Enter your height in cm: ").strip()

        if not weight_input or not height_input:
            raise ValueError("Input fields cannot be empty.")

        weight = float(weight_input)
        height = float(height_input)

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")

        workout_time, diet_plan = get_workout_and_diet_plan(bmi)
        print(f"Suggested Workout Duration: {workout_time}")
        print(f"Diet Plan: {diet_plan}")

        place = recommend_workout_place(bmi)
        print(place)

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
