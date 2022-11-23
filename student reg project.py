from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
#from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox

# import Workbook
import pathlib
from pathlib import Path


background='#06283D'
framebg='#EDEDED'
framefg='#06283D'

root=Tk()
root.title('Student Register System')
root.geometry('1250x700+210+100')
root.config(bg=background)
root.iconphoto(False, PhotoImage(file='C:/Users/Umoren Joshua/Music/Tkinter/Student.png'))

file=os.path.basename('C:/Users/Umoren Joshua/Music/Tkinter/registrer.xlsx')
# if  file in Path('c:/Users/Umoren Joshua/Music/kinter/Worksheet-Form.xlsx'):
#     pass
# else:
#     # file=Workbook()
#     sheet=file.active
#     sheet['A1']='Registration N0.'
#     sheet['B1']='Name.'
#     sheet['C1']='Class.'
#     sheet['D1']='Gender.'
#     sheet['E1']='DOB.'
#     sheet['F1']='Date of Registration.'
#     sheet['G1']='Religion.'
#     sheet['H1']='Skill.'
#     sheet['I1']='Father Name.'
#     sheet['J1']='Mother Name.'
#     sheet['K1']="Father's occupation."
#     sheet['L1']="Mother's occupation."
    
#     file.save('C:/Users/Umoren Joshua/Music/kinter/Worksheet-Form.xlsx')

Label(root, text='Email: Tkinter@gmail.ngn', width=10, height=2,
bg='#f0687c', anchor='e').pack(side=TOP,fill=X)
Label(root, text='STUDENT REGISTRATION', height=2, bg='#c36464',
fg='#fff', font='arial 20 bold').pack(side=TOP,fill=X)



imageicon3=PhotoImage(file='C:/Users/Umoren Joshua/Music/Tkinter/scope.png')
Button(text='Search', font=20, width=123, height=20, command=LEFT,
# Search=Button(root, text='Search', font='arial 13 bold', compound=LEFT,
image=imageicon3,bg='#68ddfa', fg='#fff').place(x=1110,y=60)

Search=StringVar()
Search_Entrt=Entry(root, textvariable=Search, width=15, bd=2, font='arial 20').place(x=870,y=53)



imageicon4=PhotoImage(file='C:/Users/Umoren Joshua/Music/Tkinter/Refresh.png')
update_button=Button(root, image=imageicon4, bg='#c36464')
update_button.place(x=110,y=64)

Label(root, text='Registration N0:', font='arial 13', fg=framebg, bg=background
).place(x=30,y=150)

Registration=StringVar()
Reg_Entry=Entry(root, textvariable=Registration, font='arial 10', width= 15
).place(x=160,y=150)

Label(root, text='Date:', font='arial 13', fg=framebg, bg=background
).place(x=500,y=500)

Date=StringVar()







root.mainloop()
