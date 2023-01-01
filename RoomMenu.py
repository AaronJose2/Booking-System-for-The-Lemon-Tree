from tkinter import *
from FontStyleSheet import *
def openRoomMenuWindow():
    #creates the Room Menu window
    openRoomMenuWin = Toplevel()
    openRoomMenuWin.geometry("400x400")
    openRoomMenuWin.title("Room Menu")
    
    # main title
    mainTitle = Label(openRoomMenuWin, text="Room Menu", font=Heading)
    mainTitle.pack()

    viewRoombtn = Button(openRoomMenuWin, text="View Rooms",font=BTN)
    viewRoombtn.pack()
    
    AddRoombtn = Button(openRoomMenuWin, text="Add a Room",font=BTN)
    AddRoombtn.pack()

    EditRoombtn = Button(openRoomMenuWin, text="Edit Rooms",font=BTN)
    EditRoombtn.pack()