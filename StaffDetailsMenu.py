from tkinter import *
from tkinter import messagebox
from datastructures import *
from FontStyleSheet import *
from test import *
from datetime import datetime
import re

def openStaffDetailsMenuWindow():
    #creates the Staff Details Menu window
    staffDetailsMenuWin = Toplevel()
    staffDetailsMenuWin.geometry("400x400")
    staffDetailsMenuWin.title("Staff Details Menu")

    addStaffDetailsbtn = Button(staffDetailsMenuWin, text="Add Staff Details", command=addStaffDetails, font= BTN)
    addStaffDetailsbtn.pack()

    editStaffDetailsbtn = Button(staffDetailsMenuWin, text="View and Edit Staff Details", font=BTN, command=edtiStaffDetails)
    editStaffDetailsbtn.pack()

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

def addStaffDetails():
    #creates the View Staff window
    AddStaffWin = Toplevel()
    AddStaffWin.geometry("400x875")
    AddStaffWin.title("Add Staff")

    #main title
    mainTitle = Label(AddStaffWin, text="Add Staff", font=Heading)
    mainTitle.pack()

    staffIDlbl = Label(AddStaffWin, text="Staff ID", font=SH1)
    staffIDlbl.pack()
    staffIDvar = StringVar()
    staffIDentry= Entry(AddStaffWin, textvariable=staffIDvar, font=EB, state='readonly')
    staffIDentry.pack()
    ID = "ST" +  str(len(listStaff)+1)
    def pad(ID):
        if len(ID) < 5:
            ID = ID[:2] + "0" + ID[2:]
            return pad(ID)
        else:
            return ID
    ID = pad(ID)
    staffIDvar.set(ID)

    staffFNamelbl = Label(AddStaffWin, text="Staff Name", font=SH1)
    staffFNamelbl.pack()
    staffFNameentry = Entry(AddStaffWin, font=EB)
    staffFNameentry.pack()

    staffLNamelbl = Label(AddStaffWin, text="Staff Lastname", font=SH1)
    staffLNamelbl.pack()
    staffLNameentry = Entry(AddStaffWin, font=EB)
    staffLNameentry.pack()

    staffPasswordlbl = Label(AddStaffWin, text="Staff Password", font=SH1)
    staffPasswordlbl.pack()
    staffPasswordentry = Entry(AddStaffWin, font=EB)
    staffPasswordentry.pack()

    staffJobTitlelbl = Label(AddStaffWin, text="Staff Members Job Title", font=SH1)
    staffJobTitlelbl.pack()
    staffJobTitleentry = Entry(AddStaffWin, font=EB)
    staffJobTitleentry.pack()

    staffDateJoinedlbl = Label(AddStaffWin, text="Date Joined", font=SH1)
    staffDateJoinedlbl.pack()
    staffDateJoinedvar = StringVar()
    staffDateJoinedentry = Entry(AddStaffWin, textvariable=staffDateJoinedvar, font=EB)
    staffDateJoinedentry.pack()
    staffDateJoinedvar.set(str(datetime.today())[8:10] +"/"+str(datetime.today())[5:7] +"/"+ str(datetime.today())[:4])

    staffDOBlbl = Label(AddStaffWin, text="Staff Date of Birth", font=SH1)
    staffDOBlbl.pack()
    staffDOBentry = Entry(AddStaffWin, font=EB)
    staffDOBentry.pack()

    staffTNumlbl = Label(AddStaffWin, text="Staff Telephone Number", font=SH1)
    staffTNumlbl.pack()
    staffTNumentry = Entry(AddStaffWin, font=EB)
    staffTNumentry.pack()

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

    staffEmerContNamelbl = Label(AddStaffWin, text="Staff Emergenecy Contact Name", font=SH1)
    staffEmerContNamelbl.pack()
    staffEmerContNameentry = Entry(AddStaffWin, font=EB)
    staffEmerContNameentry.pack()

    staffEmerContNumlbl = Label(AddStaffWin, text="Staff Emergency Contact Number", font=SH1)
    staffEmerContNumlbl.pack()
    staffEmerContNumentry = Entry(AddStaffWin, font=EB)
    staffEmerContNumentry.pack()

    def addStaffFunct():
        check = "1 2 3 4 5 6 7 8 9 10 11 12"

        if staffFNameentry.get() == "":
            check = check.replace("1","a")

        if staffLNameentry.get() == "":
            check = check.replace("2","a")

        if staffJobTitleentry.get() == "":
            check = check.replace("3","a")

        if staffDateJoinedentry.get() == "":
            check = check.replace("4", "a")
        try:
            if len(staffDateJoinedentry.get()) == 8:
                staffDateJoined = str(staffDateJoinedentry.get()[:6]) + "20" + str(staffDateJoinedentry.get()[6:])
            else:
                staffDateJoined = staffDateJoinedentry.get()
            staffDateJoined = datetime.strptime(staffDateJoined, '%d/%m/%Y')
        except ValueError:
            check = check.replace("4", "b")

        if staffDOBentry.get() == "":
            check = check.replace("5", "a")
        try:
            if len(staffDOBentry.get()) == 8:
                staffDob = str(staffDOBentry.get()[:6]) + "20" + str(staffDOBentry.get()[6:])
            else:
                staffDob = staffDOBentry.get()
            staffDob = datetime.strptime(staffDob, '%d/%m/%Y')
        except ValueError:
            check = check.replace("5", "b")
        
        tNum = staffTNumentry.get().replace(" ", "")

        if tNum == "":
            check = check.replace("6","a")
        elif tNum.isnumeric() != True:
            check = check.replace("6","b")
        elif len(tNum) != 11:
            check = check.replace("6","c")

        if staffEmerContNameentry.get() == "":
            check = check.replace("7","a")

        if staffEmerContNumentry.get() == "":
            check = check.replace("8","a")
        elif staffEmerContNumentry.get().isnumeric() != True:
            check = check.replace("8","b")
        elif len(staffEmerContNumentry.get()) != 11:
            check = check.replace("8","c")

        if bool(re.match(r'^[A-Z]{1,2}[0-9R][0-9A-Z][0-9][A-Z]{2}$', str(staffPostcodeentry.get()))) != True:
            check = check.replace("9","a")

        if staffAddressLine1entry.get() == "":
            check = check.replace("10","a")

            check = check.replace("11","a")

        if staffCityentry.get() == "":
            check = check.replace("12","a")
        
        if check != "1 2 3 4 5 6 7 8 9 10 11 12":
            if check[0] == "a":
                messagebox.showerror("Wait!", "The Staff Forename field is empty!")

            if check[2] == "a":
                messagebox.showerror("Wait!", "The Staff Surname field is empty!")

            if check[4] == "a":
                messagebox.showerror("Wait!", "The Job Title field is empty")

            if check[6] == "a":
                messagebox.showerror("Wait!", "The Date Joined field is empty!")
            elif check[6] == "b":
                messagebox.showerror("Wait!", "The Date Joined is not correctly formatted!")

            if check[8] == "a":
                messagebox.showerror("Wait!", "The Date of Birth field is empty!")
            elif check[8] == "b":
                messagebox.showerror("Wait!", "The Date of Birth field is not correctly formatted!")

            if check[10] == "a":
                messagebox.showerror("Wait!", "The Staff's Telephone Number field is empty!")
            elif check[10] == "b":
                messagebox.showerror("Wait!", "The Staff Telephone Number should only contain numbers!")
            elif check[6] == "c":
                messagebox.showerror("Wait!", "The Staff Telephone Number is not the correct length!")

            if check[12] == "a":
                messagebox.showerror("Wait!", "The Emergency Contact Name field is empty!")

            if check[14] == "a":
                messagebox.showerror("Wait!", "The Emergency Contact Telephone Number field is empty!")
            elif check[14] == "b":
                messagebox.showerror("Wait!", "The Emergency Contact Telephone Number should only contain numbers!")
            elif check[6] == "c":
                messagebox.showerror("Wait!", "The Emergency Contact Telephone Number is not the correct length!")

            if check[16] == "a":
                messagebox.showerror("Wait!", "There is something wrong with the Postcode field.!")

            if check[18:20] == "a":
                messagebox.showerror("Wait!", "The Adddress Line 1 field is empty!")

            if check[21:23] == "a":
                messagebox.showerror("Wait!", "The Address Line 2 field is empty!")

            if check[24:26] == "a":
                messagebox.showerror("Wait!", "The City field is empty!")

        else:
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
            newStaff.staffPassword = staffPasswordentry.get()
            AddStaffWin.withdraw()
            listStaff.append(newStaff)
            saveData()

    submitbtn = Button(AddStaffWin, text="Submit", font=BTN, command=addStaffFunct)
    submitbtn.pack()


def edtiStaffDetails():
    #creates the View Staff Details window
    ChooseStaffWin = Toplevel()
    ChooseStaffWin.geometry("450x400")
    ChooseStaffWin.title("Choose a Staff to View and Edit")

    mainTitle = Label(ChooseStaffWin, text="Choose a Staff to View and Edit", font=Heading)
    mainTitle.pack()

    staffDetailsLB = Listbox(ChooseStaffWin, width=45, font=SH2)
    staffDetailsLB.pack()

    StaffList = []
    
    for staff in listStaff:
        appendage = []
        appendage.append(staff.staffID)
        appendage.append(staff.staffFName)
        appendage.append(staff.staffLName)
        appendage.append(staff.jobTitle)
        appendage.append(staff.dateJoined)
        appendage.append(staff.DOB)
        appendage.append(staff.tNum)
        appendage.append(staff.emerContName)
        appendage.append(staff.emerContNum)
        appendage.append(staff.staffPostcode)
        appendage.append(staff.staffAddressLine1)
        appendage.append(staff.staffAddressLine2)
        appendage.append(staff.staffCity)
        appendage.append(staff.staffPassword)
        StaffList.append(appendage)
        
    sortList = StaffList

    def display():
        staffDetailsLB.delete(0,END)
        for staff in StaffList:
            staffDetailsLB.insert(END, staff[0] +" | "+ staff[1] +" "+ staff[2] +" | "+ staff[3])

    display()

    def idSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j]>sortList[j+1]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()          
        
    def firstNameSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j][1] > sortList[j+1][1]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()

    def lastNameSort():
        for i in range(0, len(sortList)-1):  
            for j in range(len(sortList)-1):
                if (sortList[j][2] > sortList[j+1][2]):  
                    temp = sortList[j]
                    sortList[j] = sortList[j+1]  
                    sortList[j+1] = temp
        display()


    idSortBtn = Button(ChooseStaffWin, text="Sort by ID", command=idSort)
    idSortBtn.pack()

    firstNameSortBtn = Button(ChooseStaffWin, text="Sort by First Name", command=firstNameSort)
    firstNameSortBtn.pack()

    lastNameSortBtn = Button(ChooseStaffWin, text="Sort by Last Name", command=lastNameSort)
    lastNameSortBtn.pack()

    def editStaff():
        ChooseStaffWin.withdraw()
        if len(staffDetailsLB.curselection()) > 0:
            index = staffDetailsLB.curselection()[0]

            ViewStaffWin = Toplevel()
            ViewStaffWin.geometry("400x970")
            ViewStaffWin.title("Edit Staff Details")

            mainTitle = Label(ViewStaffWin, text="Edit Staff Details", font=Heading)
            mainTitle.pack()

            staffIDlbl = Label(ViewStaffWin, text="Staff ID", font=SH1)
            staffIDlbl.pack()
            staffIDvar = StringVar()
            staffIDentry= Entry(ViewStaffWin, textvariable=staffIDvar, font=EB, state='readonly')
            staffIDentry.pack()
            staffIDvar.set(listStaff[index].staffID)

            staffFNamelbl = Label(ViewStaffWin, text="Staff Name", font=SH1)
            staffFNamelbl.pack()
            staffFNamevar = StringVar()
            staffFNameentry = Entry(ViewStaffWin, textvariable=staffFNamevar, font=EB, state='readonly')
            staffFNameentry.pack()
            staffFNamevar.set(listStaff[index].staffFName)

            staffLNamelbl = Label(ViewStaffWin, text="Lastname", font=SH1)
            staffLNamelbl.pack()
            staffLNamevar = StringVar()
            staffLNameentry = Entry(ViewStaffWin, textvariable=staffLNamevar, font=EB, state='readonly')
            staffLNameentry.pack()
            staffLNamevar.set(listStaff[index].staffLName)

            staffPasswordlbl = Label(ViewStaffWin, text="Password", font=SH1)
            staffPasswordlbl.pack()
            staffPasswordvar = StringVar()
            staffPasswordvar = ""
            staffPasswordentry = Entry(ViewStaffWin, textvariable=staffPasswordvar, font=EB, state='readonly')
            staffPasswordentry.pack()

            staffJobTitlelbl = Label(ViewStaffWin, text="Job Title", font=SH1)
            staffJobTitlelbl.pack()
            staffJobTitlevar = StringVar()
            staffJobTitleentry = Entry(ViewStaffWin, textvariable=staffJobTitlevar, font=EB, state='readonly')
            staffJobTitleentry.pack()
            staffJobTitlevar.set(listStaff[index].jobTitle)

            staffDateJoinedlbl = Label(ViewStaffWin, text="Date Joined", font=SH1)
            staffDateJoinedlbl.pack()
            staffDateJoinedvar = StringVar()
            staffDateJoinedentry = Entry(ViewStaffWin, textvariable=staffDateJoinedvar, font=EB, state='readonly')
            staffDateJoinedentry.pack()
            staffDateJoinedvar.set(listStaff[index].dateJoined)

            staffDOBlbl = Label(ViewStaffWin, text="Date of Birth", font=SH1)
            staffDOBlbl.pack()
            staffDOBvar = StringVar()
            staffDOBentry = Entry(ViewStaffWin, textvariable=staffDOBvar, font=EB, state='readonly')
            staffDOBentry.pack()
            staffDOBvar.set(listStaff[index].DOB)

            staffTNumlbl = Label(ViewStaffWin, text="Telephone Number", font=SH1)
            staffTNumlbl.pack()
            staffTNumvar = StringVar()
            staffTNumentry = Entry(ViewStaffWin, textvariable=staffTNumvar, font=EB, state='readonly')
            staffTNumentry.pack()
            staffTNumvar.set(listStaff[index].tNum)

            staffPostcodelbl = Label(ViewStaffWin, text="Postcode", font=SH1)
            staffPostcodelbl.pack()
            staffPostcodevar = StringVar()
            staffPostcodeentry = Entry(ViewStaffWin, textvariable=staffPostcodevar, font=EB, state='readonly')
            staffPostcodeentry.pack()
            staffPostcodevar.set(listStaff[index].staffPostcode)

            staffAddressLine1lbl = Label(ViewStaffWin, text="Address Line 1", font=SH1)
            staffAddressLine1lbl.pack()
            staffAddressLine1var = StringVar()
            staffAddressLine1entry = Entry(ViewStaffWin, textvariable=staffAddressLine1var, font=EB, state='readonly')
            staffAddressLine1entry.pack()
            staffAddressLine1var.set(listStaff[index].staffAddressLine1)

            staffAddressLine2lbl = Label(ViewStaffWin, text="Address Line 2", font=SH1)
            staffAddressLine2lbl.pack()
            staffAddressLine2var = StringVar()
            staffAddressLine2entry = Entry(ViewStaffWin, textvariable=staffAddressLine2var, font=EB, state='readonly')
            staffAddressLine2entry.pack()
            staffAddressLine2var.set(listStaff[index].staffAddressLine2)

            staffCitylbl = Label(ViewStaffWin, text="City", font=SH1)
            staffCitylbl.pack()
            staffCityvar = StringVar()
            staffCityentry = Entry(ViewStaffWin, textvariable=staffCityvar, font=EB, state='readonly')
            staffCityentry.pack()
            staffCityvar.set(listStaff[index].staffCity)

            staffEmerContNamelbl = Label(ViewStaffWin, text="Emergenecy Contact Name", font=SH1)
            staffEmerContNamelbl.pack()
            staffEmerContNamevar = StringVar()
            staffEmerContNameentry = Entry(ViewStaffWin, textvariable=staffEmerContNamevar, font=EB, state='readonly')
            staffEmerContNameentry.pack()
            staffEmerContNamevar.set(listStaff[index].emerContName)

            staffEmerContNumlbl = Label(ViewStaffWin, text="Emergency Contact Number", font=SH1)
            staffEmerContNumlbl.pack()
            staffEmerContNumvar = StringVar()
            staffEmerContNumentry = Entry(ViewStaffWin, textvariable=staffEmerContNumvar, font=EB, state='readonly')
            staffEmerContNumentry.pack()
            staffEmerContNumvar.set(listStaff[index].emerContNum)

            def submitfunct():
                global staff
            
                check = "1 2 3 4 5 6 7 8 9 10 11 12"

                if staffFNameentry.get() == "":
                    check = check.replace("1","a")

                if staffLNameentry.get() == "":
                    check = check.replace("2","a")

                if staffJobTitleentry.get() == "":
                    check = check.replace("3","a")

                if staffDateJoinedentry.get() == "":
                    check = check.replace("4", "a")
                try:
                    if len(staffDateJoinedentry.get()) == 8:
                        staffDateJoined = str(staffDateJoinedentry.get()[:6]) + "20" + str(staffDateJoinedentry.get()[6:])
                    else:
                        staffDateJoined = staffDateJoinedentry.get()
                    staffDateJoined = datetime.strptime(staffDateJoined, '%d/%m/%Y')
                except ValueError:
                    check = check.replace("4", "b")

                if staffDOBentry.get() == "":
                    check = check.replace("5", "a")
                try:
                    if len(staffDOBentry.get()) == 8:
                        staffDob = str(staffDOBentry.get()[:6]) + "20" + str(staffDOBentry.get()[6:])
                    else:
                        staffDob = staffDOBentry.get()
                    staffDob = datetime.strptime(staffDob, '%d/%m/%Y')
                except ValueError:
                    check = check.replace("5", "b")
                
                tNum = staffTNumentry.get().replace(" ", "")

                if tNum == "":
                    check = check.replace("6","a")
                elif tNum.isnumeric() != True:
                    check = check.replace("6","b")
                elif len(tNum) != 11:
                    check = check.replace("6","c")

                if staffEmerContNameentry.get() == "":
                    check = check.replace("7","a")

                if staffEmerContNumentry.get() == "":
                    check = check.replace("8","a")
                elif staffEmerContNumentry.get().isnumeric() != True:
                    check = check.replace("8","b")
                elif len(staffEmerContNumentry.get()) != 11:
                    check = check.replace("8","c")

                if bool(re.match(r'^[A-Z]{1,2}[0-9R][0-9A-Z][0-9][A-Z]{2}$', str(staffPostcodeentry.get()))) != True:
                    check = check.replace("9","a")

                if staffAddressLine1entry.get() == "":
                    check = check.replace("10","aa")

                    check = check.replace("11","aa")

                if staffCityentry.get() == "":
                    check = check.replace("12","aa")
                
                if staffJobTitleentry.get() != "Front Desk Staff":
                    confirmation = messagebox.askquestion("Wait!", "Are you sure you want to delete that?", icon="warning")
                    if confirmation == "no":
                        check = ""

                if staffJobTitleentry.get() != "Front Desk Staff":
                    messagebox.showerror("Wait!", "The Job Title field is empty")

                print(check)
                if check != "1 2 3 4 5 6 7 8 9 10 11 12":
                    if check[0] == "a":
                        messagebox.showerror("Wait!", "The Staff Forename field is empty!")

                    if check[2] == "a":
                        messagebox.showerror("Wait!", "The Staff Surname field is empty!")

                    if check[4] == "a":
                        messagebox.showerror("Wait!", "The Job Title field is empty")

                    if check[6] == "a":
                        messagebox.showerror("Wait!", "The Date Joined field is empty!")
                    elif check[6] == "b":
                        messagebox.showerror("Wait!", "The Date Joined is not correctly formatted!")

                    if check[8] == "a":
                        messagebox.showerror("Wait!", "The Date of Birth field is empty!")
                    elif check[8] == "b":
                        messagebox.showerror("Wait!", "The Date of Birth field is not correctly formatted!")

                    if check[10] == "a":
                        messagebox.showerror("Wait!", "The Staff's Telephone Number field is empty!")
                    elif check[10] == "b":
                        messagebox.showerror("Wait!", "The Staff Telephone Number should only contain numbers!")
                    elif check[6] == "c":
                        messagebox.showerror("Wait!", "The Staff Telephone Number is not the correct length!")

                    if check[12] == "a":
                        messagebox.showerror("Wait!", "The Emergency Contact Name field is empty!")

                    if check[14] == "a":
                        messagebox.showerror("Wait!", "The Emergency Contact Telephone Number field is empty!")
                    elif check[14] == "b":
                        messagebox.showerror("Wait!", "The Emergency Contact Telephone Number should only contain numbers!")
                    elif check[6] == "c":
                        messagebox.showerror("Wait!", "The Emergency Contact Telephone Number is not the correct length!")

                    if check[16] == "a":
                        messagebox.showerror("Wait!", "There is something wrong with the Postcode field.!")

                    if check[18:20] == "a":
                        messagebox.showerror("Wait!", "The Adddress Line 1 field is empty!")

                    if check[21:23] == "a":
                        messagebox.showerror("Wait!", "The Address Line 2 field is empty!")

                    if check[24:26] == "a":
                        messagebox.showerror("Wait!", "The City field is empty!")
        
                else:
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
                    if staffPasswordvar != "":
                        listStaff[index].staffPassword = staffPasswordvar
                    saveData()

                    ViewStaffWin.withdraw()

            def editMode():
                def deleteMode():
                    confirmation = messagebox.askquestion("Wait!", "Are you sure you want to delete that?", icon="warning")
                    if confirmation == "yes":
                        staffFNamevar = "#Deleted#"
                        staffLNamevar = "#Deleted#"
                        staffPasswordvar = "#Deleted#"
                        jobTitlevar = "#Deleted#"
                        dateJoinedvar = "#Deleted#"
                        DOBvar = "#Deleted#"
                        tNumvar = "#Deleted#"
                        emerContNamevar = "#Deleted#"
                        emerContNumvar = "#Deleted#"
                        staffPostcodevar = "#Deleted#"
                        staffAddressLine1var = "#Deleted#"
                        staffAddressLine2var = "#Deleted#"
                        staffCityvar = "#Deleted#"

                        listStaff[index].staffID = staffIDvar
                        listStaff[index].staffFname = staffFNamevar
                        listStaff[index].staffLName = staffLNamevar
                        listStaff[index].jobTitle = jobTitlevar
                        listStaff[index].dateJoined = dateJoinedvar
                        listStaff[index].DOB = DOBvar
                        listStaff[index].tNum = tNumvar
                        listStaff[index].emerContName = tNumvar
                        listStaff[index].emerContNum = emerContNamevar
                        listStaff[index].staffPostcode = emerContNumvar
                        listStaff[index].staffAddressLine1 = staffAddressLine1var
                        listStaff[index].staffAddressLine2 = staffAddressLine2var
                        listStaff[index].staffCity = staffCityvar
                        if staffPasswordvar != "":
                            listStaff[index].staffPassword = staffPasswordvar

                        saveData()
                        ViewStaffWin.withdraw()

                staffFNameentry.configure(state='normal')
                staffLNameentry.configure(state='normal')
                staffPasswordentry.configure(state='normal')
                staffJobTitleentry.configure(state='normal')
                staffDateJoinedentry.configure(state='normal')
                staffDOBentry.configure(state='normal')
                staffTNumentry.configure(state='normal')
                staffEmerContNameentry.configure(state='normal')
                staffEmerContNumentry.configure(state='normal')
                staffPostcodeentry.configure(state='normal')
                staffAddressLine1entry.configure(state='normal')
                staffAddressLine2entry.configure(state='normal')
                staffCityentry.configure(state='normal')
                

                ViewStaffWin.title("Edit Staff Details")
                exitbtn.configure(text="Close Without Saving")
             
                togglebtn.configure(text="Read Mode", command = readMode)
                deletebtn.configure(command = deleteMode)

                exitbtn.forget()
                deletebtn.pack()
                submitbtn.pack()
                exitbtn.pack()

            def readMode():
                staffFNameentry.configure(state='readonly')
                staffLNameentry.configure(state='readonly')
                staffPasswordentry.configure(state='readonly')
                staffJobTitleentry.configure(state='readonly')
                staffDateJoinedentry.configure(state='readonly')
                staffDOBentry.configure(state='readonly')
                staffTNumentry.configure(state='readonly')
                staffEmerContNameentry.configure(state='readonly')
                staffEmerContNumentry.configure(state='readonly')
                staffPostcodeentry.configure(state='readonly')
                staffAddressLine1entry.configure(state='readonly')
                staffAddressLine2entry.configure(state='readonly')
                staffCityentry.configure(state='readonly')
            
                ViewStaffWin.title("View Staff Details")
                togglebtn.configure(text="Edit Mode", command = editMode)
                exitbtn.configure(text="Close")
                deletebtn.forget()
                submitbtn.forget()

            togglebtn = Button(ViewStaffWin, text="Edit Mode", command = editMode)
            togglebtn.pack()

            submitbtn = Button(ViewStaffWin,text="Save Staff Record", command = submitfunct)

            deletebtn = Button(ViewStaffWin, text="Delete Record")
            
            exitbtn = Button(ViewStaffWin,text="Close", command = lambda: ViewStaffWin.withdraw())
            exitbtn.pack()

    editbtn = Button(ChooseStaffWin, text="View Record", command=editStaff)
    editbtn.pack()

