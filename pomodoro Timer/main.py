import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
TIMER = None

# reset the timer

def rest_timer():

    windows.after_cancel(TIMER)
    timer_clock.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    checked_mark.config(tex = '')
    global reps
    reps = 0


# set count down timer


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_clock.config(text='Long Break', fg=RED)
    elif reps% 2 == 0:
        count_down(short_break)
        timer_clock.config(text= 'Short Break', fg =PINK)

    else:
        count_down(work_sec)
        timer_clock.config(text='Work', fg=GREEN)

#countdown logic


def  count_down(count):
    global  TIMER

    count_minute = math.floor(count/60)
    count_sec= count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_minute}:{count_sec}")
    if count > 0:
        TIMER = windows.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
            mark += '✔'
        checked_mark.config(text=mark)


# GUI setup
windows = Tk()
windows.config(padx=100, pady=50,bg=YELLOW)

windows.title("Pomotoro Timer")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)

timer_text = canvas.create_text( 100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)


timer_clock = Label(text="Timer", font=(FONT_NAME, 38, "bold"), fg= GREEN, bg=YELLOW)
timer_clock.grid(column=1, row=0)

checked_mark = Label(font=("Arial", 20, "bold"), fg= GREEN, bg=YELLOW)
checked_mark.grid(column=1, row=4)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", command= rest_timer)
reset.grid(column=2, row=3)

windows.mainloop()
