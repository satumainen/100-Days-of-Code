from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
TIMER = 3000 #3 seconds to figure out answer

current_card = {}
to_learn = {}
#------------------------------------- IMPORT CSV ---------------------------------------------

"""
The code will run the original CSV french_words.csv. If the user has practiced with the app 
previously, the user will continue to practice the words that they did not mark as known.
"""

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")


#------------------------------------- FUNCTIONS ----------------------------------------------

def next_card():
    """Fills the card with a new random word, gives user 3 seconds to guess answer"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=current_card["French"], fill="black")
    flash_card.itemconfigure(card_img, image=card_front_img)
    flip_timer = window.after(TIMER, flip_card)


def flip_card():
    """Flips the card to show the answer in English"""
    flash_card.itemconfig(card_title, fill="white")
    flash_card.itemconfig(card_word, fill="white")
    flash_card.itemconfig(card_title, text="English")
    flash_card.itemconfig(card_img, image=card_back_img)
    flash_card.itemconfig(card_word, text=current_card["English"])

def is_known():
    """Removes known words from the training dictionary"""
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False) #does not add indexes to created csv
    next_card()


#----------------------------------------- UI -------------------------------------------------

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(TIMER, func=flip_card)

#Flash card Canvas
flash_card = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = flash_card.create_image(400, 263, image=card_front_img)
flash_card.grid(column=0, row=0, columnspan=2)
card_title = flash_card.create_text(400, 150, text="French", font=LANGUAGE_FONT)
card_word = flash_card.create_text(400, 263, text="placeholder", font=WORD_FONT)

#Buttons
incorrect_img = PhotoImage(file="images/wrong.png")
incorrect_button = Button(window, image=incorrect_img, command=next_card)
incorrect_button.grid(column=0, row=1)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(window, image=correct_img, command=is_known)
correct_button.grid(column=1, row=1)

#initialize flash card app with a first word
next_card()

window.mainloop()
