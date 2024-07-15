import random
import string

def generate_password(password_length):
    if password_length <= 0:
        print("Error: Password length must be greater than 0")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    
    return password

def main():
    try:
        password_length = int(input("Enter password length: "))
    except ValueError:
        print("Error: Please enter a valid number")
        return
    
    password = generate_password(password_length)
    
    if password:
        print("Generated Password: " + password)

if __name__ == "__main__":
    main()
