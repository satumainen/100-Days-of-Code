from tkinter import *
from tkinter import messagebox #needs to be imported separately
import password_generator
#to copy and paste the password
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    print("Generating password")
    password = password_generator.generate_password()
    #add generated password to password entry field
    pyperclip.copy(password) #copies password to the clipboard
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def on_add():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()

    #check for empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Oops", "Please fill all fields")

    else:
        #user confirmation
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it okay to save?")

        if is_ok:
            file = open('password_data.txt', 'a')
            file.write(f'{website} | {password} | {username}\n'"")
            file.close()
            #clear website and password
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

#labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#entries
website_entry = Entry(width=35)
website_entry.focus() #let's user type directly in here when app is opened
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)

username_entry = Entry(width=35)
username_entry.insert(0, "email@email.com") #give "my" e-mail as default
username_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1, sticky=EW)

#buttons
add_button = Button(text="Add", width=36, command=on_add)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=EW)


window.mainloop()

