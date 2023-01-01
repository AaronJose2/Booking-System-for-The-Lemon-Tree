from tkinter import *
from pickle import *
from datastructures import *
from FontStyleSheet import *

def openRoomMenuWindow():
    #creates the Room Menu window
    RoomMenuWin = Toplevel()
    RoomMenuWin.geometry("400x400")
    RoomMenuWin.title("Room Menu")
    
    # main title
    mainTitle = Label(RoomMenuWin, text="Room Menu", font=Heading)
    mainTitle.pack()

    viewRoombtn = Button(RoomMenuWin, text="View Rooms", font=BTN, command=openViewRoomsWindow)
    viewRoombtn.pack()
    
    AddRoombtn = Button(RoomMenuWin, text="Add a Room", font=BTN, command=openAddRoomWindow)
    AddRoombtn.pack()

    EditRoombtn = Button(RoomMenuWin, text="Edit Rooms", font=BTN, command=openEditRoomsWindow)
    EditRoombtn.pack()

def openViewRoomsWindow():
    #creates the View Room window
    ViewRoomWin = Toplevel()
    ViewRoomWin.geometry("400x400")
    ViewRoomWin.title("View Rooms")

    # main title
    mainTitle = Label(ViewRoomWin, text="View Rooms", font=Heading)
    mainTitle.pack()

    listRoomLB = Listbox(ViewRoomWin, font=SH2)
    listRoomLB.pack()

    listRoomLB.delete(0,END)
    for room in listRoom:
        listRoomLB.insert(END, room.roomName + room.guestLimit + str(room.familyRoom))

def openAddRoomWindow():
    #global roomNameentry, guestLimitentry, familyRoomentry
    #creates the View Room window
    AddRoomWin = Toplevel()
    AddRoomWin.geometry("400x400")
    AddRoomWin.title("Add Room")

    # main title
    mainTitle = Label(AddRoomWin, text="Add Room", font=Heading)
    mainTitle.pack()

    #labels and respseective entries.
    def genreateRoomID():
        prefix = "RM"
        ID = prefix + str(len(listRoom)+1).zfill(3)
        roomIDvar.set(ID)

    roomIDvar = StringVar()
    roomIDent= Entry(AddRoomWin, textvariable=roomIDvar, font=EB)
    roomIDent.pack()
    submitbtn = Button(AddRoomWin, text="Generate RoomID", font=BTN, command=genreateRoomID)
    submitbtn.pack()



    roomNamelbl = Label(AddRoomWin, text="Room Name", font=SH1)
    roomNamelbl.pack()
    roomNameentry = Entry(AddRoomWin, font=EB)
    roomNameentry.pack()

    guestLimitlbl = Label(AddRoomWin, text="Set the Guest Limit", font=SH1)
    guestLimitlbl.pack()
    guestLimitentry = Entry(AddRoomWin, font=EB)
    guestLimitentry.pack()

    familyRoomVar = IntVar()
    familyRoombtn = Checkbutton(AddRoomWin, text="Is this a family room?", variable=familyRoomVar)
    familyRoombtn.pack()


    def addRoomFunct():
        #validation

        if True == True:
            newRoom = room()
            newRoom.roomName = roomNameentry.get()
            newRoom.guestLimit = guestLimitentry.get()
            if familyRoomVar.get() == 1:
                newRoom.familyRoom = True
            else:
                newRoom.familyRoom = False
        
        listRoom.append(newRoom)
        saveData()
        print(listRoom)
    submitbtn = Button(AddRoomWin, text="Submit", font=BTN, command=addRoomFunct)
    submitbtn.pack()

def openEditRoomsWindow():
    global listRoomLB
    #creates the View Room window
    EditRoomWin = Toplevel()
    EditRoomWin.geometry("400x600")
    EditRoomWin.title("Edit Rooms")

    # main title
    mainTitle = Label(EditRoomWin, text="Edit Rooms", font=Heading)
    mainTitle.pack()

    listRoomLB = Listbox(EditRoomWin, font=SH2)
    listRoomLB.pack()

    listRoomLB.delete(0,END)
    for room in listRoom:
        listRoomLB.insert(END, room.roomName + room.guestLimit + str(room.familyRoom))
       
    def editRoom():
        global listRoomLB
        if len(listRoomLB.curselection()) > 0:
            index = listRoomLB.curselection()[0]

            #Room Name
            rmlbl = Label(EditRoomWin, text= "Room Name", font=SH1)
            rmlbl.pack()
            roomNameentryvar = StringVar()
            rment = Entry(EditRoomWin, textvariable=roomNameentryvar, font=EB)
            rment.pack()
            roomNameentryvar.set(listRoom[index].roomName)
            
    
            #Guest Limit
            gllbl = Label(EditRoomWin, text= "Guest Limit", font=SH1)
            gllbl.pack()
            guestLimitentryvar = StringVar()
            glent = Entry(EditRoomWin, textvariable=guestLimitentryvar, font=EB)
            glent.pack()
            guestLimitentryvar.set(listRoom[index].guestLimit)
            
            #Family Room
            frlbl = Label(EditRoomWin, text= "Family Room", font=SH1)
            frlbl.pack()
            familyRoomentryvar = StringVar()
            frent = Entry(EditRoomWin, textvariable=familyRoomentryvar, font=EB)
            frent.pack()

            if listRoom[index].familyRoom == 1:
                familyRoomentryvar.set("True")
            else:
                familyRoomentryvar.set("False")
            
            def submitfunct():
                global listRoomLB
                index = listRoomLB.curselection()[0]
                #validation
                
                if True == True:
                    listRoom[index].roomName = roomNameentryvar.get()
                    listRoom[index].guestLimit = guestLimitentryvar.get()
                    listRoom[index].familyRoom = familyRoomentryvar.get()

                listRoomLB.delete(0,END)
                for room in listRoom:
                    listRoomLB.insert(END, room.roomName + room.guestLimit + str(room.familyRoom))
         
                rmlbl.pack_forget()
                rment.pack_forget()
                gllbl.pack_forget()
                glent.pack_forget()
                frlbl.pack_forget()
                frent.pack_forget()
                submitbtn.pack_forget()
                saveData()


            submitbtn = Button(EditRoomWin,text="submit changes", command = submitfunct)
            submitbtn.pack()

    editbtn = Button(EditRoomWin, text="Edit Record", command=editRoom)
    editbtn.pack()

    

