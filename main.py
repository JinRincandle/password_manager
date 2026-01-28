import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import random
import string
import pyperclip
import pandas
import random_password

IMAGE_PATH = "photo3.jpg"
WIDTH = 450   #change these to get different size 
HEIGHT = 550

root = tk.Tk()
root.title("PASSWORD VAULT")
root.resizable(False, False)


image = Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT))
tk_image = ImageTk.PhotoImage(image)


canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.pack()


canvas.create_image(0, 0, image=tk_image, anchor="nw")

def save():
    name = e1.get()
    email = e2.get()
    password = e3.get()
    
    if not name or not email or not password:
        tk.messagebox.showwarning("Missing Information","Please fill in all fields!")
        return
          
    data=(f"Name of Website: {name}\n"
            f"Email: {email}\n"
            f"Password: {password}\n\n")        
    with open("password_data.txt", "a") as f:
        f.write(data) 

    #for json format
    new_data = {
        name:{
        "Email" : email,
        "Password" : password
        }
    }
    try:
        with open("password_data.json","r") as j_file:
            j_data = json.load(j_file)
    except (FileNotFoundError, json.JSONDecodeError):
        j_data = {}

    j_data.update(new_data)

    with open("password_data.json", "w") as j_file:
        json.dump(j_data, j_file, indent=4)

    e1.delete(0, tk.END)   
    e3.delete(0, tk.END)
    tk.messagebox.showinfo("Success", "Password saved successfully!")

def generate():
    
    password = random_password.generate()

    e3.delete(0, tk.END)
    e3.insert(0, password)   
        
def find():
    website = e1.get()
    if website =="":
        tk.messagebox.showwarning("Missing Information","Please fill in Website Box !")
        return
    try:
        with open("password_data.json","r") as j_file:
            data = json.load(j_file)
    except FileNotFoundError:
        tk.messagebox.showwarning("ERROR", "No Data File Found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            tk.messagebox.showinfo("SEARCH",f"For the searched website {website}\n"
                                   f"Email: {email}\nPassword: {password}")
        else:
            tk.messagebox.showwarning("ERROR",f"No details for {website} exists.")

    e1.delete(0, tk.END)
def copy():
    pyperclip.copy(e3.get())
    
#website
l1=tk.Label(text="WEBSITE",
            background="white",
            borderwidth=0,
            font=('Bold', 9),
            highlightthickness=0)
l1.place(x=100,y=250)
e1=tk.Entry(width=26,
            borderwidth=0,
            highlightcolor="black",
            highlightbackground="black",
            highlightthickness=1)
e1.place(x=167,y=250)
e1.focus()

#email
l2=tk.Label(text="EMAIL",
            borderwidth=0,
            background="white",
            font=('Bold', 9),
            highlightthickness=0)
l2.place(x=110,y=275)
e2=tk.Entry(width=39,
            borderwidth=0,
            highlightcolor="black",
            highlightbackground="black",
            highlightthickness=1)
e2.place(x=167,y=275)
e2.insert(0,"rajamhaider@gmail.com")

#password
l3=tk.Label(text="PASSWORD",
            borderwidth=1,
            background="white",
            font=('Bold', 9),
            highlightthickness=0)
l3.place(x=95,y=300)
e3=tk.Entry(width=26,
            borderwidth=0,
            highlightcolor="black",
            highlightbackground="black",
            highlightthickness=1)
e3.place(x=167,y=300)

#generate button
b1=tk.Button(text="GENERATE",
            width=10,
            borderwidth=1,
            background="white",
            relief="solid",
            font=('Arial', 9),
            activebackground="green",
            activeforeground="black",
            command=generate)
b1.place(x=328,y=297)

#add button
b2=tk.Button(text="ADD",
            width=33,
            borderwidth=1,
            background="white",
            relief="solid",
            font=('Arial', 9),
            activebackground="green",
            activeforeground="black",
            command=save)

b2.place(x=167,y=325)

#COPY
b3 = tk.Button(text="COPY PASSWORD",
            width=15,
            borderwidth=1,
            background="white",
            relief="solid",
            font=('Arial', 9),
            activebackground="green",
            activeforeground="black",
            command=copy)
b3.place(x=167,y=355)

#close
b4 = tk.Button(text="CLOSE",
            width=15,
            borderwidth=1,
            background="white",
            relief="solid",
            font=('Arial', 9),
            activebackground="green",
            activeforeground="black",
            command=root.destroy)
b4.place(x=290,y=355)

b5 = tk.Button(text="SEARCH",
            width=10,
            borderwidth=1,
            background="white",
            relief="solid",
            font=('Arial', 9),
            activebackground="green",
            activeforeground="black",
            command=find)
b5.place(x=328,y=250)


root.mainloop()
