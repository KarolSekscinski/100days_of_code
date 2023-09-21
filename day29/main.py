from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():

    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    if len(website_data) < 1 or len(password_data) < 1:
        messagebox.showinfo(title="Oopsie", message="Please don't leave empty fields.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Password Search ------------------------------- #
def find_password():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title=website_name, message="No Data File Found")
    else:
        if website_name in data:

            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title=website_name, message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=57)
email_entry.insert(0, "YOUR EMAIL")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, width=20)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=49, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=20)
search_button.grid(column=2, row=1)

window.mainloop()
