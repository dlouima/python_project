from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def calculate_miles():
    mile = float(user_input.get())
    km = round(mile * 1.609)
    result.config(text=f"{km}")

 # create the entry lebal to old the user import


user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=1, row=0)

# label *** set the equal statment
equal = Label(text="is equal to", font=("Arial", 13))
equal.grid(column=0, row=1)
equal.config(padx=20, pady=0)

# label 2. create the lebal to old the calculation
result = Label(text=" 0", font=("Arial", 13))
result.grid(column=1, row=1)

# labe 3
distance_in_Miles = Label(text=" Miles", font=("Arial", 13))
distance_in_Miles.grid(column=2, row=0)
distance_in_Miles.config(padx=10, pady=0)

# label 3
distance_in_KM = Label(text=" KM ", font=("Arial", 13))
distance_in_KM.grid(column=2, row=1)
distance_in_KM.config(padx=10, pady=0)
# button
button = Button(text="Calculate", command=calculate_miles)
button.grid(column=1, row=2)

window.mainloop()
