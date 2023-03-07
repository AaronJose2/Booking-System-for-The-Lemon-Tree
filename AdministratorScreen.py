# imports the relevant modules and files that are necessary
from tkinter import *
from FontStyleSheet import *
from CustomerDetailsMenu import *
from BookingsMenu import *
from StaffDetailsMenu import *
from HolidayMenu import *
from RoomMenu import *
from TimetableMenu import *

def openAdminWindow():
    #Creates the New window named Administrative Menu. 
    #This window will act as a sort of home/landing page for administrative users. 
    #The window's main function is to let the user navigate to the relevant functions of the program.
    #e.g. adding/viewing/editing/deleting booking/customer/staff/room/holiday details 
    adminWin = Toplevel()
    adminWin.geometry("400x400")
    adminWin.title("Administrative Menu")

    #Creates a Title/Heading for the Window that says Administrative Window
    #It is formatted to the font style Heading
    mainTitle = Label(adminWin, text="Administrative Window", font=Heading)
    mainTitle.pack()

    #The below creates and packs buttons to the screen that once pressed activate different subroutines that reside in other files
    #The buttons are formatted with the style BTN which is abreviated from BUTTON
    CustomerDetailsMenubtn = Button(adminWin, text="Customer Details Menu", font=BTN, command=CustomerDetailsMenuWindow)
    CustomerDetailsMenubtn.pack()

    BookingsMenubtn = Button(adminWin, text="Booking Menu", font=BTN, command=openBookingMenuWindow)
    BookingsMenubtn.pack()

    StaffDetailsMenubtn = Button(adminWin, text="Staff Details Menu", font=BTN, command=openStaffDetailsMenuWindow)
    StaffDetailsMenubtn.pack()

    HolidayMenubtn = Button(adminWin, text="Holiday Menu", font=BTN, command=openHolidayMenuWindow)
    HolidayMenubtn.pack()

    RoomMenubtn = Button(adminWin, text="Room Menu", font=BTN, command=openRoomMenuWindow)
    RoomMenubtn.pack()
    
    TimetableMenubtn = Button(adminWin, text="Timetable Menu", font=BTN, command=openTimetableMenuWindow)
    TimetableMenubtn.pack()
    