import random
import string
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

# Generate a key and save it if it doesn't exist
def load_or_create_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

fernet = load_or_create_key()

# Encrypt and save passwords to a file
def save_password_to_file(app_name, password):
    # Ensure each entry is written on a new line
    encrypted_data = fernet.encrypt(f"{app_name},{password}".encode())
    with open("passwords.enc", "ab") as file:
        file.write(encrypted_data + b'\n')  # Add a newline to separate entries
    print(f"Saving to file: {app_name},{password}")  # Debug print

# Load and decrypt passwords from the file
def load_passwords_from_file():
    if not os.path.exists("passwords.enc"):
        return []
    
    passwords = []
    with open("passwords.enc", "rb") as file:
        for line in file:
            print(f"Decrypting line: {line}")  # Debug print
            try:
                decrypted_data = fernet.decrypt(line.strip()).decode().strip()  # Strip newline
                # Ensure there is a valid format before unpacking
                if ',' in decrypted_data:
                    app, pwd = decrypted_data.split(',', 1)
                    passwords.append((app, pwd))
                else:
                    print(f"Invalid format: {decrypted_data}")  # Log invalid entries for debugging
            except Exception as e:
                print(f"Failed to decrypt line: {line}. Error: {e}")  # For debugging
    return passwords

# Function to generate a password
def generate_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation  # Include special characters if selected
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle password generation
def generate_password_handler():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive number.")
        
        use_special_chars = special_chars_var.get()  # Get the state of the checkbox
        password = generate_password(length, use_special_chars)

        app_name = entry_app_name.get().strip()  # Get the app name
        if not app_name:
            raise ValueError("App name cannot be empty.")
        
        # Save the generated password
        save_password(app_name, password)
        
        # Display the generated password
        messagebox.showinfo("Generated Password", f"App: {app_name}\nPassword: {password}")
        
        # Copy the password to clipboard
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(password)  # Copy the generated password
        messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard.")
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to save the generated password
def save_password(app_name, password):
    save_password_to_file(app_name, password)

# Function to display the saved passwords in a new window
def open_saved_passwords_window():
    saved_passwords_window = tk.Toplevel(root)
    saved_passwords_window.title("Saved Passwords")
    saved_passwords_window.resizable(False, False)
    saved_passwords_text = tk.Text(saved_passwords_window, height=10, width=50)
    saved_passwords_text.pack(pady=10)

    # Load passwords from the encrypted file
    saved_passwords_list = load_passwords_from_file()
    
    # Display the passwords in the text widget
    if saved_passwords_list:
        for app, password in saved_passwords_list:
            saved_passwords_text.insert(tk.END, f"App: {app}, Password: {password}\n")
    else:
        saved_passwords_text.insert(tk.END, "No passwords saved yet.")

# Setting up the main window

root = tk.Tk()
icon = tk.PhotoImage(file="chaves.png")
root.iconphoto(True, icon)
root.title("One Time Password Generator")
root.resizable(False, False)

# Creating the GUI elements
label_app_name = tk.Label(root, text="Enter the app name:")
label_app_name.pack(pady=5, padx=110)

entry_app_name = tk.Entry(root)
entry_app_name.pack(pady=5)

label_length = tk.Label(root, text="Enter the length of the password:")
label_length.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Checkbox for including special characters
special_chars_var = tk.BooleanVar(value=True)  # Default is True
checkbox_special_chars = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
checkbox_special_chars.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=generate_password_handler)
button_generate.pack(pady=10)

button_view_saved = tk.Button(root, text="View Saved Passwords", command=open_saved_passwords_window)
button_view_saved.pack(pady=10)

# Start the main loop of the interface
root.mainloop()
