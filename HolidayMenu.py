from tkinter import *
from pickle import *
from datastructures import *
from FontStyleSheet import *

def openHolidayMenuWindow():
    #creates the Holiday Menu window
    holidaysMenuWin = Toplevel()
    holidaysMenuWin.geometry("400x400")
    holidaysMenuWin.title("Holiday Menu")
    
    # main title
    mainTitle = Label(holidaysMenuWin, text="Booking Menu", font=Heading)
    mainTitle.pack()

    viewHolidaybtn = Button(holidaysMenuWin, text="View Booking", font=BTN, command=viewHolidays)
    viewHolidaybtn.pack()
    
    AddHolidaybtn = Button(holidaysMenuWin, text="Add a Booking", font=BTN, command=addHolidays)
    AddHolidaybtn.pack()

    EditHolidaybtn = Button(holidaysMenuWin, text="Edit Booking Details", font=BTN, command=editHolidays)
    EditHolidaybtn.pack()

def viewHolidays():
    pass

def addHolidays():
    addHolidaysWin = Toplevel()
    addHolidaysWin.geometry("400x400")
    addHolidaysWin.title("Add a Holiday")

    # main title
    mainTitle = Label(addHolidaysWin, text="Add Customer", font=Heading)
    mainTitle.pack()

    def generateHolidayID():
        prefix = "HD"
        ID = prefix + str(len(listHoliday)+1).zfill(3)
        holidayIDvar.set(ID)
    
    holidayIDlbl = Label(addHolidaysWin, text="Add a Holiday ID", font=SH1)
    holidayIDlbl.pack()
    holidayIDvar = StringVar()
    holidayIDent = Entry(addHolidaysWin, textvariable=holidayIDvar, font=EB)
    holidayIDent.pack()
    holidayIDbtn = Button(addHolidaysWin, text="Generate ID", font=BTN, command=generateHolidayID)
    holidayIDbtn.pack()

    holidayNamelbl = Label(addHolidaysWin, text="Holiday Name", font=SH1)
    holidayNamelbl.pack()
    holidayNameent = Entry(addHolidaysWin, font=EB)
    holidayNameent.pack()

    dateslbl = Label(addHolidaysWin, text="Holiday Date", font=SH1)
    dateslbl.pack()
    datesent = Entry(addHolidaysWin, font=EB)
    datesent.pack()

    holidaySDateslbl = Label(addHolidaysWin, text="Holiday Start Date", font = SH1)
    holidaySDateslbl.pack()
    holidaySDatesent = Entry(addHolidaysWin, font=EB)
    holidaySDatesent.pack()

    holidayEDatelbl = Label(addHolidaysWin, text="Holiday End Date", font=SH1)
    holidayEDatelbl.pack()
    holidayEDateent = Entry(addHolidaysWin, font=EB)
    holidayEDateent.pack()

    def submitHoliday():
        if True == True:
            newHoliday = holiday()
            newHoliday.holidayID = holidayIDent.get()
            newHoliday.name = holidayNameent.get()
            newHoliday.startDate = holidayEDateent.get()
            newHoliday.endDate = holidaySDatesent.get()
            listHoliday.append(newHoliday)
            saveData()

    holidaySubmitbtn = Button(addHolidaysWin, text="Submit Holiday", font=BTN, command=submitHoliday)
    holidaySubmitbtn.pack()

def editHolidays():
    ChooseCustomerWin = Toplevel()
    ChooseCustomerWin.geometry("650x400")
    ChooseCustomerWin.title("Choose an Holiday's Details to Edit")

    mainTitle = Label()
    mainTitle.pack()