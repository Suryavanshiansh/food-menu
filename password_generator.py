def password_generator(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    import random
    import string
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

   
    all_chars = lowercase + uppercase + numbers + special_chars

    if not all_chars:
        raise ValueError("At least one character set must be selected.")

   
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password
print("Welcome to the Password Generator!")
print("Select the options for your password:")
length = int(input("Enter the desired length of the password (default is 12): ") or 12)
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
use_numbers = input("Include numbers? (y/n): ").lower() == "y"
use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

password = password_generator(length, use_uppercase, use_numbers, use_special_chars)
print(f"Generated password: {password}")