from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(200, 150)
window.config(padx=20, pady=20)

def button_clicked():
    miles = float(input.get()) #get user input from input
    km = miles * 1.609
    show_km_label.config(text=f"{km}")


# label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=5, pady=5)

show_km_label = Label(text="")
show_km_label.grid(column=1, row=1)
show_km_label.config(padx=5, pady=5)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

# button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)


# input field
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)



window.mainloop() #keepts window on screen



