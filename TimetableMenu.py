from pickle import *
import os
import webbrowser
import datetime
from datetime import date
from datastructures import *


def openTimetableMenuWindow():
  fh = open("template.html","r")
  template = fh.read()
  fh.close()

  i = 0
  headerinsert = "<th> n </th>"
  while i < 7 :
    tempdate = date.today() + datetime.timedelta(days=i)
    temp = "<th>" + str(tempdate) + "</th>"
    headerinsert += temp
    i += 1

  sortedlistBooking = []
  for booking in listBooking:
    print(booking.roomID)
    temp = []
    temp.append(booking.bookingID)
    temp.append(booking.customerID)
    temp.append(booking.roomID)
    temp.append(booking.checkInDate)
    temp.append(booking.checkOutDate)
    temp.append(booking.amountOfGuests)
    temp.append(booking.breakfastRequired)
    sortedlistBooking.append(temp)
  

  def bubble_sort(sortedlistBooking):
    for i in range(0, len(sortedlistBooking)-1):  
        for j in range(len(sortedlistBooking)-1):
          if(sortedlistBooking[j][2][2:5]>sortedlistBooking[j+1][2][2:5]):  
            temp = sortedlistBooking[j]
            sortedlistBooking[j] = sortedlistBooking[j+1]  
            sortedlistBooking[j+1] = temp
    return sortedlistBooking

  bodyinsert = ""
  sortedlistBooking = bubble_sort(sortedlistBooking)

  for booking in sortedlistBooking:
    rowinsert = "<tr>"
    temp = "<td>" + booking[2] + "</td>"
    rowinsert += temp
    i = 0
    while i < 7 :
      tempdate = date.today() + datetime.timedelta(days=i)
      start_date = booking[3]
      end_date = booking[4]
      start_date = start_date.replace("/","")
      end_date = end_date.replace("/","")
      start_date = date(int(str(20)+str(start_date[4:6])), int(start_date[2:4]), int(start_date[0:2]))
      end_date = date(int(str(20)+str(end_date[4:6])), int(end_date[2:4]), int(end_date[0:2]))
      if str(start_date) <= str(tempdate) <= str(end_date):
        temp = "<td>~~~Booked~~~</td>"
      else:
        temp = "<td>            </td>"

      i += 1
      rowinsert += temp

    bodyinsert += rowinsert + "</tr>"
    

  htmloutput = template.replace("##TITLEROW##",headerinsert)
  htmloutput = htmloutput.replace("##REPEATROWSHERE##",bodyinsert)

  fh = open("Timetable.html","w")
  fh.write(htmloutput)
  fh.close()

  filename = 'file:///'+os.getcwd()+'/' + 'Timetable.html'
  webbrowser.open_new_tab(filename)