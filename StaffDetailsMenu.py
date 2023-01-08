from tkinter import *
from datastructures import *
from FontStyleSheet import *
def openStaffDetailsMenuWindow():
    #creates the Staff Details Menu window
    staffDetailsMenuWin = Toplevel()
    staffDetailsMenuWin.geometry("400x400")
    staffDetailsMenuWin.title("Staff Details Menu")
    
    #creates the function for viewing staff details
    def viewStaffDetails():
        #creates window
        viewStaffDetailsWin = Toplevel()
        viewStaffDetailsWin.geometry("650x400")
        viewStaffDetailsWin.title("View Staff Details")

        #creates label
        staffDetailslbl = Label(viewStaffDetailsWin, font=Heading, text="Staff Details",)
        staffDetailslbl.pack()

        staffDetailsLB = Listbox(viewStaffDetailsWin, width="75", font=SH2)
        staffDetailsLB.pack()

        staffDetailsLB.delete(0,END)
        for staff in listStaff:
            staffDetailsLB.insert(END, staff.staffID + staff.staffFName + staff.staffLName + staff.jobTitle + staff.dateJoined + staff.DOB + staff.tNum + staff.emerContName + staff.emerContNum + staff.staffPostcode + staff.staffAddressLine1 + staff.staffAddressLine2 + staff.staffCity)
    
    viewStaffDetailsbtn = Button(staffDetailsMenuWin, text="View Staff Details", command=viewStaffDetails, font= BTN)
    viewStaffDetailsbtn.pack()

    def addStaffDetails():
        #creates the View Room window
        AddStaffWin = Toplevel()
        AddStaffWin.geometry("400x850")
        AddStaffWin.title("View Rooms")

        #main title
        mainTitle = Label(AddStaffWin, text="Add Staff", font=Heading)
        mainTitle.pack()

        def genreateStaffID():
            prefix = "ST"
            ID = prefix + str(len(listStaff)+1).zfill(3)
            staffIDvar.set(ID)

        staffIDlbl = Label(AddStaffWin, text="Staff ID", font=SH1)
        staffIDlbl.pack()
        staffIDvar = StringVar()
        staffIDentry= Entry(AddStaffWin, textvariable=staffIDvar, font=EB)
        staffIDentry.pack()
        submitbtn = Button(AddStaffWin, text="Generate RoomID", font=BTN, command=genreateStaffID)
        submitbtn.pack()

        staffFNamelbl = Label(AddStaffWin, text="Staff Name", font=SH1)
        staffFNamelbl.pack()
        staffFNameentry = Entry(AddStaffWin, font=EB)
        staffFNameentry.pack()

        staffLNamelbl = Label(AddStaffWin, text="Staff Lastname", font=SH1)
        staffLNamelbl.pack()
        staffLNameentry = Entry(AddStaffWin, font=EB)
        staffLNameentry.pack()

        staffJobTitlelbl = Label(AddStaffWin, text="Staff Members Job Title", font=SH1)
        staffJobTitlelbl.pack()
        staffJobTitleentry = Entry(AddStaffWin, font=EB)
        staffJobTitleentry.pack()

        staffDateJoinedlbl = Label(AddStaffWin, text="Date Joined", font=SH1)
        staffDateJoinedlbl.pack()
        staffDateJoinedentry = Entry(AddStaffWin, font=EB)
        staffDateJoinedentry.pack()

        staffDOBlbl = Label(AddStaffWin, text="Staff Date of Birth", font=SH1)
        staffDOBlbl.pack()
        staffDOBentry = Entry(AddStaffWin, font=EB)
        staffDOBentry.pack()

        staffTNumlbl = Label(AddStaffWin, text="Staff Telephone Number", font=SH1)
        staffTNumlbl.pack()
        staffTNumentry = Entry(AddStaffWin, font=EB)
        staffTNumentry.pack()

        staffEmerContNamelbl = Label(AddStaffWin, text="Staff Emergenecy Contact Name", font=SH1)
        staffEmerContNamelbl.pack()
        staffEmerContNameentry = Entry(AddStaffWin, font=EB)
        staffEmerContNameentry.pack()

        staffEmerContNumlbl = Label(AddStaffWin, text="Staff Emergency Contact Number", font=SH1)
        staffEmerContNumlbl.pack()
        staffEmerContNumentry = Entry(AddStaffWin, font=EB)
        staffEmerContNumentry.pack()

        staffPostcodelbl = Label(AddStaffWin, text="Staff Postcode", font=SH1)
        staffPostcodelbl.pack()
        staffPostcodeentry = Entry(AddStaffWin, font=EB)
        staffPostcodeentry.pack()

        staffAddressLine1lbl = Label(AddStaffWin, text="Staff Address Line 1", font=SH1)
        staffAddressLine1lbl.pack()
        staffAddressLine1entry = Entry(AddStaffWin, font=EB)
        staffAddressLine1entry.pack()

        staffAddressLine2lbl = Label(AddStaffWin, text="Staff Address Line 2", font=SH1)
        staffAddressLine2lbl.pack()
        staffAddressLine2entry = Entry(AddStaffWin, font=EB)
        staffAddressLine2entry.pack()

        staffCitylbl = Label(AddStaffWin, text="Staff City", font=SH1)
        staffCitylbl.pack()
        staffCityentry = Entry(AddStaffWin, font=EB)
        staffCityentry.pack()

        def addStaffFunct():
            global staff
            #validation

            if True == True:
                newStaff = staff()
                newStaff.staffID = staffIDentry.get()
                newStaff.staffFName = staffFNameentry.get()
                newStaff.staffLName = staffLNameentry.get()
                newStaff.jobTitle = staffJobTitleentry.get()
                newStaff.dateJoined = staffDateJoinedentry.get()
                newStaff.DOB = staffDOBentry.get()
                newStaff.tNum = staffTNumentry.get()
                newStaff.emerContName = staffEmerContNameentry.get()
                newStaff.emerContNum = staffEmerContNumentry.get()
                newStaff.staffPostcode = staffPostcodeentry.get()
                newStaff.staffAddressLine1 = staffAddressLine1entry.get()
                newStaff.staffAddressLine2 = staffAddressLine2entry.get()
                newStaff.staffCity = staffCityentry.get()
                AddStaffWin.withdraw()
                listStaff.append(newStaff)
                saveData()

        submitbtn = Button(AddStaffWin, text="Submit", font=BTN, command=addStaffFunct)
        submitbtn.pack()

    addStaffDetailsbtn = Button(staffDetailsMenuWin, text="Add Staff Details", command=addStaffDetails, font= BTN)
    addStaffDetailsbtn.pack()

    def editStaffDetailsWindow():
        #creates the View Staff Details window
        ChooseStaffWin = Toplevel()
        ChooseStaffWin.geometry("650x400")
        ChooseStaffWin.title("Choose a Staff to Edit")

        mainTitle = Label(ChooseStaffWin, text="Choose a Staff Member's Details to Edit", font=Heading)
        mainTitle.pack()

        staffDetailsLB = Listbox(ChooseStaffWin, width=75, font=SH2)
        staffDetailsLB.pack()

        staffDetailsLB.delete(0,END)
        for staff in listStaff:
            staffDetailsLB.insert(END, staff.staffID + staff.staffFName + staff.staffLName + staff.jobTitle + staff.dateJoined + staff.DOB + staff.tNum + staff.emerContName + staff.emerContNum + staff.staffPostcode + staff.staffAddressLine1 + staff.staffAddressLine2 + staff.staffCity)
    
        def editStaff():
            if len(staffDetailsLB.curselection()) > 0:
                index = staffDetailsLB.curselection()[0]

                EditStaffWin = Toplevel()
                EditStaffWin.geometry("400x900")
                EditStaffWin.title("Edit Staff Details")

                mainTitle = Label(EditStaffWin, text="Edit Staff Details", font=Heading)
                mainTitle.pack()

                staffIDlbl = Label(EditStaffWin, text="Staff ID", font=SH1)
                staffIDlbl.pack()
                staffIDvar = StringVar()
                staffIDentry= Entry(EditStaffWin, textvariable=staffIDvar, font=EB)
                staffIDentry.pack()
                staffIDvar.set(listStaff[index].staffID)

                staffFNamelbl = Label(EditStaffWin, text="Staff Name", font=SH1)
                staffFNamelbl.pack()
                staffFNamevar = StringVar()
                staffFNameentry = Entry(EditStaffWin, textvariable=staffFNamevar, font=EB)
                staffFNameentry.pack()
                staffFNamevar.set(listStaff[index].staffFName)

                staffLNamelbl = Label(EditStaffWin, text="Staff Lastname", font=SH1)
                staffLNamelbl.pack()
                staffLNamevar = StringVar()
                staffLNameentry = Entry(EditStaffWin, textvariable=staffLNamevar, font=EB)
                staffLNameentry.pack()
                staffLNamevar.set(listStaff[index].staffLName)

                staffJobTitlelbl = Label(EditStaffWin, text="Staff Members Job Title", font=SH1)
                staffJobTitlelbl.pack()
                staffJobTitlevar = StringVar()
                staffJobTitleentry = Entry(EditStaffWin, textvariable=staffJobTitlevar, font=EB)
                staffJobTitleentry.pack()
                staffJobTitlevar.set(listStaff[index].jobTitle)

                staffDateJoinedlbl = Label(EditStaffWin, text="Date Joined", font=SH1)
                staffDateJoinedlbl.pack()
                staffDateJoinedvar = StringVar()
                staffDateJoinedentry = Entry(EditStaffWin, textvariable=staffDateJoinedvar, font=EB)
                staffDateJoinedentry.pack()
                staffDateJoinedvar.set(listStaff[index].dateJoined)

                staffDOBlbl = Label(EditStaffWin, text="Staff Date of Birth", font=SH1)
                staffDOBlbl.pack()
                staffDOBvar = StringVar()
                staffDOBentry = Entry(EditStaffWin, textvariable=staffDOBvar, font=EB)
                staffDOBentry.pack()
                staffDOBvar.set(listStaff[index].DOB)

                staffTNumlbl = Label(EditStaffWin, text="Staff Telephone Number", font=SH1)
                staffTNumlbl.pack()
                staffTNumvar = StringVar()
                staffTNumentry = Entry(EditStaffWin, textvariable=staffTNumvar, font=EB)
                staffTNumentry.pack()
                staffTNumvar.set(listStaff[index].tNum)

                staffEmerContNamelbl = Label(EditStaffWin, text="Staff Emergenecy Contact Name", font=SH1)
                staffEmerContNamelbl.pack()
                staffEmerContNamevar = StringVar()
                staffEmerContNameentry = Entry(EditStaffWin, textvariable=staffEmerContNamevar, font=EB)
                staffEmerContNameentry.pack()
                staffEmerContNamevar.set(listStaff[index].emerContName)

                staffEmerContNumlbl = Label(EditStaffWin, text="Staff Emergency Contact Number", font=SH1)
                staffEmerContNumlbl.pack()
                staffEmerContNumvar = StringVar()
                staffEmerContNumentry = Entry(EditStaffWin, textvariable=staffEmerContNumvar, font=EB)
                staffEmerContNumentry.pack()
                staffEmerContNumvar.set(listStaff[index].emerContNum)

                staffPostcodelbl = Label(EditStaffWin, text="Staff Postcode", font=SH1)
                staffPostcodelbl.pack()
                staffPostcodevar = StringVar()
                staffPostcodeentry = Entry(EditStaffWin, textvariable=staffPostcodevar, font=EB)
                staffPostcodeentry.pack()
                staffPostcodevar.set(listStaff[index].staffPostcode)

                staffAddressLine1lbl = Label(EditStaffWin, text="Staff Address Line 1", font=SH1)
                staffAddressLine1lbl.pack()
                staffAddressLine1var = StringVar()
                staffAddressLine1entry = Entry(EditStaffWin, textvariable=staffAddressLine1var, font=EB)
                staffAddressLine1entry.pack()
                staffAddressLine1var.set(listStaff[index].staffAddressLine2)

                staffAddressLine2lbl = Label(EditStaffWin, text="Staff Address Line 2", font=SH1)
                staffAddressLine2lbl.pack()
                staffAddressLine2var = StringVar()
                staffAddressLine2entry = Entry(EditStaffWin, textvariable=staffAddressLine2var, font=EB)
                staffAddressLine2entry.pack()
                staffAddressLine2var.set(listStaff[index].staffID)


                staffCitylbl = Label(EditStaffWin, text="Staff City", font=SH1)
                staffCitylbl.pack()
                staffCityvar = StringVar()
                staffCityentry = Entry(EditStaffWin, textvariable=staffCityvar, font=EB)
                staffCityentry.pack()

                staffCityvar.set(listStaff[index].staffCity)

                def addStaffFunct():
                    global staff
                    #validation

                    if True == True:
                        newStaff = staff()
                        listStaff[index].staffID = staffIDentry.get()
                        listStaff[index].staffFName = staffFNameentry.get()
                        listStaff[index].staffLName = staffLNameentry.get()
                        listStaff[index].jobTitle = staffJobTitleentry.get()
                        listStaff[index].dateJoined = staffDateJoinedentry.get()
                        listStaff[index].DOB = staffDOBentry.get()
                        listStaff[index].tNum = staffTNumentry.get()
                        listStaff[index].emerContName = staffEmerContNameentry.get()
                        listStaff[index].emerContNum = staffEmerContNumentry.get()
                        listStaff[index].staffPostcode = staffPostcodeentry.get()
                        listStaff[index].staffAddressLine1 = staffAddressLine1entry.get()
                        listStaff[index].staffAddressLine2 = staffAddressLine2entry.get()
                        listStaff[index].staffCity = staffCityentry.get()
                        saveData()

                        staffDetailsLB.delete(0,END)
                        for staff in listStaff:
                            staffDetailsLB.insert(END, staff.staffID + staff.staffFName + staff.staffLName + staff.jobTitle + staff.dateJoined + staff.DOB + staff.tNum + staff.emerContName + staff.emerContNum + staff.staffPostcode + staff.staffAddressLine1 + staff.staffAddressLine2 + staff.staffCity)
    
                    EditStaffWin.withdraw()


                submitbtn = Button(EditStaffWin, text="Submit", font=BTN, command=addStaffFunct)
                submitbtn.pack()

        editbtn = Button(ChooseStaffWin, text="Edit Record", command=editStaff)
        editbtn.pack()

    editStaffDetailsbtn = Button(staffDetailsMenuWin, text="Edit Staff Details", font=BTN, command=editStaffDetailsWindow)
    editStaffDetailsbtn.pack()


