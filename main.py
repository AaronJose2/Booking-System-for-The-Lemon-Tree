#importing necessary modules and files
from tkinter import *
import datastructures

# setting up the main window.
mainWin = Tk()
mainWin.geometry("400x400")
mainWin.title("Main Menu")

#importing the font styles from seperate file and other screens
from FontStyleSheet import *
from AdministratorScreen import *
# main title
mainTitle = Label(mainWin, text="Login", font=Heading)
mainTitle.pack()

#label and its respective entry for login function.
userIDlbl = Label(mainWin, text="User ID", font=SH1)
userIDlbl.pack()
userIDentry = Entry(mainWin, font=EB)
userIDentry.pack()
passwordlbl = Label(mainWin, text="Password", font=SH1)
passwordlbl.pack()
passwordentry = Entry(mainWin, font=EB)
passwordentry.pack()

#checkbox to see if the user is an admin
adminBool = IntVar()
adminCheckButton = Checkbutton(mainWin, text="Are you an Administrator", variable=adminBool)
adminCheckButton.pack()
#submit button and function that gets the inputs from the Entry boxes and validate and verfies them.
def getPassUserID():
    userID = userIDentry.get()
    password = passwordentry.get()

    print(adminBool.get())
    #validation and verification.
    print(userID, password)
    mainWin.withdraw()
    openAdminWindow()

passwordbtn = Button (mainWin, text="Let me innnnn", font=SH2, command=getPassUserID)
passwordbtn.pack()


mainWin.mainloop()