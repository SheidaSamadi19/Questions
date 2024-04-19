# Authors: Sheida Samadi , Baran Farrokhian

# Libraries
import string

# Functions
def Password(password):
    length = len(password)
    symbols = ['@' , '#']

# Check if the length is between 8 and 12 characters
    if length not in range (8 , 13):
        print("Length of the password should be between 8 & 12")

# Check for at least one small letter
    if not any(char.islower() for char in password):
        print("You should enter one capital letter at least")

# Check for at least one capital letter
    if not any(char.isupper() for char in password):
        print("You should enter one small letter at least")

# Check for at least one digit
    if not any(char.isdigit() for char in password):
        print("You should enter one digit at least")

# Check for at least one special character (# or @)
    if not any(char in symbols for char in password):
        print("You should  at least enter one of the '@' or '#' characters")

    
# Take input from the user
password = input("Enter your password please : " )
print(Password(password))

print("Your password is valid")


