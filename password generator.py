# The  Import modules
import random
import string

def generate_password(length):
    # characters to use
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

# user input
length = int(input("Enter the length password: "))

# Generate password
pwd = generate_password(length)

print("generate password:", pwd)