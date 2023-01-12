from tkinter import *
import calendar
from pickle import *
from datastructures import *
from FontStyleSheet import *

def openBookingMenuWindow():
    #creates the Booking Menu window
    BookingDetailsMenuWin = Toplevel()
    BookingDetailsMenuWin.geometry("400x400")
    BookingDetailsMenuWin.title("Booking Menu")

    # main title
    mainTitle = Label(BookingDetailsMenuWin, text="Booking Menu", font=Heading)
    mainTitle.pack()

    viewBookingbtn = Button(BookingDetailsMenuWin, text="View Booking", font=BTN, command=viewBookingWindow)
    viewBookingbtn.pack()
    
    AddBookingbtn = Button(BookingDetailsMenuWin, text="Add a Booking", font=BTN, command=addBookingWindow)
    AddBookingbtn.pack()

    EditBookingbtn = Button(BookingDetailsMenuWin, text="Edit Booking Details", font=BTN, command=editBookingWindow)
    EditBookingbtn.pack()

    Calendarbtn = Button(BookingDetailsMenuWin, text="Edit Booking Details", font=BTN, command=calendar)
    Calendarbtn.pack()

def viewBookingWindow():
    pass

def addBookingWindow():
    #creates the View Booking window
    AddBookingWin = Toplevel()
    AddBookingWin.geometry("400x600")
    AddBookingWin.title("Add Booking")

    # main title
    mainTitle = Label(AddBookingWin, text="Add Booking", font=Heading)
    mainTitle.pack()

    #labels and respseective entries.
    def genreateBookingID():
        prefix = "BG"
        ID = prefix + str(len(listBooking)+1).zfill(3)
        BookingIDvar.set(ID)

    BookingIDlbl = Label(AddBookingWin, text="Booking ID", font=SH1)
    BookingIDlbl.pack()
    BookingIDvar = StringVar()
    BookingIDentry= Entry(AddBookingWin, textvariable=BookingIDvar, font=EB)
    BookingIDentry.pack()
    submitbtn = Button(AddBookingWin, text="Generate Booking ID", font=BTN, command=genreateBookingID)
    submitbtn.pack()

    def customerIDSelection():
        CustomerIDMenuWin = Toplevel()
        CustomerIDMenuWin.geometry("400x400")
        CustomerIDMenuWin.title("Customer ID Selection Menu")

        # main title
        mainTitle = Label(CustomerIDMenuWin, text= "Choose Customer ID", font=Heading)
        mainTitle.pack()

        listCustomerLB = Listbox(CustomerIDMenuWin, font=SH2)
        listCustomerLB.pack()

        listCustomerLB.delete(0,END)
        for customer in listCustomer:
            listCustomerLB.insert(END, customer.customerID + customer.surname)

        def addCustomerID():
            if len(listCustomerLB.curselection()) > 0:
                index = listCustomerLB.curselection()[0]

            CustomerIDvar.set(listCustomer[index].customerID)

            CustomerIDMenuWin.withdraw()

        submitbtn = Button(CustomerIDMenuWin, text= "Select", font=BTN, command=addCustomerID)
        submitbtn.pack()

    CustomerIDlbl = Label(AddBookingWin, text="Customer ID", font=SH1)
    CustomerIDlbl.pack()
    CustomerIDvar = StringVar()
    CustomerIDentry= Entry(AddBookingWin, textvariable=CustomerIDvar, font=EB)
    CustomerIDentry.pack()
    CustomerIDSelectionbtn = Button(AddBookingWin, text="Select Customer ID", font=BTN, command=customerIDSelection)
    CustomerIDSelectionbtn.pack()

    def roomIDSelection():
        RoomIDMenuWin = Toplevel()
        RoomIDMenuWin.geometry("400x400")
        RoomIDMenuWin.title("Room ID Selection Menu")

        # main title
        mainTitle = Label(RoomIDMenuWin, text= "Choose Room ID", font=Heading)
        mainTitle.pack()

        listRoomLB = Listbox(RoomIDMenuWin, font=SH2)
        listRoomLB.pack()

        listRoomLB.delete(0,END)
        for room in listRoom:
            listRoomLB.insert(END, room.roomID + room.roomName)

        def addRoomID():
            if len(listRoomLB.curselection()) > 0:
                index = listRoomLB.curselection()[0]

            RoomIDvar.set(listRoom[index].roomID)

            RoomIDMenuWin.withdraw()

        submitbtn = Button(RoomIDMenuWin, text= "Select", font=BTN, command=addRoomID)
        submitbtn.pack()

    RoomIDlbl = Label(AddBookingWin, text="Room ID", font=SH1)
    RoomIDlbl.pack()
    RoomIDvar = StringVar()
    RoomIDentry= Entry(AddBookingWin, textvariable=RoomIDvar, font=EB)
    RoomIDentry.pack()
    RoomIDSelectionbtn = Button(AddBookingWin, text="Select Room ID", font=BTN, command=roomIDSelection)
    RoomIDSelectionbtn.pack()


def editBookingWindow():

    pass

class CalendarWidget(Frame):
    def __init__(self, parent, year, month, **kwargs):
        super().__init__(parent, **kwargs)

        self.cal_frame = Frame(self)
        self.cal_frame.pack(side="top", fill="x")

        self.redraw(year, month)

    def redraw(self, year, month):
        '''Redraws the calendar for the given year and month'''

        for child in self.cal_frame.winfo_children():
            child.destroy()

        # day of the week headings
        for col, day in enumerate(("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")):
            label = Label(self.cal_frame, text=day)
            label.grid(row=0, column=col, sticky="nsew")

        # buttons for each day
        cal = calendar.monthcalendar(year, month)
        for row, week in enumerate(cal):
            for col, day in enumerate(week):
                text = "" if day == 0 else day
                state = "normal" if day > 0 else "disabled"
                cell = Button(self.cal_frame, text=text, state=state, command=lambda day=day: self.set_day(day))
                cell.grid(row=row+1, column=col, sticky="nsew")

    def set_day(self, num):
        print(f"you selected day {num}")

def calendar():
    calendarWin = Toplevel()
    c = CalendarWidget(calendarWin, year=2022, month=4, bd=2, relief="groove")
    c.pack(padx=4, pady=4)