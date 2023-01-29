from pickle import *

class staff():
  staffID = "" #PK
  staffFName = ""
  staffLName = ""
  jobTitle = ""
  dateJoined = ""
  DOB = ""
  tNum = ""
  emerContName = ""
  emerContNum = ""
  staffPostcode = ""
  staffAddressLine1 = ""
  staffAddressLine2 = ""
  staffCity = ""

class customer():
  customerID = "" #PK
  forename = ""
  surname = ""
  telephoneNum = ""
  postcode = ""
  addressLine1 = ""
  addressLine2 = ""
  city = ""

class room():
  roomID = "" #PK
  roomName = ""
  guestLimit = ""
  familyRoom = bool()
  ppp = 0
  
class booking():
  bookingID = "" #PK
  customerID = "" #FK
  roomID = "" #FK
  checkInDate = ""
  checkOutDate = ""
  amountOfGuests = 0
  breakfastRequired = bool()

class holiday():
  holidayID = ""
  name = ""
  startDate = ""
  endDate = ""

def loadData():
  global listStaff, listCustomer, listRoom, listBooking, listHoliday
  try:
    fh = open("LemonTree.pickle","rb")
    listStaff = load(fh)
    listCustomer = load(fh)
    listRoom = load(fh)
    listBooking =  load(fh)
    listHoliday = load(fh)
    fh.close()
  except:
    listStaff = []
    listCustomer = []
    listRoom = []
    listBooking = []
    listHoliday = []

def saveData():
  fh = open("LemonTree.pickle","wb")
  dump(listStaff, fh)
  dump(listCustomer, fh)
  dump(listRoom, fh)
  dump(listBooking, fh)
  dump(listHoliday, fh)
  fh.close()