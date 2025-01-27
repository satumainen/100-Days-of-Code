import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

#label component
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "italic")) #does not yet show the label in the GUI
my_label.pack(side="left") #places label into the GUI



#place at bottom
#loop that listnens for user interaction:
window.mainloop() #keepts window on screen



