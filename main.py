#importing necessary modules and files
from tkinter import *
from datastructures import *

loadData()

# setting up the main window.
mainWin = Tk()
mainWin.geometry("400x400")
mainWin.title("Main Menu")  

from FontStyleSheet import *
# main title
mainTitle = Label(mainWin, text="Login", font=Heading)
mainTitle.pack()

#label and its respective entry for login function.
from AdministratorScreen import *
from FrontDeskStaff import *
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
adminCheckbtn = Checkbutton(mainWin, text="Are you an Administrator", variable=adminBool)
adminCheckbtn.pack()

#submit button and function that gets the inputs from the Entry boxes and validate and verfies them.
def getPassUserID():
    global adminBool
    userID = userIDentry.get()
    password = passwordentry.get()

    if True:
        # add validation and verification of password and user name here for final implementation
        print(userID, password)
        mainWin.withdraw()
        openAdminWindow()
    else:
        mainWin.withdraw()
        openFrontDeskWindow()

passwordbtn = Button(mainWin, text="Login", font=BTN, command=getPassUserID)
passwordbtn.pack()

mainWin.mainloop()