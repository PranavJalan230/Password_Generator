import random
import string

def generate_password(length=8):
    # Define possible characters: letters, digits, symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure length is valid
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")