from pickle import *
from tkinter import *
from tkinter import messagebox
from datastructures import *
from FontStyleSheet import *


def test():
    #creates the View Room window
    selectRoom = Toplevel()
    selectRoom.geometry("450x400")
    selectRoom.title("View and Edit Rooms")

    # main title
    mainTitle = Label(selectRoom, text="View Rooms", font=Heading)
    mainTitle.pack()

    listRoomLB = Listbox(selectRoom, font=SH2, width=40)
    listRoomLB.pack()

    RoomList = []

    def update(RoomList):
        for room in listRoom:
            appendage = []
            appendage.append(room.roomID)
            appendage.append(room.roomName)
            appendage.append(room.guestLimit)
            if room.familyRoom == True:
                familyvar = 1
            else:
                familyvar = 0
            appendage.append(familyvar)
            RoomList.append(appendage)

        try:
            display(RoomList)
        except:
            pass
        
    update(RoomList)

    sortList = RoomList

    def display(RoomList):
        listRoomLB.delete(0,END)
        for room in RoomList:
            if room[3] == 1:
                familyvar = "family"
            else:
                familyvar = "normal"
            listRoomLB.insert(END, room[0] +" ~ "+ room[1] +" ~ "+ room[2] +" ~ "+ familyvar)
    
    display(RoomList)

    def idSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j]>sortList[j+1]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display() 
    
    def roomNameSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j][1] > sortList[j+1][1]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()

    def guetsLimitSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j][2] > sortList[j+1][2]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()

    def familyRoomSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j][3] < sortList[j+1][3]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()
    

    idSortBtn = Button(selectRoom, text="Sort by ID", command=idSort)
    idSortBtn.pack()

    roomNameSortbtn = Button(selectRoom, text="Sort by Room Name", command=roomNameSort)
    roomNameSortbtn.pack()

    guetsLimitSortbtn = Button(selectRoom, text="Sort by Guest Limit", command=guetsLimitSort)
    guetsLimitSortbtn.pack()

    familyRoomSortbtn = Button(selectRoom, text="Sort by Family Room", command=familyRoomSort)
    familyRoomSortbtn.pack()
    

    def editRoom():
        if len(listRoomLB.curselection()) > 0:
            index = listRoomLB.curselection()[0]

            viewRoomWin = Toplevel()
            viewRoomWin.geometry("400x400")
            viewRoomWin.title("Add Room")

            #Room Name
            rmlbl = Label(viewRoomWin, text= "Room Name", font=SH1)
            rmlbl.pack()
            roomNameentryvar = StringVar()
            rment = Entry(viewRoomWin, textvariable=roomNameentryvar, font=EB, state='readonly')
            rment.pack()
            roomNameentryvar.set(listRoom[index].roomName)
    
            #Guest Limit
            gllbl = Label(viewRoomWin, text= "Guest Limit", font=SH1)
            gllbl.pack()
            guestLimitentryvar = StringVar()
            glent = Entry(viewRoomWin, textvariable=guestLimitentryvar, font=EB, state='readonly')
            glent.pack()
            guestLimitentryvar.set(listRoom[index].guestLimit)
            
            #Family Room
            frvar = IntVar()
            frent = Checkbutton(viewRoomWin, text="Is this a family room?", variable=frvar, state='disabled')
            frent.pack()

            if listRoom[index].familyRoom == 1:
                frent.select()
            
            def submitfunct():
                check = "12"
                if rment.get() == "":
                    check = check.replace("1","a")

                if glent.get() == "":
                    check = check.replace("2","a")

                if check != "12":
                    if check[0] == "a":
                        messagebox.showerror("Wait!", "The Room Name is empty!")

                    if check[1] == "a":
                        messagebox.showerror("Wait!", "The Guest Limit is empty!")
                    elif check[1] == "b":
                        messagebox.showerror("Wait!", "The Guest Limit is not a number!")
                else:
                    listRoom[index].roomName = rment.get()
                    listRoom[index].guestLimit = glent.get()
                    listRoom[index].familyRoom = frvar.get()

                    RoomList = []
                    saveData()
                    update(RoomList)
                    viewRoomWin.withdraw()

            def editMode():
                def deleteMode():
                    confirmation = messagebox.askquestion("Wait!", "Are you sure you want to delete the record?", icon="warning")
                    if confirmation == "yes":
                        roomNameentryvar = "#Deleted#"
                        guestLimitentryvar = "#Deleted#"

                        listRoom[index].roomName = roomNameentryvar
                        listRoom[index].guestLimit = guestLimitentryvar

                        RoomList = []
                        saveData()
                        update(RoomList)
                        viewRoomWin.withdraw()

                rment.configure(state='normal')
                glent.configure(state='normal')
                frent.configure(state='normal')

                viewRoomWin.title("Edit Room Details")
                exitbtn.configure(text="Close")
                exitbtn.forget()
                togglebtn.configure(text="Read Mode", command = readMode)
                deletebtn.configure(command = deleteMode)
                submitbtn.pack()
                deletebtn.pack()
                exitbtn.pack()

            def readMode():
                rment.configure(state='readonly')
                glent.configure(state='readonly')
                frent.configure(state='disabled')

                viewRoomWin.title("View Room Details")
                togglebtn.configure(text="Edit Mode", command = editMode)
                exitbtn.configure(text="Close")
                deletebtn.forget()
                submitbtn.forget()

            togglebtn = Button(viewRoomWin, text="Edit Mode", command = editMode)
            togglebtn.pack()

            submitbtn = Button(viewRoomWin, text="submit changes", command = submitfunct)

            deletebtn = Button(viewRoomWin, text="Delete Record")
            
            exitbtn = Button(viewRoomWin,text="Close", command = lambda: viewRoomWin.withdraw())
            exitbtn.pack()
    

    editbtn = Button(selectRoom, text="View and Edit Room", command=editRoom)
    editbtn.pack()
