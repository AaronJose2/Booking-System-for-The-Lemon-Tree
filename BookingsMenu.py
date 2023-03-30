# imports the relevant modules and files that are necessary
from tkinter import *
from tkinter import messagebox
from pickle import *
from datastructures import *
from FontStyleSheet import *

from datetime import date, timedelta

#This subroutine and the window contained within will act as a sort of navigation page for administrative and normal users. 
#The window's main function is to let the user navigate to the relevant functions that would fall under the Bookings umbrella term.
#e.g. adding/viewing/deleting booking details.

def openBookingMenuWindow():
    global viewBookingLB

    #Creates the New window named Administrative Menu. 
    BookingDetailsMenuWin = Toplevel()
    BookingDetailsMenuWin.geometry("400x400")
    BookingDetailsMenuWin.title("Booking Menu")

    #Creates a Title/Heading for the Window that says Booking Menu.
    #It is formatted to the font style Heading.
    mainTitle = Label(BookingDetailsMenuWin, text="Booking Menu", font=Heading)
    mainTitle.pack()

    #The code below creates and packs buttons to the screen that once pressed activate different subroutines that reside further down in the file.
    #The buttons are formatted with the style BTN which is abreviated from BUTTON.

    AddBookingbtn = Button(BookingDetailsMenuWin, text="Create a new Booking", font=BTN, command=addBookingWindow)
    AddBookingbtn.pack()

    viewBookingbtn = Button(BookingDetailsMenuWin, text="View Bookings", font=BTN, command=viewBookingWindow)
    viewBookingbtn.pack()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This subroutine and the window contained within will display the bookings to the user
#e.g. adding/viewing/deleting booking details.
def viewBookingWindow():
    #Creates a new Window named Bookings
    ViewBookingWin = Toplevel()
    ViewBookingWin.geometry("650x600")
    ViewBookingWin.title("Bookings")

    #Creates a Title/Heading for the Window that says View Bookings.
    #It is formatted to the font style Heading.
    roomIDlbl = Label(ViewBookingWin, text= "View Bookings", font=Heading)
    roomIDlbl.pack()

    # This creates a List Box which will visualise the 3 dimensional array for the user.
    # Using this the user will be able to select a record in that array.    
    # window = _default_root.nametowidget(winfo_toplevel())
    viewBookingLB = Listbox(ViewBookingWin, width=75, font=SH2) 
    viewBookingLB.pack()
    viewBookingLB.delete(0,END)
    for booking in listBooking:  
        viewBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This subroutine and the other subroutines and windows contained within will let the user add bookings to the save file.
def addBookingWindow():
    global addBookingLB
    #Creates a new Window named Add Booking
    AddBookingWin = Toplevel()
    AddBookingWin.geometry("400x600")
    AddBookingWin.title("Add Booking")

    def restOfBooking():
        #Creates a new Window named Ender Details
        AddRestOfBookingWin = Toplevel()
        AddRestOfBookingWin.geometry("400x600")
        AddRestOfBookingWin.title("Enter Details")
        
        #When called the following fuction creates a new list using the booking class and then populates it with the booking data.
        #This data is then appended to the main list.
        #The function saveData() is then called which saves the list to the file.
        def savefunct():
                    
            if True == True:
                newBooking = booking()
                newBooking.bookingID = bookingIDent.get()
                newBooking.customerID = CustomerIDentry.get()
                newBooking.roomID = roomIDent.get()
                newBooking.checkInDate = selectIDateent.get()
                newBooking.checkOutDate = selectODateent.get()
                newBooking.amountOfGuests = NumGuestentry.get()

                #Changes the numerical answer into a boolean one.
                if BreakReqVar.get() == 1:
                    newBooking.breakfastRequired = True
                else:
                    newBooking.breakfastRequired = False

                listBooking.append(newBooking)
                AddRestOfBookingWin.withdraw()
                AddBookingWin.withdraw()
                saveData()

        #Checks to see if the user has slected something from the listbox
        if len(addBookingLB.curselection()) > 0:
            #getting an index number for the selected piece of data
            index = addBookingLB.curselection()[0]

            #The following code generates a label and entry for the booking data with a few exceptions
            bookingIDlbl = Label(AddRestOfBookingWin, text= "Booking ID", font=SH1)
            bookingIDlbl.pack()
            bookingIDvar = StringVar()
            bookingIDent= Entry(AddRestOfBookingWin, textvariable=bookingIDvar, font=EB, state='readonly')
            bookingIDent.pack()

            #Room ID does not need to be entered as it is already known as it was selected before, so we take that selection and get the roomID
            #It is then set to a String var and placed on the screen to avoid confusion with the user.
            roomIDlbl = Label(AddRestOfBookingWin, text= "Room ID", font=SH1)
            roomIDlbl.pack()
            roomIDentryvar = StringVar()
            roomIDent = Entry(AddRestOfBookingWin, textvariable=roomIDentryvar, font=EB, state='readonly')
            roomIDent.pack()
            roomIDentryvar.set(addBookingLB.get(index)[:5])

            #Another Exception is the function that creates an ID for the Booking
            #it simply gets the length of the booking and adds one to get the place in the list that this booking would be
            #and that number is padded out with 0s to make it standardized.
            prefix = "BG"
            ID = prefix + str(len(listBooking)+1).zfill(3)
            bookingIDvar.set(ID)
            
            #This subroutine contains a window with a listbox that allows the user to select a customerID.
            #The reason a listbox is used is for user ease
            def customerIDSelection():
                CustomerIDMenuWin = Toplevel()
                CustomerIDMenuWin.geometry("400x400")
                CustomerIDMenuWin.title("Customer ID Selection Menu")

                #
                mainTitle = Label(CustomerIDMenuWin, text= "Choose Customer ID", font=Heading)
                mainTitle.pack()

                listCustomerLB = Listbox(CustomerIDMenuWin, font=SH2, width=40)
                listCustomerLB.pack()

                listCustomerLB.delete(0,END)
                for customer in listCustomer:
                    listCustomerLB.insert(END, customer.customerID +" "+ customer.forename +" "+ customer.surname)

                def addCustomerID():
                    if len(listCustomerLB.curselection()) > 0:
                        index = listCustomerLB.curselection()[0]

                    CustomerIDvar.set(listCustomer[index].customerID)
                    CustomerIDMenuWin.withdraw()

                submitbtn = Button(CustomerIDMenuWin, text= "Select", font=BTN, command=addCustomerID)
                submitbtn.pack()

            CustomerIDlbl = Label(AddRestOfBookingWin, text="Customer ID", font=SH1)
            CustomerIDlbl.pack()
            CustomerIDvar = StringVar()
            CustomerIDentry= Entry(AddRestOfBookingWin, textvariable=CustomerIDvar, font=EB,  state='readonly')
            CustomerIDentry.pack()
            CustomerIDSelectionbtn = Button(AddRestOfBookingWin, text="Select Customer ID", font=BTN, command=customerIDSelection)
            CustomerIDSelectionbtn.pack()

            NumGuestlbl = Label(AddRestOfBookingWin, text="Number of Guests", font=SH1)
            NumGuestlbl.pack()
            NumGuestvar = IntVar()
            NumGuestentry= Entry(AddRestOfBookingWin, textvariable=NumGuestvar, font=EB)
            NumGuestentry.pack()

            NumGuestvar.set(1)

            BreakReqVar = IntVar()
            BreakReqbtn = Checkbutton(AddRestOfBookingWin, text="Do you require Breakfast?", variable=BreakReqVar)
            BreakReqbtn.pack()

            submitbtn = Button(AddRestOfBookingWin, text= "Select", font=BTN, command=savefunct)
            submitbtn.pack()

    #The button with the name view available rooms which is created below activates this subroutine
    #The purpose of this subroutine is to process the start and end date and generate a list populated with the dates between those two dates
    #This is possible thanks to the datetime module which was imported at the begining of this file
    def selectDate():
        try:
            addBookingLB.delete(0, END)
        except:
            pass
        # this gets the start and end date of the proposed booking from the entry boxes and then removes and reformats them to a style that the datetime module prefers
        new_booking_start_date = selectIDateent.get()
        new_booking_end_date = selectODateent.get()
        new_booking_start_date = new_booking_start_date.replace("/","")
        new_booking_end_date = new_booking_end_date.replace("/","")
        new_booking_start_date = new_booking_start_date.replace("-","")
        new_booking_end_date = new_booking_end_date.replace("-","")

        InDateCheck = True
        try:
            new_booking_start_date = date(int(str(20)+str(new_booking_start_date[4:6])), int(new_booking_start_date[2:4]), int(new_booking_start_date[0:2]))
            new_booking_end_date = date(int(str(20)+str(new_booking_end_date[4:6])), int(new_booking_end_date[2:4]), int(new_booking_end_date[0:2]))
            # the daylist list will hold all the temporary dates inbetween the start and end date for the proposed booking
            daylist = []
            # the delta variable counts how many days between the start and end date
            delta = new_booking_end_date - new_booking_start_date
        except:
            messagebox.showerror("Wait!", "There is something wrong with the dates \n please use the format dd/mm/yy or dd-mm-yy")
            InDateCheck = False
        
        confirmation = "yes"
        if int(delta.days) > 31:
            confirmation = messagebox.askquestion("Wait!", "Are you sure you want to make a booking thats more than a month long?", icon="warning")
        if int(delta.days) < 0:
            messagebox.showerror("Wait!", "The Check Out Date occurs before the Check In Date")
        if InDateCheck == False:
            pass
        if confirmation == "no":
            pass
        else:
            
            # the for loop below populates the above daylist with the dates
            for i in range(delta.days + 1): 
                day = new_booking_start_date + timedelta(days=i) 
                day = str(day)
                daylist.append(day)
            
            for r in listRoom:
                addBookingLB.insert(END, r.roomID +" "+ r.roomName +" "+ r.guestLimit +" "+ str(r.familyRoom))

            # these for loops and if statements search forf if the proposed booking would clash with any previously made bookings.
            # the first few for loops and if statements iterate through all the bookings one by one comparing them to every room, 
            # if a booking and a room share the same ID then they are given a check value of 0
            # then the check is carried out to see if the proposed booking clashes
            # this is done by getting the palced booking's check in and out date; 
            # formatting them and then checking if any of the dates contained within the daylist we created earlier
            # are within the in and out date
            # if they are we can set the check digit to 1
            # once all the days within the daylist have been iterated through we can check the status of the check digit.
            # if the digit is still 0 we can go ahead and add that room to the listbox
            # if not then we dont
            # if the roomIDs
            temptemp = []
            for b in listBooking:
                for r in listRoom:
                    if r.roomID == b.roomID:
                        check = 0
                        for n in daylist:
                            b_checkInDate = b.checkInDate.replace("/","")
                            b_checkOutDate = b.checkOutDate.replace("-","")
                            b_checkInDate = date(int(str(20)+str(b_checkInDate[4:6])), int(b_checkInDate[2:4]), int(b_checkInDate[0:2]))
                            b_checkOutDate = date(int(str(20)+str(b_checkOutDate[4:6])), int(b_checkOutDate[2:4]), int(b_checkOutDate[0:2]))
                            if str(b_checkInDate) <= n <= str(b_checkOutDate):
                                check = 1
                                break
                        if check == 1:
                            try:
                                temp = addBookingLB.get(0,END).index(r.roomID +" "+ r.roomName +" "+ r.guestLimit +" "+ str(r.familyRoom))
                                addBookingLB.delete(temp)
                            except:
                                pass
    #Creates a Title/Heading for the Window that says Add a Booking.
    #It is formatted to the font style Heading.
    mainTitle = Label(AddBookingWin, text="Add a Booking", font= Heading)
    mainTitle.pack()

    #Creates a Label and Entry box that asks the user to input the checkin and out dates and allows the user to input the data respectively.
    selectIDatelbl = Label(AddBookingWin, text="Select a Check in Date", font=SH1)
    selectIDatelbl.pack()
    
    selectIDateent = Entry(AddBookingWin, font=EB)
    selectIDateent.pack()

    selectODatelbl = Label(AddBookingWin, text="Select a Check out Date", font=SH1)
    selectODatelbl.pack()

    selectODateent = Entry(AddBookingWin, font=EB)
    selectODateent.pack()

    #This button activates a subroutine that allows the user to view the available rooms.
    selectDatebtn = Button(AddBookingWin, text="View Available Rooms", font=BTN, command=selectDate)
    selectDatebtn.pack()

    selectRoomlbl = Label(AddBookingWin, text="The Available Rooms Are Below.", font=SH1)
    selectRoomlbl.pack()

    addBookingLB = Listbox(AddBookingWin, font=SH2)
    addBookingLB.pack()

    selectDatebtn = Button(AddBookingWin, text="Select Room", font=BTN, command=restOfBooking)
    selectDatebtn.pack()

    #This subroutine and the window contained within will act as a sort of navigation page for administrative and normal users. 
    #The window's main function is to let the user navigate to the relevant functions that would fall under the Bookings umbrella term.
    #e.g. adding/viewing/deleting booking details.
    #Creates the New window named Administrative Menu.
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def viewBookingWindow():
    ChooseBookingWin = Toplevel()
    ChooseBookingWin.geometry("650x400")
    ChooseBookingWin.title("Choose a Booking to View")

    # main title
    mainTitle = Label(ChooseBookingWin, text="View Booking Details", font=Heading)
    mainTitle.pack()

    listBookingLB = Listbox(ChooseBookingWin, font=SH2, width=75)
    listBookingLB.pack()

    BookingList = []
    for booking in listBooking:
        appendage = []
        appendage.append(booking.bookingID)
        appendage.append(booking.customerID)
        appendage.append(booking.roomID)
        appendage.append(booking.checkInDate)
        appendage.append(booking.checkOutDate)
        appendage.append(booking.amountOfGuests)
        appendage.append(booking.breakfastRequired)
        BookingList.append(appendage)
    
    sortList = BookingList

    def display():
        listBookingLB.delete(0,END)
        for booking in BookingList:
            for customer in listCustomer:
                if booking[1] == customer.customerID:
                    break

            for room in listRoom:
                if booking[2] == room.roomID:
                    break

            listBookingLB.insert(END, booking[0] +" ~ "+ booking[1] +" "+ customer.forename +" "+ customer.surname +" ~ "+ booking[2] +" "+ room.roomName +" ~ "+ booking[3] +" "+ booking[4])

    display()

    def bookingidSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j]>sortList[j+1]):
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()          
        
    def customeridSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j][1] > sortList[j+1][1]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()

    def dateSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j][3] > sortList[j+1][3]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()

    bookingidSortBtn = Button(ChooseBookingWin, text="Sort by Booking ID", command=bookingidSort)
    bookingidSortBtn.pack()

    customeridSortBtn = Button(ChooseBookingWin, text="Sort by Customer ID", command=customeridSort)
    customeridSortBtn.pack()

    dateSortBtn = Button(ChooseBookingWin, text="Sort by Check In Date", command=dateSort)
    dateSortBtn.pack()

    def viewBooking():
        def deleteMode():
            confirmation = messagebox.askquestion("Wait!", "Are you sure you want to delete that?", icon="warning")

            if confirmation == "yes":
                customerForenamevar.set("#Deleted#")
                customerSurnamevar.set("#Deleted#")
                customerTelephoneNumvar.set("#Deleted#")
                customerPostcodevar.set("#Deleted#")
                customerAddressLine1var.set("#Deleted#")
                customerAddressLine2var.set("#Deleted#")
                customerCityvar.set("#Deleted#")

                newBooking = booking()
                newBooking.bookingID = bookingIDent.get()
                newBooking.customerID = bookingCustomerIDent.get()
                newBooking.roomID = roomIDent.get()
                newBooking.checkInDate = selectIDateent.get()
                newBooking.checkOutDate = selectODateent.get()
                newBooking.amountOfGuests = NumGuestentry.get()
                newBooking.breakfastRequired = bookingBreakfastRequiredent.get()

                listBooking.append(newBooking)
                saveData()

        if len(listBookingLB.curselection()) > 0:
            index = listBookingLB.curselection()[0]

            ViewBookingWin = Toplevel()
            ViewBookingWin.geometry("400x520")
            ViewBookingWin.title("View Booking Details")

            bookingIDlbl = Label(ViewBookingWin, text="Booking ID", font=SH1)
            bookingIDlbl.pack()
            bookingIDvar = StringVar()
            bookingIDent = Entry(ViewBookingWin, textvariable=bookingIDvar, font=EB, state='readonly')
            bookingIDent.pack()
            bookingIDvar.set(listBooking[index].bookingID)

            bookingCustomerIDlbl = Label(ViewBookingWin, text="Customer ID", font=SH1)
            bookingCustomerIDlbl.pack()
            bookingCustomerIDvar = StringVar()
            bookingCustomerIDent = Entry(ViewBookingWin, textvariable=bookingCustomerIDvar, font=EB, state='readonly')
            bookingCustomerIDent.pack()
            bookingCustomerIDvar.set(listBooking[index].customerID)

            bookingCustomerNamelbl = Label(ViewBookingWin, text="Customer Full Name", font=SH1)
            bookingCustomerNamelbl.pack()
            bookingCustomerNamevar = StringVar()
            bookingCustomerNameent = Entry(ViewBookingWin, textvariable=bookingCustomerNamevar, font=EB, state='readonly')
            bookingCustomerNameent.pack()
            for customer in listCustomer:
                if listBooking[index].customerID == customer.customerID:                    
                    bookingCustomerNamevar.set(str(customer.forename) +" "+ str(customer.surname) )

            bookingRoomIDlbl = Label(ViewBookingWin, text="RoomID", font=SH1)
            bookingRoomIDlbl.pack()
            bookingRoomIDvar = StringVar()
            bookingRoomIDent = Entry(ViewBookingWin, textvariable=bookingRoomIDvar, font=EB, state='readonly')
            bookingRoomIDent.pack()
            bookingRoomIDvar.set(listBooking[index].roomID)

            bookingRoomNamelbl = Label(ViewBookingWin, text="Room Name", font=SH1)
            bookingRoomNamelbl.pack()
            bookingRoomNamevar = StringVar()
            bookingRoomNameent = Entry(ViewBookingWin, textvariable=bookingRoomNamevar, font=EB, state='readonly')
            bookingRoomNameent.pack()
            for room in listRoom:
                if listBooking[index].roomID == room.roomID:                    
                    bookingRoomNamevar.set(room.roomName)
                    
            bookingCheckInDatelbl = Label(ViewBookingWin, text="Check In Date", font=SH1)
            bookingCheckInDatelbl.pack()
            bookingCheckInDatevar = StringVar()
            bookingCheckInDateent = Entry(ViewBookingWin, textvariable=bookingCheckInDatevar, font=EB, state='readonly')
            bookingCheckInDateent.pack()
            bookingCheckInDatevar.set(listBooking[index].checkInDate)

            bookingCheckOutDatelbl = Label(ViewBookingWin, text="Check Out Date", font=SH1)
            bookingCheckOutDatelbl.pack()
            bookingCheckOutDatevar = StringVar()
            bookingCheckOutDateent = Entry(ViewBookingWin, textvariable=bookingCheckOutDatevar, font=EB, state='readonly')
            bookingCheckOutDateent.pack()
            bookingCheckOutDatevar.set(listBooking[index].checkOutDate)

            bookingAmountOfGuestslbl = Label(ViewBookingWin, text="Amount of Guests", font=SH1)
            bookingAmountOfGuestslbl.pack()
            bookingAmountOfGuestsvar = StringVar()
            bookingAmountOfGuestsent = Entry(ViewBookingWin, textvariable=bookingAmountOfGuestsvar, font=EB, state='readonly')
            bookingAmountOfGuestsent.pack()
            bookingAmountOfGuestsvar.set(listBooking[index].amountOfGuests)

            bookingBreakfastRequiredlbl = Label(ViewBookingWin, text="Breakfast Required", font=SH1)
            bookingBreakfastRequiredlbl.pack()
            bookingBreakfastRequiredvar = StringVar()
            bookingBreakfastRequiredent = Entry(ViewBookingWin, textvariable=bookingBreakfastRequiredvar, font=EB, state='readonly')
            bookingBreakfastRequiredent.pack()
            bookingBreakfastRequiredvar.set(listBooking[index].breakfastRequired)

    viewbtn = Button(ChooseBookingWin, text="View Booking", command = viewBooking)
    viewbtn.pack()
