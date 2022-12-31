class staff():
  staffID = "" #PK
  forename = ""
  surname = ""
  jobTitle = ""
  dateJoined = ""
  dateOfBirth = ""
  telephoneNumber = ""
  emergencyContactNumber = ""
  staffPostcode = ""
  staffAddressLine1 = ""
  staffAddressLine2 = ""
  staffCity = ""

class customer():
  customerID = "" #PK
  forename = ""
  surname = ""
  telephoneNum = ""
  customerPostcode = ""
  customerAddressLine1 = ""
  customerAddressLine2 = ""
  customerCity = ""

class room():
  roomNumber = "" #PK
  roomName = ""
  guestLimit = ""
  familyRoom = bool()
  ppp = 0
  
class booking():
  customerID = "" #FK
  roomNumber = "" #FK
  checkInDate = ""
  checkOutDate = ""
  amountOfGuests = 0
  breakfastRequired = bool()
  dateBooked = ""
