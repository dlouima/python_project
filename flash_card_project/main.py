from textwrap import fill
from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
data = {}
current_card = ''
try:
    file_data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    data = original_data.to_dict(orient="records")

else:
    data = file_data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(data)
    french_word = current_card['French']
    canvas.itemconfig(card_word, text=french_word, fill='black')
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(canvas_image, image=image)
    flip_timer = windows.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=new_image)
    english_word = current_card['English']
    canvas.itemconfig(card_word, text=english_word, fill='white')
    canvas.itemconfig(card_title, text='English', fill='white')


def master_word_list():
    data.remove(current_card)
    next_card()
    word_list = pd.DataFrame(data)
    word_list.to_csv('data/words_to_learn.csv')


# ************************** SET UP**************
windows = Tk()

windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000, func=flip_card)

windows.title('French Learn Made Easy ')
canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file='./images/card_front.png')
new_image = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263,  image=image)
canvas.grid(column=0, columnspan=2, row=0)
card_title = canvas.create_text(
    400, 150, text='', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(
    400, 263, text='', font=('Arial', 60, 'bold'))

red_image = PhotoImage(file="./images/wrong.png")
red_button = Button(image=red_image, highlightthickness=0, command=next_card)
red_button.grid(row=1, column=0)

green_image = PhotoImage(file="./images/right.png")
green_button = Button(
    image=green_image, highlightthickness=0, command=master_word_list)
green_button.grid(row=1, column=1)
next_card()


windows.mainloop()
