from tkinter import *
def openAdminWindow():
    #creates the administrative window
    AdminWin = Toplevel()
    AdminWin.geometry("400x400")
    AdminWin.title("Administrative Menu")
    # main title
    mainTitle = Label(mainWin, text="Login", font=Heading)
    mainTitle.pack()