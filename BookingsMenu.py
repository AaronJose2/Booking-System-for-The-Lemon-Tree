# imports the relevant modules and files that are necessary
from tkinter import *
from tkinter import nametowidget, winfo_toplevel
from pickle import *
from datastructures import *
from FontStyleSheet import *
from ListboxSave import *
from datetime import date, timedelta

#This subroutine and the window contained within will act as a sort of navigation page for administrative and normal users. 
#The window's main function is to let the user navigate to the relevant functions that would fall under the Bookings umbrella term.
#e.g. adding/viewing/editing/deleting booking details.

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
    viewBookingbtn = Button(BookingDetailsMenuWin, text="View Booking", font=BTN, command=viewBookingWindow)
    viewBookingbtn.pack()
    
    AddBookingbtn = Button(BookingDetailsMenuWin, text="Add a Booking", font=BTN, command=addBookingWindow)
    AddBookingbtn.pack()

    EditBookingbtn = Button(BookingDetailsMenuWin, text="Edit Booking Details", font=BTN, command=editBookingWindow)
    EditBookingbtn.pack()


    

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#This subroutine and the window contained within will display the bookings to the user
#e.g. adding/viewing/editing/deleting booking details.
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
    window = nametowidget(winfo_toplevel())
    viewBookingLB = Listbox(window, width=75, font=SH2)
    viewBookingLB.pack()

    viewBookingLBSave(viewBookingLB)

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
            #Validation
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
            #The first of which is here at Room ID.
            #Room ID does not need to be entered as it is already known as it was selected before, so we take that selection and get the roomID
            #It is then set to a String var and placed on the screen to avoid confusion with the user.
            roomIDlbl = Label(AddRestOfBookingWin, text= "Room ID", font=SH1)
            roomIDlbl.pack()
            roomIDentryvar = StringVar()
            roomIDent = Entry(AddRestOfBookingWin, textvariable=roomIDentryvar, font=EB)
            roomIDent.pack()
            roomIDentryvar.set(listRoom[index].roomID)

            #Another Exception is the function that creates an ID for the Booking
            #These subroutines simply get the length of the booking and adds one to get the place in the list that this booking would be
            #and that number is padded out with 0s to make it standardized.
            def genreateBookingID():
                prefix = "BG"
                ID = prefix + str(len(listBooking)+1).zfill(3)
                bookingIDvar.set(ID)

            bookingIDlbl = Label(AddRestOfBookingWin, text= "Booking ID", font=SH1)
            bookingIDlbl.pack()
            bookingIDvar = StringVar()
            bookingIDent= Entry(AddRestOfBookingWin, textvariable=bookingIDvar, font=EB)
            bookingIDent.pack()
            submitbtn = Button(AddRestOfBookingWin, text="Generate Booking ID", font=BTN, command=genreateBookingID)
            submitbtn.pack()
            
            #This subroutine contains a window with a listbox that allows the user to select a customerID.
            #The reason a listbox is used is for user ease
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

    #The button with the name view available rooms which is created below activates this subroutine
    #The purpose of this subroutine is to process the start and end date and generate a list populated with the dates between those two dates
    #This is possible thanks to the datetime module which was imported at the begining of this file
    def selectDate():
        global daylist
        start_date = selectIDateent.get()
        end_date = selectODateent.get()

        #the below removes the formatting of the date that the user would have inputted into the data.
        #In the future this will be replaced with a recurrsion loop
        start_date = start_date.replace("/","")  #removes / from the data that the user enters
        end_date = end_date.replace("/","")
        #The following variable reassignments are needed due to the module datetime uses a different date structure than the english language would use.
        start_date = date(int(str(20)+str(start_date[4:6])), int(start_date[2:4]), int(start_date[0:2]))
        end_date = date(int(str(20)+str(end_date[4:6])), int(end_date[2:4]), int(end_date[0:2]))

        delta = end_date - start_date   # returns difference in dates

        #the list which will contain all the dates between the start and end dates
        daylist = []
        # returns all of the dates between the two specified in list form and appends them to daylist
        for i in range(delta.days + 1): 
            day = start_date + timedelta(days=i) 
            day = str(day)
            daylist.append(day)

        #Clears the avaiable rooms listbox incase the function was ran before and changed and repopulates with the correct rooms
        addBookingLB.delete(0,END)

        for room in listRoom:
            addBookingLB.insert(END, room.roomName + room.guestLimit + str(room.familyRoom))
        # however if it is has data within it the following code is run.
        # Then checks if that booking contains a date that matches the current dates selected for booking
        # If so the system does not added it to the listbox but if it does not match it is added to the list box
        else: 
            for n in listRoom:
                for m in listBooking:
                    # It cycles through the list of rooms and bookings checking if the current room has a booking.
                    # A list of dates between the check in and checkout dates is generated by the same code that we saw before.
                    # This List is then checked against the list of dates for the new booking.
                    # If there is a match between the two the room is skipped and it moves to the next room.
                    if n.roomID == m.roomID:
                        check = 1
                        start_date = m.checkInDate
                        print(start_date)
                        end_date = m.checkOutDate
                        print(end_date)
                        start_date = start_date.replace("/","")
                        end_date = end_date.replace("/","")
                        start_date = date(int(str(20)+str(start_date[4:6])), int(start_date[2:4]), int(start_date[0:2]))
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
                            addBookingLB.insert(END, n.roomName + n.guestLimit + str(n.familyRoom))
                    else:
                        addBookingLB.insert(END, n.roomName + n.guestLimit + str(n.familyRoom))

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
    #e.g. adding/viewing/editing/deleting booking details.
    #Creates the New window named Administrative Menu.
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def editBookingWindow():
    global editBookingLB
    #creates the Booking Menu window
    EditBookingDetailsWin = Toplevel()
    EditBookingDetailsWin.geometry("650x400")
    EditBookingDetailsWin.title("Choose a Booking")

    # main title
    mainTitle = Label(EditBookingDetailsWin, text="Choose a Booking", font=Heading)
    mainTitle.pack()

    editBookingLB = Listbox(EditBookingDetailsWin, width=75, font=SH2)
    editBookingLB.pack()
    
    editBookingLBSave(editBookingLB)

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

                    # BookingsLBSave()

                    saveData()
                    EditBookingWin.withdraw()
            
        submitbtn = Button(EditBookingWin,text="submit changes", command = submitfunct)
        submitbtn.pack()
        
    editbtn = Button(EditBookingDetailsWin, text="Edit Record", command=editBooking)
    editbtn.pack()