from tkinter import *

root=Tk()
root.title('Registration')#Title of the dialog box
root.geometry('600x470')#size of the dialog box
root.resizable(False,False)#the dialog box can't be resized outside the code
root.iconphoto(False,
PhotoImage(file='C:/Users/Umoren Joshua/Music/Tkinter/Icon/icons8-document-writer-16.png'))
#enter your own icon ocation path, best have it in the same folder with your python documnent


def regiaster():
  if Label
    print('Registered')# this will print when the regiseter button is clicked.

#filling in the content of the box (i.e) Entry. and packing
Label(root, text="Registration Form",font='arial 25').pack(pady=50)
Label(text='Name',font=23).place(x=100, y=150)#place is location of the Label 'name'
Label(text='Phone',font=23).place(x=100, y=200)
Label(text='Gender',font=23).place(x=100, y=250)
Label(text='Email',font=23).place(x=100, y=300)

nameValue=StringVar()#the name value should be converted to becoming a string for printing
PhoneValue=StringVar()
genderValue=StringVar()
emailValue=StringVar()

nameEntry=Entry(root, textvariable=nameValue, width=30, bd=2, font=20)
nameEntry.place(x=200, y=150)

phoneEntry=Entry(root, textvariable=nameValue, width=30, bd=2, font=20)
phoneEntry.place(x=200, y=200)

genderEntry=Entry(root, textvariable=nameValue, width=30, bd=2, font=20)
genderEntry.place(x=200, y=250)

emailEntry=Entry(root, textvariable=nameValue, width=30, bd=2, font=20)
emailEntry.place(x=200, y=300)

checkValue=IntVar
checkbtn=Checkbutton(text='remember mr?', variable=checkValue)
checkbtn.place(x=200, y=340)

Button(text='Register', font=20, width=11, height=2).place(x=250,y=380, command=register)

root.mainloop()
