import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import string

def Genpwd(length):
    char=string.ascii_letters + string.digits + string.punctuation

    password=' '.join((random.choice(char)) for _ in range(length))
    return password

def generate():
    length = int(len_entry.get())
    try:
        if length<=0:
            print('length should be an positive number..')
        else:
            pwd=Genpwd(length)
            result_label.config(text=f"Your password is: {pwd}")

    except ValueError:
        messagebox.showerror('invalid input,Try again.. ')

root=Tk()
root.title('Password Generator')
root.geometry('500x350')

gen_text=Label(root,text='Enter your desired password length..',font='arial 20')
gen_text.pack(pady=30)

len_entry=Entry(root,width=10,bd=10,font='arial 16',justify='center')
len_entry.pack(pady=1,ipady=10)

len_button=Button(root,text='Generate',font='arial 16',command=generate)
len_button.pack(pady=20)

result_label=Label(root,text=' ',font='arial 13')
result_label.pack(pady=10)

root.mainloop()


