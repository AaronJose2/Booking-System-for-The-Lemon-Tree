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
  customerID = "" #FK
  roomID = "" #FK
  checkInDate = ""
  checkOutDate = ""
  amountOfGuests = 0
  breakfastRequired = bool()
  dateBooked = ""

def loadData():
  global listStaff, listCustomer, listRoom, listBooking
  try:
    fh = open("LemonTree.pickle","rb")
    listStaff = load(fh)
    listCustomer = load(fh)
    listRoom = load(fh)
    listBooking =  load(fh)
    fh.close()
  except:
    listStaff = []
    listCustomer = []
    listRoom = []
    listBooking = []

def saveData():
  fh = open("LemonTree.pickle","wb")
  dump(listStaff, fh)
  dump(listCustomer, fh)
  dump(listRoom, fh)
  dump(listBooking, fh)
  fh.close()