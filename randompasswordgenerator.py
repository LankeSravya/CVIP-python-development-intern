import tkinter as tk
from tkinter import StringVar
from random import choice
def generate_password9():
    specialchars9 = "!@#$%^&*- _~+-="
    digits9="0123456789"
    uppercase9="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase9="abcdefghijklmnopqrstuvwxyz"
    allchars9=digits9+uppercase9+lowercase9+specialchars9
    passwordlength9= 12 
    password9= ''.join(choice(allchars9) for _ in range(passwordlength9))
    return password9
root = tk.Tk()
root.title('PASSWORD GENERATOR')
root.geometry("400x90") 
passwordvar9 = StringVar()
def click_generate9():
    password9= generate_password9()
    passwordvar9.set(password9)
passwordlabel9 = tk.Label(root, textvariable=passwordvar9, font=("Bold", 18), padx=10, pady=5)
passwordlabel9.pack()
generatebutton9 = tk.Button(root, text="GENERATE", command=click_generate9, font=("Italian", 14))
generatebutton9.pack()
root.mainloop()
