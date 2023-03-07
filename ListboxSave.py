from tkinter import *
from datastructures import *

#This for loop iterates through the items in the array listBooking and inserts the data within that record into the list box
def viewBookingLBSave(viewBookingLB):
    #This subroutine aims to keep every instance of a listbox upto date concurently
    viewBookingLB.delete(0,END)
    for booking in listBooking:  
        viewBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)

def editBookingLBSave(editBookingLB):
    editBookingLB.delete(0,END)
    for booking in listBooking:  
        editBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)



    # try:
    #     addBookingLB.delete(0,END)
    #     for booking in listBooking:  
    #             addBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)
    # except:
    #     pass

    # try:
    #     editBookingLB.delete(0,END)
    #     for booking in listBooking:  
    #             editBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)
    # except:
    #     pass

    # try:
    #     viewBookingLB.delete(0,END)
    #     for booking in listBooking:  
    #             viewBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)
    # except:
    #     pass