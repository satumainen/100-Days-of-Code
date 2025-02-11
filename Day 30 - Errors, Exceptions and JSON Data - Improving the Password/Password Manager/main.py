import json
from tkinter import *
from tkinter import messagebox #needs to be imported separately
import password_generator
#to copy and paste the password
import pyperclip

"""
In the previous version of this code, the password data was saved in a text file. This project updates it to JSON.
JavaScriptObjectNotation was designed for JS, but is now used in many languages. JSON has the key value pair format,
which allows for searchin data.
- write: json.dump()
- read: json.load() 
    - converts JSON to dictionary
- update: json.update()
"""

# ------------------------------ FIND PASSWORD --------------------------------- #

def on_search():
    print("Searching for website...")
    website = website_entry.get()
    try:
        with open("password.json", "r") as password_file:
            password_data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No password file found, please add a password to create a file.")
    else:
        #teacher tip: if it easy to do with if and else, stick to them
        if website in password_data:
            username = password_data[website]["email"]
            password = password_data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username:  {username}\nPassword:  {password}")
        else:
            messagebox.showerror(title="Error", message="Password not found")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password = password_generator.generate_password()
    #add generated password to password entry field
    pyperclip.copy(password) #copies password to the clipboard
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def on_add():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()

    """
    New dictionary needed for the JSON format.
    """
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    #check for empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Oops", "Please fill all fields")

    else:
        try:
            with open("password.json", "r") as password_file:
                #Read old data
                data = json.load(password_file)
        except FileNotFoundError:
            with open("password.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open("password.json", "w") as password_file:
                # Save the updated data
                json.dump(data, password_file, indent=4)
        finally:
            # clear website and password fields
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
website_entry.grid(column=1, row=1, sticky=EW)

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

search_button = Button(text="Search", width=13, command=on_search)
search_button.grid(column=2, row=1, sticky=EW)

window.mainloop()

