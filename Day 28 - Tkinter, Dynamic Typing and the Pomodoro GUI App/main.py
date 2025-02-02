from tkinter import *
import math

LIGHT_BLUE = "#A6CDC6"
DARK_YELLOW = "#DDA853"
DARK_BLUE= "#16404D"
LIGHT_YELLOW = "#FBF5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None #initially empty, needed for resetting timer

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config( text="Timer")
    check_marks_label.config(text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global worked_sessions

    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=DARK_YELLOW)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=LIGHT_BLUE)
        countdown(WORK_MIN * 60)
    else:
        title_label.config(text="Work", fg=DARK_BLUE)
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

"""
Dynamic typing: Show 00 instead of 0 when time is shown in the countdown. We can show a string "00"
when the seconds are equal to int 0. There is no type error, as dynamic typing allows us to change
the data type by dynamic typing.

Data types are very flexible in Python.
"""

def countdown(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds <10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1) #Inside of a variable so that it can be reset
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=LIGHT_YELLOW)


#title label
title_label = Label(window, text="Timer", fg=DARK_BLUE, bg=LIGHT_YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)


#Canvas widget
canvas = Canvas(window, width=200, height=224, bg=LIGHT_YELLOW, highlightthickness=0)
#PhotoImage reads file

image = PhotoImage(file="penguin.png")

canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 25, "bold"), fill="#16404D")
canvas.grid(column=1, row=1)

#buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


#check mark label
check_marks_label = Label(window, text="", fg=DARK_YELLOW, bg=LIGHT_YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks_label.grid(column=1, row=3)

window.mainloop()