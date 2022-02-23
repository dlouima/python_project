from tkinter import *
from turtle import width
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()

    new_data = {
        website_entry: {
            'email': email_entry,
            'password': password_entry
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(
            title='Ooops', message='Please make you have not left any field empty')
    else:
        try:

            with open('login.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except:
            with open('login.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            with open('login.json', 'w') as file:
                json.dump(data, file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()

windows.config(padx=20, pady=20)

windows.title('Password Manager ')
canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100,  image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website", font=("courier", 12, ))
website.grid(column=0, row=1)

email = Label(text="Eamil/Username: ", font=("courier", 12, ))
email.grid(column=0, row=2)

password = Label(text="Password: ", font=("courier", 12, ))
password.grid(column=0, row=3)


website_input = Entry(width=35)
website_input.grid(column=1, columnspan=2,  row=1)
website_input.focus()

email_input = Entry(width=38)
email_input.grid(column=1, columnspan=2,  row=2)
email.config(padx=10, pady=10)
email_input.insert(0, 'samplemail@gmail.com')

password_input = Entry(width=21)
password_input.grid(column=1,  row=3)


generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add_password = Button(text="Add", command=save)
add_password.grid(column=1, columnspan=2, row=4)
add_password.config(width=36, )

search = Button(text="Search", command='')
search.grid(column=2, row=1)


windows.mainloop()
