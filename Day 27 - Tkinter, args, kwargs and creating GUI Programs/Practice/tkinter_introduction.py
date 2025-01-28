from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

#label component
my_label = Label(text="I am a Label", font=("Arial", 20, "italic")) #does not yet show the label in the GUI
my_label.pack() #places label into the GUI

# https://docs.python.org/3/library/tkinter.html

#CHANGE TEXT
# my_label["text"] = "new text value" #change text value or like this:
#my_label.config(text="New text")

#CREATE BUTTON

def button_clicked():
    user_input = input.get() #get user input from input
    my_label.config(text=user_input)

button = Button(text="Click Me", command=button_clicked)
button.pack()
#event listener

#ENTRY (input)
input = Entry(width=10)
input.pack()



#place at bottom
#loop that listnens for user interaction:
window.mainloop() #keepts window on screen



