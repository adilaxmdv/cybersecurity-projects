import string
from getpass import getpass  # Secretly Input

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

print("Secretly Input is here.Dont Panic Not showing your password")
# Input Password Secretly
password = getpass()


def pass_check(password):
    has_lower = any(char in lower for char in password)
    has_upper = any(char in upper for char in password)
    has_digit = any(char in num for char in password)
    has_symbol = any(char in symbols for char in password)

    if len(password) >= 8:
        if has_lower and has_upper and has_digit and has_symbol:
            print("It's an absolutely powerful password!")
        elif has_lower and has_digit and has_symbol:
            print("It's a powerful password, but I suggest you use uppercase letters as well.")
        elif has_upper and has_digit and has_symbol:
            print("It's a powerful password, but I suggest you use lowercase letters as well.")
        elif has_upper and has_lower and has_symbol:
            print("I suggest you use digits in your password.")
        elif has_upper and has_lower and has_digit:
            print("I suggest you use symbols in your password.")
        else:
            print("Please use a stronger password. For example, ensure it has a minimum length of 8 characters and includes uppercase letters, symbols, lowercase letters, and digits.")
    else:
        print("Please use a stronger password. For example, ensure it has a minimum length of 8 characters and includes uppercase letters, symbols, lowercase letters, and digits.")


pass_check(password)
