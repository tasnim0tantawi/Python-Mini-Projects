from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password

    }}
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        is_ok = messagebox.askyesno(title= f"Save {website}", message=f"Do you want to save {website} with {email}"
                                                                      f" and {password}?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Writing into JSON file
                    # json.dump(new_data, data_file, indent=4)
                    # Reading from JSON file
                    json_data = json.load(data_file)
                    # Appending new data to JSON file
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                json_data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving data to JSON file
                    json.dump(json_data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    try:
        website = website_entry.get()
        with open("data.json", "r") as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found!")
    else:
        if website in json_data:
            found_email = json_data[website]["email"]
            found_password = json_data[website]["password"]
            email_entry.insert(0, found_email)
            password_entry.insert(0, found_password)
            messagebox.showinfo("Found", f"{website} was found in the database! \n Email: {found_email}"
                                         f"\nPassword: {found_password}")
        else:
            messagebox.showerror("Error", f"Website {website} not found!")


def generate_password():
    password = ""
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
               "L","M", "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]"]
    password_length = random.randint(10, 16)
    for i in range(password_length//3):
        password += random.choice(letters)
        password += random.choice(numbers)
        password += random.choice(special_characters)
    password = password.split()
    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)




window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "tasnim0tantawi@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=4)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search, width=13)
search_button.grid(row=1, column=4)

window.mainloop()