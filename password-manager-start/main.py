import tkinter
from tkinter import messagebox
from password_generator import password
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def store():
    address = website_entry.get()
    email = identification_entry.get()
    new = password_entry.get()
    new_data = {
        address: {
            "email": email,
            "password": new
        }
    }

    if email == "" or new == "" or address == "":
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                #Reading old data
                data_file = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            #Updating old data with new data
            data_file.update(new_data)

            with open("data.json", "w") as data:
                #Saving Updated data
                json.dump(data_file, data, indent=4)
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    address = website_entry.get()
    try:
        with open("data.json", "r") as data:
            data_file = json.load(data)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        # messagebox.showinfo(title="Confirmation", message=f"{data_file[address]}")
        if address in data_file:
            email = data_file[address]["email"]
            new = data_file[address]["password"]
            messagebox.showinfo(title="Confirmation", message=f"E-mail: {email}\nPassword: {new}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {address} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(height=200, width=200)
lock = tkinter.PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=lock)
canvas.grid(row=0, column=1)

#-----------Label------------#
website = tkinter.Label(text="Website")
website.grid(row=1, column=0)

identification = tkinter.Label(text="Email/Username")
identification.grid(row=2, column=0)

password_label = tkinter.Label(text="Password")
password_label.grid(row=3, column=0)

#-----------Entry------------#
website_entry = tkinter.Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()

identification_entry = tkinter.Entry(width=40)
identification_entry.grid(row=2, column=1, columnspan=2)
identification_entry.insert(0, "jun9894@naver.com")

password_entry = tkinter.Entry(width=22)
password_entry.grid(row=3, column=1)

website_search = tkinter.Button(text="Search", width=13, command=search)
website_search.grid(row=1, column=2)

password_generate = tkinter.Button(text="Generate Password", command=random_password)
password_generate.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=38, command=store)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()

