import random
import string

def generate_password(length):
    """Generates a random password of the specified length."""

    # Define all possible characters (letters, digits, punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to select characters with replacement
    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    """Prompts the user for password length and generates a password."""

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Password length must be positive.")

            password = generate_password(length)
            print("Generated password:", password)
            break

        except ValueError as e:
            print(e) 

if __name__ == "__main__":
    main()
