import tkinter as tk
import string
import secrets

# ---------------- Password Generation Functions ----------------
def generate_password1(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password2(length):
    characters = string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password3(length):
    characters = string.ascii_letters
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password4(length, hobbies, date, location, food, sports):
    arr = [date, location, hobbies, food, sports]
    specialCharacters = ['!', '@', '#', '%']
    numbers = list("0123456789")
    arr.extend(specialCharacters)
    arr.extend(numbers)
    password = []
    while len(''.join(password)) < length:
        part = secrets.choice(arr)
        password.append(part)
    return ''.join(password)[:length]

# ---------------- GUI Functions ----------------
def main_screen():
    clear_frame()
    tk.Label(main_frame, text="Do you want to create a randomized password?", font=("Arial", 12)).pack(pady=20)
    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="YES", width=10, command=show_password_choices).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="NO", width=10, command=no_clicked).grid(row=0, column=1, padx=10)

def show_password_choices():
    clear_frame()
    tk.Label(main_frame, text="Select the type of password:", font=("Arial", 12)).pack(pady=10)
    tk.Button(main_frame, text="Randomized", width=15, command=lambda: ask_length("Randomized")).pack(pady=5)
    tk.Button(main_frame, text="Alphabets", width=15, command=lambda: ask_length("Alphabets")).pack(pady=5)
    tk.Button(main_frame, text="Numerical", width=15, command=lambda: ask_length("Numerical")).pack(pady=5)
    tk.Button(main_frame, text="Back", width=10, command=main_screen).pack(pady=10)

def ask_length(choice):
    clear_frame()
    tk.Label(main_frame, text=f"Enter the length for {choice} password:", font=("Arial", 12)).pack(pady=10)
    length_entry = tk.Entry(main_frame)
    length_entry.pack(pady=5)
    tk.Button(main_frame, text="Generate", command=lambda: generate_and_show(choice, length_entry.get())).pack(pady=10)
    tk.Button(main_frame, text="Back", width=10, command=show_password_choices).pack(pady=10)

def generate_and_show(choice, length_str):
    if not length_str.isdigit():
        show_result("Please enter a valid number.", error=True)
        return
    length = int(length_str)
    if choice == "Randomized":
        password = generate_password1(length)
    elif choice == "Numerical":
        password = generate_password2(length)
    elif choice == "Alphabets":
        password = generate_password3(length)
    show_result(password)

def no_clicked():
    clear_frame()
    tk.Label(main_frame, text="Fill in your favorites:", font=("Arial", 12)).pack(pady=5)

    entries = {}
    for label in ["Hobby", "Date", "Location", "Food", "Sports/Team"]:
        tk.Label(main_frame, text=f"Enter Fav {label}:", font=("Arial", 10)).pack()
        e = tk.Entry(main_frame)
        e.pack(pady=2)
        entries[label] = e

    tk.Label(main_frame, text="Password Length:", font=("Arial", 10)).pack()
    length_entry = tk.Entry(main_frame)
    length_entry.pack(pady=5)

    def generate_from_favorites():
        if not length_entry.get().isdigit():
            show_result("Please enter a valid length.", error=True)
            return
        password = generate_password4(
            int(length_entry.get()),
            entries["Hobby"].get(),
            entries["Date"].get(),
            entries["Location"].get(),
            entries["Food"].get(),
            entries["Sports/Team"].get()
        )
        show_result(password)

    tk.Button(main_frame, text="Generate", command=generate_from_favorites).pack(pady=10)
    tk.Button(main_frame, text="Back", width=10, command=main_screen).pack(pady=10)

def show_result(text, error=False):
    clear_frame()
    if error:
        tk.Label(main_frame, text=text, font=("Arial", 11), fg="red").pack(pady=10)
    else:
        tk.Label(main_frame, text="Your Password:", font=("Arial", 11)).pack(pady=5)
        password_entry = tk.Entry(main_frame, font=("Arial", 12), width=30, justify="center")
        password_entry.pack(pady=5)
        password_entry.insert(0, text)
        password_entry.select_range(0, tk.END)  # highlight for easy copy
    tk.Button(main_frame, text="Back", width=10, command=main_screen).pack(pady=10)

# Utility to clear main_frame
def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x400")

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both")

note_label = tk.Label(root, text="* Clicking NO will create a password from your favorites list.", font=("Arial", 10), fg="gray")
note_label.pack(side="bottom", pady=10)

main_screen()

root.mainloop()
