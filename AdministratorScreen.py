from tkinter import *
from FontStyleSheet import *
from CustomerDetailsMenu import *
from BookingsMenu import *
from StaffDetailsMenu import *
from HolidayMenu import *
from RoomMenu import *

def openAdminWindow():
    #creates the administrative window
    adminWin = Toplevel()
    adminWin.geometry("400x400")
    adminWin.title("Administrative Menu")

    # main title
    mainTitle = Label(adminWin, text="Administrative Window", font=Heading)
    mainTitle.pack()

    #buttons and respective subroutines that lead to new windows
    def withdraw():
        adminWin.withdraw()
    
    #CustomerDetailsMenubtn = Button(adminWin, text="Customer Details Menu", command=lambda: [openCustomerDetailsMenuWindow(),withdraw()] )
    #CustomerDetailsMenubtn.pack()
    CustomerDetailsMenubtn = Button(adminWin, text="Customer Details Menu", font=BTN, command=CustomerDetailsMenuWin)
    CustomerDetailsMenubtn.pack()

    BookingsMenubtn = Button(adminWin, text="Booking Menu", font=BTN, command=openBookingMenuWindow)
    BookingsMenubtn.pack()

    StaffDetailsMenubtn = Button(adminWin, text="Staff Details Menu", font=BTN, command=openStaffDetailsMenuWindow)
    StaffDetailsMenubtn.pack()

    HolidayMenubtn = Button(adminWin, text="Holiday Menu", font=BTN, command=openHolidayMenuWindow)
    HolidayMenubtn.pack()

    RoomMenubtn = Button(adminWin, text="Room Menu", font=BTN, command=openRoomMenuWindow)
    RoomMenubtn.pack()
    
    