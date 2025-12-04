import random
import string

print("Welcome to the Password Generator")

# Ask user for password requirements
password_length = int(input("Enter total password length: "))
letters_count   = int(input("How many letters do you want? "))
digits_count    = int(input("How many digits do you want? "))
symbols_count   = int(input("How many symbols do you want? "))

# Check if counts match desired total length
required_total = letters_count + digits_count + symbols_count

if required_total == password_length:

    # Generate parts of the password
    letters = random.choices(string.ascii_letters, k=letters_count)
    digits  = random.choices(string.digits,        k=digits_count)
    symbols = random.choices(string.punctuation,   k=symbols_count)

    # Combine all characters in one list
    password_parts = letters + digits + symbols

    # Shuffle the password to randomize order
    random.shuffle(password_parts)

    # Convert list to a string
    password = "".join(password_parts)

    print("\nYour generated password:")
    print(password)

else:
    print("\nError: The sum of letters, digits, and symbols does not match the total password length.")