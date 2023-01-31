from tkinter import *
from pickle import *
from datastructures import *
from FontStyleSheet import *
from datetime import date, timedelta

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

def viewBookingWindow():
    ViewBookingWin = Toplevel()
    ViewBookingWin.geometry("650x600")
    ViewBookingWin.title("Bookings")

    listBookingLB = Listbox(ViewBookingWin, width=75, font=SH2)
    listBookingLB.pack()

    roomIDlbl = Label(ViewBookingWin, text= "View Bookings", font=SH1)
    roomIDlbl.pack()

    for booking in listBooking:  
        listBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)

def addBookingWindow():
    AddBookingWin = Toplevel()
    AddBookingWin.geometry("400x600")
    AddBookingWin.title("Choose a Date and Room")

    def restOfBooking():
        AddRestOfBookingWin = Toplevel()
        AddRestOfBookingWin.geometry("400x600")
        AddRestOfBookingWin.title("Enter Details")

        def savefunct():
            #validation
            if True == True:
                newBooking = booking()
                newBooking.bookingID = bookingIDent.get()
                newBooking.customerID = CustomerIDentry.get()
                newBooking.roomID = roomIDent.get()
                newBooking.checkInDate = selectIDateent.get()
                newBooking.checkOutDate = selectODateent.get()
                newBooking.amountOfGuests = NumGuestentry.get()

                if BreakReqVar.get() == 1:
                    newBooking.breakfastRequired = True
                else:
                    newBooking.breakfastRequired = False

                listBooking.append(newBooking)
                AddRestOfBookingWin.withdraw()
                AddBookingWin.withdraw()
                saveData()

        if len(listRoomLB.curselection()) > 0:
            index = listRoomLB.curselection()[0]

            roomIDlbl = Label(AddRestOfBookingWin, text= "Room ID", font=SH1)
            roomIDlbl.pack()
            roomIDentryvar = StringVar()
            roomIDent = Entry(AddRestOfBookingWin, textvariable=roomIDentryvar, font=EB)
            roomIDent.pack()
            roomIDentryvar.set(listRoom[index].roomID)

            def genreateRoomID():
                prefix = "BG"
                ID = prefix + str(len(listBooking)+1).zfill(3)
                bookingIDvar.set(ID)

            bookingIDlbl = Label(AddRestOfBookingWin, text= "Booking ID", font=SH1)
            bookingIDlbl.pack()
            bookingIDvar = StringVar()
            bookingIDent= Entry(AddRestOfBookingWin, textvariable=bookingIDvar, font=EB)
            bookingIDent.pack()
            submitbtn = Button(AddRestOfBookingWin, text="Generate Booking ID", font=BTN, command=genreateRoomID)
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
                    listCustomerLB.insert(END, customer.customerID + customer.forename + customer.surname)

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
            CustomerIDentry= Entry(AddRestOfBookingWin, textvariable=CustomerIDvar, font=EB)
            CustomerIDentry.pack()
            CustomerIDSelectionbtn = Button(AddRestOfBookingWin, text="Select Customer ID", font=BTN, command=customerIDSelection)
            CustomerIDSelectionbtn.pack()

            NumGuestlbl = Label(AddRestOfBookingWin, text="Number of Guests", font=SH1)
            NumGuestlbl.pack()
            NumGuestvar = IntVar()
            NumGuestentry= Entry(AddRestOfBookingWin, textvariable=NumGuestvar, font=EB)
            NumGuestentry.pack()

            BreakReqVar = IntVar()
            BreakReqbtn = Checkbutton(AddRestOfBookingWin, text="Do you require Breakfast?", variable=BreakReqVar)
            BreakReqbtn.pack()

            submitbtn = Button(AddRestOfBookingWin, text= "Select", font=BTN, command=savefunct)
            submitbtn.pack()

    def selectDate():
        global daylist
        start_date = selectIDateent.get()
        end_date = selectODateent.get()

        #replace with recursion loop
        start_date = start_date.replace("/","")  #removes / from the data that the user enters
        end_date = end_date.replace("/","")

        start_date = date(int(str(20)+str(start_date[4:6])), int(start_date[2:4]), int(start_date[0:2])) #reformats the data to a format that the module datetime understands but is still common sense to the user
        end_date = date(int(str(20)+str(end_date[4:6])), int(end_date[2:4]), int(end_date[0:2]))

        delta = end_date - start_date   # returns difference in dates

        daylist = []

        for i in range(delta.days + 1): # returns all of the dates between the two specified in list form
            day = start_date + timedelta(days=i) 
            day = str(day)
            daylist.append(day)

        listRoomLB.delete(0,END)

        if len(listBooking) == 0:
            for room in listRoom:
                listRoomLB.insert(END, room.roomName + room.guestLimit + str(room.familyRoom))

        else: # the following cycles through the list of rooms and bookings checking if the current room has a booking and then checks if that booking contains a date that matches the current dates selected for booking if so the system does not added it to the listbox but if it does not match it is added to the list box
            for n in listRoom:
                for m in listBooking:
                    if n.roomID == m.roomID:
                        check = 1
                        start_date = m.checkInDate
                        print(start_date)
                        end_date = m.checkOutDate
                        print(end_date)
                        start_date = start_date.replace("/","")
                        end_date = end_date.replace("/","")
                        start_date = date(int(str(20)+str(start_date[4:6])), int(start_date[2:4]), int(start_date[0:2])) #reformats the data to a format that the module datetime understands but is still common sense to the user
                        end_date = date(int(str(20)+str(end_date[4:6])), int(end_date[2:4]), int(end_date[0:2]))

                        delta = end_date - start_date

                        temp = []

                        for i in range (delta.days + 1):
                            day = start_date + timedelta(days=i)
                            day = str(day)
                            temp.append(day)
                        
                        for z in temp:
                            for x in daylist:
                                if str(z) == str(x):
                                    check = 0
                        if check == 1:
                            listRoomLB.insert(END, n.roomName + n.guestLimit + str(n.familyRoom))
                    else:
                        listRoomLB.insert(END, n.roomName + n.guestLimit + str(n.familyRoom))

    mainTitle = Label(AddBookingWin, text="Add a Booking", font= Heading)
    mainTitle.pack()

    selectIDatelbl = Label(AddBookingWin, text="Select a Check in Date", font=SH1)
    selectIDatelbl.pack()

    selectIDateent = Entry(AddBookingWin, font=EB)
    selectIDateent.pack()

    selectODatelbl = Label(AddBookingWin, text="Select a Check out Date", font=SH1)
    selectODatelbl.pack()

    selectODateent = Entry(AddBookingWin, font=EB)
    selectODateent.pack()

    selectDatebtn = Button(AddBookingWin, text="View Available Rooms", font=BTN, command=selectDate)
    selectDatebtn.pack()

    selectRoomlbl = Label(AddBookingWin, text="The Available Rooms Are Below.", font=SH1)
    selectRoomlbl.pack()

    listRoomLB = Listbox(AddBookingWin, font=SH2)
    listRoomLB.pack()

    selectDatebtn = Button(AddBookingWin, text="Select Room", font=BTN, command=restOfBooking)
    selectDatebtn.pack()

def editBookingWindow():
    #creates the Booking Menu window
    EditBookingDetailsWin = Toplevel()
    EditBookingDetailsWin.geometry("650x400")
    EditBookingDetailsWin.title("Choose a Booking")

    # main title
    mainTitle = Label(EditBookingDetailsWin, text="Choose a Booking", font=Heading)
    mainTitle.pack()

    listBookingLB = Listbox(EditBookingDetailsWin, width=75, font=SH2)
    listBookingLB.pack()

    listBookingLB.delete(0,END)
    for booking in listBooking:  
        listBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)

    def editBooking():
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

        if len(listBookingLB.curselection()) > 0:
            index = listBookingLB.curselection()[0]
            bookingIDVar.set(listBooking[index].bookingID)
            customerIDVar.set(listBooking[index].customerID)
            roomIDVar.set(listBooking[index].roomID)
            checkInDateVar.set(listBooking[index].checkInDate)
            checkOutDateVar.set(listBooking[index].checkOutDate)
            amountOfGuestsVar.set(listBooking[index].amountOfGuests)
            breakfastRequiredVar.set(listBooking[index].breakfastRequired)

        def submitfunct():
                if True == True:
                    listBooking[index].bookingID = bookingIDent.get()
                    listBooking[index].customerID = customerIDent.get()
                    listBooking[index].roomID = roomIDent.get()
                    listBooking[index].checkInDate = checkInDateent.get()
                    listBooking[index].checkOutDate = checkOutDateent.get()
                    listBooking[index].amountOfGuests = amountOfGuestsent.get()
                    listBooking[index].breakfastRequired = breakfastRequiredent.get()

                    listBookingLB.delete(0,END)
                    for booking in listBooking:  
                        listBookingLB.insert(END, booking.bookingID +  " | " + listCustomer[int(booking.customerID[3:5])-1].forename +  " | " + listCustomer[int(booking.customerID[3:5])-1].surname +  " | " + booking.checkInDate +  " | " + booking.checkOutDate +  " | " + booking.roomID)

                    saveData()
                    EditBookingWin.withdraw()
            
        submitbtn = Button(EditBookingWin,text="submit changes", command = submitfunct)
        submitbtn.pack()
        
    editbtn = Button(EditBookingDetailsWin, text="Edit Record", command=editBooking)
    editbtn.pack()