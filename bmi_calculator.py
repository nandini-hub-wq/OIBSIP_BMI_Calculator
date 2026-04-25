# Oasis Infobyte Python Programming Internship
# Task 2: BMI Calculator
# Developed by: Nandini Daharwal

def calculate_bmi():
    print("--- Welcome to the BMI Calculator ---")
    
    try:
        # Get user input for weight and height
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return

        # Calculate BMI using the formula: weight / (height^2)
        bmi = weight / (height ** 2)

        # Display result and categorization
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    except ValueError:
        print("Error: Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    calculate_bmi()
