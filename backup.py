from tkinter import *
from pickle import *
from datastructures import *
from FontStyleSheet import *
from ListboxSave import *
from test import *

from datetime import date, timedelta

def test():
    #creates the Booking Menu window
    EditBookingDetailsWin = Toplevel()
    EditBookingDetailsWin.geometry("650x400")
    EditBookingDetailsWin.title("Choose a Booking")

    # main title
    mainTitle = Label(EditBookingDetailsWin, text="Choose a Booking", font=Heading)
    mainTitle.pack()

    editBookingLB = Listbox(EditBookingDetailsWin, width=75, font=SH2)
    editBookingLB.pack()
    
    editBookingLB.delete(0,END)
    for booking in listBooking:  
        editBookingLB.insert(END, booking.bookingID +  " ~ " + listCustomer[int(booking.customerID[3:5])-1].forename + listCustomer[int(booking.customerID[3:5])-1].surname +  " ~ " + booking.checkInDate)

    def editBooking():
        #creates the entry boxes that are going to be populated from the data set that is chosen(highlighted) by the user.
        EditBookingWin = Toplevel()
        EditBookingWin.geometry("400x900")
        EditBookingWin.title("Edit Customer Details")

        bookingIDlbl = Label(EditBookingWin, text="Booking ID", font=SH1)
        bookingIDlbl.pack()
        bookingIDVar = StringVar()
        bookingIDent = Entry(EditBookingWin, textvariable=bookingIDVar)
        bookingIDent.pack()

        customerIDlbl = Label(EditBookingWin, text="Customer ID", font=SH1)
        customerIDlbl.pack()
        customerIDVar = StringVar()
        customerIDent = Entry(EditBookingWin, textvariable=customerIDVar)
        customerIDent.pack()

        roomIDlbl = Label(EditBookingWin, text="Room ID", font=SH1)
        roomIDlbl.pack()
        roomIDVar = StringVar()
        roomIDent = Entry(EditBookingWin, textvariable=roomIDVar)
        roomIDent.pack()

        checkInDatelbl = Label(EditBookingWin, text="Check In Date", font=SH1)
        checkInDatelbl.pack()
        checkInDateVar = StringVar()
        checkInDateent = Entry(EditBookingWin, textvariable=checkInDateVar)
        checkInDateent.pack()

        checkOutDatelbl = Label(EditBookingWin, text="Check Out Date", font=SH1)
        checkOutDatelbl.pack()
        checkOutDateVar = StringVar()
        checkOutDateent = Entry(EditBookingWin, textvariable=checkOutDateVar)
        checkOutDateent.pack()

        amountOfGuestslbl = Label(EditBookingWin, text="Amount of Guests", font=SH1)
        amountOfGuestslbl.pack()
        amountOfGuestsVar = StringVar()
        amountOfGuestsent = Entry(EditBookingWin, textvariable=amountOfGuestsVar)
        amountOfGuestsent.pack()

        breakfastRequiredlbl = Label(EditBookingWin, text="Breakfast Required", font=SH1)
        breakfastRequiredlbl.pack()
        breakfastRequiredVar = StringVar()
        breakfastRequiredent = Entry(EditBookingWin, textvariable=breakfastRequiredVar)
        breakfastRequiredent.pack()

        # The actual population of the entry boxes.
        if len(editBookingLB.curselection()) > 0:
            index = editBookingLB.curselection()[0]
            bookingIDVar.set(listBooking[index].bookingID)
            customerIDVar.set(listBooking[index].customerID)
            roomIDVar.set(listBooking[index].roomID)
            checkInDateVar.set(listBooking[index].checkInDate)
            checkOutDateVar.set(listBooking[index].checkOutDate)
            amountOfGuestsVar.set(listBooking[index].amountOfGuests)
            breakfastRequiredVar.set(listBooking[index].breakfastRequired)

        # This function saves all the data to the save file.
        def submitfunct():
                if True == True:
                    listBooking[index].bookingID = bookingIDent.get()
                    listBooking[index].customerID = customerIDent.get()
                    listBooking[index].roomID = roomIDent.get()
                    listBooking[index].checkInDate = checkInDateent.get()
                    listBooking[index].checkOutDate = checkOutDateent.get()
                    listBooking[index].amountOfGuests = amountOfGuestsent.get()
                    listBooking[index].breakfastRequired = breakfastRequiredent.get()

                    editBookingLB.delete(0,END)
                    for booking in listBooking:  
                        editBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)

                    saveData()
                    EditBookingWin.withdraw()
            
        submitbtn = Button(EditBookingWin,text="submit changes", command = submitfunct)
        submitbtn.pack()
        
    editbtn = Button(EditBookingDetailsWin, text="Edit Record", command=editBooking)
    editbtn.pack()