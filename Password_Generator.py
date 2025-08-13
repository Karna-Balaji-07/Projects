# Password Generator

'''
Generate passwords from the list of things that they select or just randomly from their given choice
'''

import string
import secrets
import csv
from cryptography.fernet import Fernet
import os
CSV_FILE = "passwords.csv"
KEY_FILE = "key.key"


def generate_password1(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_password2(length):
    characters = string.digits
    password= "".join(secrets.choice(characters) for i in range(length))
    return password

def generate_password3(length):
    characters = string.ascii_letters
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def generate_password4(length):
    hobbies = input("Enter Fav Hobby: ")
    date = input("Enter your fav date : ")
    location = input("Enter fav location : ")
    food = input("Enter fav food : ")
    sports = input("fav sports or sports team : ")
    arr = [date, location, hobbies,food, sports]
    specialCharacters = ['!','@','#','%']
    numbers = list("0123456789")
    arr.extend(specialCharacters)
    arr.extend(numbers)
    password = []
    while len(''.join(password)) < length:
        part = secrets.choice(arr)
        password.append(part)
    
    passwords = ''.join(password)[:length]
    return passwords

#-----------------------------------------------------------------------------------------------------------------
def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
    return key

def save_password(service, password, fernet):
    encrypted_pw = fernet.encrypt(password.encode()).decode()
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Service", "Password"])
        writer.writerow([service, encrypted_pw])


def view_passwords(fernet):
    if not os.path.exists(CSV_FILE):
        print("No passwords saved yet.")
        return

    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            decrypted_pw = fernet.decrypt(row["Password"].encode()).decode()
            print(f"Service: {row['Service']} | Password: {decrypted_pw}")
            
            
def main():
    key = load_or_create_key()
    fernet = Fernet(key)

    while True:
        print("\nMenu:")
        print("1. Create a password")
        print("2. View saved passwords")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            passwords = input("Do you want to create a randomized password? (Y/N): ").lower()
            if passwords == 'y':
                choices = {
                    '1': 'Randomized',
                    '2': 'Alphabets',
                    '3': 'Numerical'
                }
                print(choices)
                input1 = input("What kind of password do you want? ")

                if input1 == '1':
                    n = int(input("Enter the length of your password: "))
                    password = generate_password1(n)

                elif input1 == '2':
                    n = int(input("Enter the length of your password: "))
                    password = generate_password3(n)

                elif input1 == '3':
                    n = int(input("Enter the length of your password: "))
                    password = generate_password2(n)

                else:
                    print("Invalid choice.")
                    continue

            else:
                n = int(input("Enter the length of your Password: "))
                password = generate_password4(n)

            print("Your Password is:", password)

            if input("Do you want to save this password? (Y/N): ").lower() == 'y':
                service = input("What is this password for? (e.g., Email, Bank, Netflix): ")
                save_password(service, password, fernet)

        elif choice == '2':
            view_passwords(fernet)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()