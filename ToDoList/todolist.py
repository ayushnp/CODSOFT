
import tkinter
from tkinter import *

root=Tk()
root.title('To-Do List')
root.geometry('400x650+400+100')
root.resizable(False,False)

task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("C:/Users/ayush/Downloads/New folder/tasklist.txt.txt",'a') as taskfile:
            taskfile.write(f'\n{task}')
        task_list.append(task)
        listbox.insert( END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("C:/Users/ayush/Downloads/New folder/tasklist.txt.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')

        listbox.delete(ANCHOR)
                
    

def openTaskfile():
    try:
        global task_list
        with open("C:/Users/ayush/Downloads/New folder/tasklist.txt.txt",'r') as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert( END, task)
    except:
        file=open("C:/Users/ayush/Downloads/New folder/tasklist.txt.txt",'w')
        file.close()
        

Image_icon=PhotoImage(file="C:/Users/ayush/Downloads/task.png")
root.iconphoto(False,Image_icon)

Top_image=PhotoImage(file="C:/Users/ayush/Downloads/topbar.png")
Label(root,image=Top_image).pack()

dockImage=PhotoImage(file="C:/Users/ayush/Downloads/dock.png")
Label(root,image=dockImage,bg='#32405b').place(x=35,y=25)

heading=Label(root,text='ALL TASKS',font="arial 20 bold",fg='white',bg='#32405b')
heading.place(x=130,y=20)

frame = Frame(root, width=400, height=50, bg='white')
frame.place(x=0, y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font='arial 25',bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text='ADD',font='arial 20 bold',width=6,bg='#5a95ff',fg='#fff',bd=0,command=addTask)
button.place(x=300,y=0)


new_frame=Frame(root,bd=3,width=800,height=280,bg='#32405b')
new_frame.pack(pady=(160,0))

listbox=Listbox(new_frame,font='arial 12',width=40,height=16,bg='#32405b',fg='white',cursor='hand2',selectbackground='#5a95ff')
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(new_frame)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskfile()

delete_icon=PhotoImage(file="C:/Users/ayush/Downloads/delete.png")
Button(root,image=delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)



root.mainloop()
 