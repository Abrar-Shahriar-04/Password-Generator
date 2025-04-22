import random
import string

def get_user_input():
    while True:
        try:
            length = int(input("How long do you want the password to be? "))
            if length <= 0:
                print("Please enter a positive number.")
            elif length > 12:
                print("Password length should not exceed 12 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    return length, use_digits, use_special, use_uppercase, use_lowercase
  

# This function generates the password using the user's choices
def generate_password(length, use_digits, use_special, use_uppercase, use_lowercase):
    characters = ''  # We'll build a pool of characters here

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected. Cannot generate password.")

    # Randomly choose characters from the selected pool to build the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


#Ask user for options
length, use_digits, use_special, use_uppercase, use_lowercase = get_user_input()

#Generate password using those options
password = generate_password(length, use_digits, use_special, use_uppercase, use_lowercase)

#Print the generated password
print("Generated password:", password)
