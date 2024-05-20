import random
import string

def generate_password(length):
    """
    Generate a complex password with the following characteristics:
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Numbers (0-9)
    - Special characters (!, @, #, $, etc.)

    :param length: The desired length of the password
    :return: A complex password as a string
    """
    # Define the character sets to use
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation

    # Combine the character sets
    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    # Fill the rest of the password with random characters from all sets
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to avoid the first characters always being in the same character set
    random.shuffle(password)

    # Convert the password list to a string
    password = ''.join(password)

    return password

# Example usage
length = 12  # Generate a password with a length of 12 characters
password = generate_password(length)
print(f"Generated password: {password}")
