from tkinter import *
from FontStyleSheet import *
def openAdminWindow():
    #creates the administrative window
    adminWin = Toplevel()
    adminWin.geometry("400x400")
    adminWin.title("Administrative Menu")
    # main title
    mainTitle = Label(adminWin, text="Administrative Window", font=Heading)
    mainTitle.pack()
    #buttons and respective subroutines that lead to new windows
    