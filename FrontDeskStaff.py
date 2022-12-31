from tkinter import *
from FontStyleSheet import *
from CustomerDetailsMenu import *
from BookingsMenu import *
from TimetableMenu import *

def openFrontDeskWindow():
    #creates the Front Desk Menu window
    frontDeskWin = Toplevel()
    frontDeskWin.geometry("400x400")
    frontDeskWin.title("Holiday Menu")
    
    # main title
    mainTitle = Label(frontDeskWin, text="Front Desk Menu", font=Heading)
    mainTitle.pack()

    CustomerDetailsbtn = Button(frontDeskWin, text="Customer Details Menu", command=openCustomerDetailsMenuWindow)
    CustomerDetailsbtn.pack()

    BookingMenu = Button(frontDeskWin, text="Booking Menu", command=openBookingMenuWindow)
    BookingMenu.pack()

    TimetableMenubtn = Button(frontDeskWin, text="Timetable Menu", command=openTimetableMenuWindow)
    TimetableMenubtn.pack()