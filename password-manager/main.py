from tkinter import *
from turtle import width
from tkinter import messagebox



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry= website_input.get()
    email_entry =email_input.get()
    password_entry= password_input.get()
    is_ok =messagebox.askokcancel(title= website_entry, message=f'Here are the details entered: \n email: {email_entry}'
                            f'\npassword: {password_entry}\n is it ok to save')

    if len(website_entry) == 0 or len(password_entry) ==0:
         messagebox.showinfo(title= 'Ooops', message='Please make you have not left any field empty')
    else:
        if is_ok:
            with open('login.txt', 'a') as file:
                file.write(F"websie:  {website_entry}\nEmail:  {email_entry}\nPassword: {password_entry}\n\n")
                website_input.delete(0, END)
                password_input.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()

windows.config(padx=20, pady=20)

windows.title('Password Manager ')
canvas= Canvas(width=200, height=200)
image= PhotoImage(file='logo.png')
canvas.create_image( 100, 100,  image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website", font=("courier", 12, ))
website.grid(column=0, row=1)

email = Label(text="Eamil/Username: ", font=("courier", 12, ))
email.grid(column=0, row=2)

password = Label(text="Password: ", font=("courier", 12, ))
password.grid(column=0, row=3)



website_input = Entry(width=38)
website_input.grid(column=1, columnspan=2,  row=1)
website_input.focus()

email_input = Entry(width=38)
email_input.grid(column=1, columnspan=2,  row=2)
email.config(padx=10, pady=10)

password_input = Entry(width=30)
password_input.grid(column=1,  row=3)


generate_password = Button(text="Generate Password", command='')
generate_password.grid(column=2, row=3)

add_password = Button(text="Add", command= save)
add_password.grid(column=1, columnspan=2, row=4)
add_password.config(width=36, )








windows.mainloop()