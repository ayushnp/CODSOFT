import tkinter
from tkinter import messagebox
import random

root=Tk()
root.geometry('400x200+800+300')
root.title('Rock-Paper-Scissors')
root.resizable(False,False)


def play_game(user_choice):
    choices=['Rock','Paper','Scissors']
    computer_choice=random.choice(choices)

    if user_choice==computer_choice:
        message="It's a tie!!\nBetter luck next time.."

    elif(user_choice=='Rock' and computer_choice=='Scissors')or\
        (user_choice=='Scissors' and computer_choice=='Paper')or\
        (user_choice=='Paper' and computer_choice=='Rock'):
        message='You Win!!'

    else:
        message='You Lose!!\nBetter luck next time..'

    messagebox.showinfo('Result :',f"You chose {user_choice}\nComputer chose {computer_choice}\n{message}")


label = Label(root, text='Play The Game',font='arial 20')
label.pack()

choose_line =Label(root,text='Choose Rock,Paper or Scissors',font='arial 14')
choose_line.place(x=65,y=55)

Rock=Button(root,text='Rock',font='arial 12',width=11,bd=5,command=lambda:play_game('Rock'))
Rock.place(x=20,y=120)

Paper=Button(root,text='Paper',font='arial 12',width=11,bd=5,command=lambda:play_game('Paper'))
Paper.place(x=145,y=120)

Scissors=Button(root,text='Scissors',font='arial 12',width=11,bd=5,command=lambda:play_game('Scissors'))
Scissors.place(x=275,y=120)


root.mainloop()
