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
    pass

def addBookingWindow():
    AddBookingWin = Toplevel()
    AddBookingWin.geometry("400x400")
    AddBookingWin.title("Add a Booking")

    def restOfBooking():
        try:
            check = listRoom[0].datesBooked #ERRORrrrrrrrrr------------asfoa [eog;ocje`v;ochf…ø √®h;isuzhxcaoiduvfxigucuzhcvo;zoud zugh`]w

            for b in listRoom:
                n = 0
                temp = b.datesBooked
                print(temp)
                if daylist[0] == temp[n]:
                    print("found")
                else:
                    saveData()

        except:
            saveData()


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

        try:
            daylist = listRoom[0].datesBooked
        except:
            daylist = []

        for i in range(delta.days + 1): # returns all of the dates between the two specified in list form
            day = start_date + timedelta(days=i) 
            day = str(day)
            daylist.append(day)
            print(daylist[0])
            print(daylist)
        
        restOfBooking()

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

    for b in listRoom:
        print(b.datesBooked)


def editBookingWindow():
    pass