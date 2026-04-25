import random
import string

def generate_password():
    print("--- Random Password Generator ---")
    
    try:
        # Step 1: Get user preferences
        length = int(input("Enter the desired password length: "))
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").lower() == 'y'

        # Step 2: Define the character pool
        characters = string.ascii_letters  # Always include letters
        if include_symbols:
            characters += string.punctuation
        if include_numbers:
            characters += string.digits

        if length < 4:
            print("Password length should be at least 4 for better security.")
            return

        # Step 3: Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))

        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Error: Please enter a valid number for the length.")

if __name__ == "__main__":
    generate_password()
