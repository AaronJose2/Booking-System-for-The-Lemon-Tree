from tkinter import *
from tkinter import messagebox
from datastructures import *
from FontStyleSheet import *

#On the Customer Details menu Button, the user will arrive at the follow page
def CustomerDetailsMenuWindow():
    #This page acts as a landing page, and guides the user down two routes
    #The ability to look at a customer and edit their details or add a new one
    #The following code creats a new toplevel window and names it customer details menu
    customerDetailsMenuWin = Toplevel()
    customerDetailsMenuWin.geometry("400x400")
    customerDetailsMenuWin.title("Customer Details Menu")
    #the following creates and packs a title saying customer menu
    #aswell as two buttons that lead you down the routes of viewing and editing; and creation.
    mainTitle = Label(customerDetailsMenuWin, text="Customer Menu", font=Heading)
    mainTitle.pack()

    AddCustomerbtn = Button(customerDetailsMenuWin, text="Create a new Customer", font=BTN, command=AddCustomerDetailsWindow)
    AddCustomerbtn.pack()

    viewCustomerbtn = Button(customerDetailsMenuWin, text="View and Edit Customer Details", font=BTN, command=viewCustomerDetailsWindow)
    viewCustomerbtn.pack()

def AddCustomerDetailsWindow():
    #the first of the two windows relating to customer details is the creation of a new customer.
    # it only makes sense for this one to come first in the list as you cannot view and edit data that does not exist.
    AddCustomerWin = Toplevel()
    AddCustomerWin.geometry("400x530")
    AddCustomerWin.title("Add Customer")

    mainTitle = Label(AddCustomerWin, text="Add Customer", font=Heading)
    mainTitle.pack()
    # following the creation of the title and window, the code then makes numerous labels and entries
    # the labels serve as a indicator to the user what data goes in which entry
    # and the entry serves as a way to collect the data that the user inputs
    # the function named generateCustomerID generates a new customer id with a collective prefix and unique identifier number
    def genreateCustomerID():
        prefix = "CR"
        ID = prefix + str(len(listCustomer)+1).zfill(3)
        CustomerIDvar.set(ID)

    CustomerIDvar = StringVar()
    CustomerIDlbl = Label(AddCustomerWin, text="Customer ID", font=SH1)
    CustomerIDlbl.pack()
    CustomerIDentry= Entry(AddCustomerWin, textvariable=CustomerIDvar, font=EB, state='readonly')
    genreateCustomerID()
    CustomerIDentry.pack()

    CustomerFNamelbl = Label(AddCustomerWin, text="Customer First Name", font=SH1)
    CustomerFNamelbl.pack()
    CustomerFNameentry = Entry(AddCustomerWin, font=EB)
    CustomerFNameentry.pack()

    CustomerSNamelbl = Label(AddCustomerWin, text="Customer Last Name", font=SH1)
    CustomerSNamelbl.pack()
    CustomerSNameentry = Entry(AddCustomerWin, font=EB)
    CustomerSNameentry.pack()

    CustomerTelephoneNumlbl = Label(AddCustomerWin, text="Customers Telephone Number", font=SH1)
    CustomerTelephoneNumlbl.pack()
    CustomerTelephoneNumentry = Entry(AddCustomerWin, font=EB)
    CustomerTelephoneNumentry.pack()

    CustomerPostcodebtn = Label(AddCustomerWin, text="Customers Postcode", font=SH1)
    CustomerPostcodebtn.pack()
    CustomerPostcodeentry = Entry(AddCustomerWin, font=EB)
    CustomerPostcodeentry.pack()

    CustomerAddressLine1btn = Label(AddCustomerWin, text="Customers Address Line 1", font=SH1)
    CustomerAddressLine1btn.pack()
    CustomerAddressLine1entry = Entry(AddCustomerWin, font=EB)
    CustomerAddressLine1entry.pack()

    CustomerAddressLine2btn = Label(AddCustomerWin, text="Customers Address Line 2", font=SH1)
    CustomerAddressLine2btn.pack()
    CustomerAddressLine2entry = Entry(AddCustomerWin, font=EB)
    CustomerAddressLine2entry.pack()

    CustomerCitybtn = Label(AddCustomerWin, text="Customers City", font=SH1)
    CustomerCitybtn.pack()
    CustomerCityentry = Entry(AddCustomerWin, font=EB)
    CustomerCityentry.pack()

    def addCustomerFunct():
        check = "1234567"
                
        if CustomerFNameentry.get() == "":
            check = check.replace("1","a")

        if  CustomerSNameentry.get() == "":
            check = check.replace("2","a")

        if CustomerTelephoneNumentry.get() == "":
            check = check.replace("3","a")
        elif CustomerTelephoneNumentry.get().isnumeric() != True:
            check = check.replace("3","b")
        elif len(CustomerTelephoneNumentry.get()) != 11:
            check = check.replace("3","c")

        if CustomerPostcodeentry.get() == "":
            check = check.replace("4","a")
        elif len(CustomerPostcodeentry.get()) > 7:
            check = check.replace("4","b")
        elif len(CustomerPostcodeentry.get()) < 5:
            check = check.replace("4","c")

        if CustomerAddressLine1entry.get() == "":
            check = check.replace("5","a")

        if CustomerAddressLine2entry.get() == "":
            check = check.replace("6","a")

        if CustomerCityentry.get() == "":
            check = check.replace("7","a")

        if check != "1234567":
            if "a" == check[0]:
                messagebox.showerror("Wait!", "The Customer Forename field is blank")
                    
            if "a" == check[1]:
                messagebox.showerror("Wait!", "The Customer Surname field is blank")
                    
            if "a" == check[2]:
                messagebox.showerror("Wait!", "The Customer Telephone Number field is blank")
            elif "b" == check[2]:
                messagebox.showerror("Wait!", "The Customer Telephone Number contains non-numeric characters")
            elif "c" == check[2]:
                messagebox.showerror("Wait!", "The Customer Telephone Number is not of standard length 11\nif the number is 10 digits long add an extra 0 at the front of the number")

            if "a" == check[3]:
                messagebox.showerror("Wait!", "The Customer Postcode field is blank")
            elif "b" == check[3]:
                messagebox.showerror("Wait!", "The Customer Postcode field is too long")
            elif "c" == check[3]:
                messagebox.showerror("Wait!", "The Customer Postcode field is too short")

            if "a" == check[4]:
                messagebox.showerror("Wait!", "The Customer Address Line 1 field is blank")
                    
            if "a" == check[5]:
                messagebox.showerror("Wait!", "The Customer Address Line 2 field is blank")
                    
            if "a" == check[6]:
                messagebox.showerror("Wait!", "The Customer City field is blank")
        else:
            newCustomer = customer()
            newCustomer.customerID = CustomerIDentry.get()
            newCustomer.forename = CustomerFNameentry.get()
            newCustomer.surname = CustomerSNameentry.get()
            newCustomer.telephoneNum = CustomerTelephoneNumentry.get()
            newCustomer.postcode = CustomerPostcodeentry.get()
            newCustomer.addressLine1 = CustomerAddressLine1entry.get()
            newCustomer.addressLine2 = CustomerAddressLine2entry.get()
            newCustomer.city = CustomerCityentry.get()
            listCustomer.append(newCustomer)
            AddCustomerWin.withdraw() 
            saveData()

    submitbtn = Button(AddCustomerWin, text="Submit", font=BTN, command=addCustomerFunct)
    submitbtn.pack()

def viewCustomerDetailsWindow():
    ChooseCustomerWin = Toplevel()
    ChooseCustomerWin.geometry("450x400")
    ChooseCustomerWin.title("Choose a Customer's Details to View and Edit")

    mainTitle = Label(ChooseCustomerWin, text="View and Edit Customer Details", font=Heading)
    mainTitle.pack()

    listCustomerLB = Listbox(ChooseCustomerWin, width=45, font=SH2)
    listCustomerLB.pack()

    CustomerList = []
    
    for customer in listCustomer:
        appendage = []
        appendage.append(customer.customerID)
        appendage.append(customer.forename)
        appendage.append(customer.surname)
        appendage.append(customer.telephoneNum)
        appendage.append(customer.postcode)
        appendage.append(customer.addressLine1)
        appendage.append(customer.addressLine2)
        appendage.append(customer.city)
        CustomerList.append(appendage)
        
    sortList = CustomerList

    def display():
        listCustomerLB.delete(0,END)
        for customer in CustomerList:
            listCustomerLB.insert(END, customer[0] +" ~ "+ customer[1] +" "+ customer[2])

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


    idSortBtn = Button(ChooseCustomerWin, text="Sort by ID", command=idSort)
    idSortBtn.pack()

    firstNameAlphabeticalSortBtn = Button(ChooseCustomerWin, text="Sort by First Name", command=firstNameSort)
    firstNameAlphabeticalSortBtn.pack()

    lastNameAlphabeticalSortBtn = Button(ChooseCustomerWin, text="Sort by Last Name", command=lastNameSort)
    lastNameAlphabeticalSortBtn.pack()

    def viewCustomer():
        if len(listCustomerLB.curselection()) > 0:
            index = listCustomerLB.curselection()[0]

            ViewCustomerWin = Toplevel()
            ViewCustomerWin.geometry("400x600")
            ViewCustomerWin.title("View Customer Details")

            customerIDlbl = Label(ViewCustomerWin, text="Customer ID", font=SH1)
            customerIDlbl.pack()
            customerIDvar = StringVar()
            customerIDent = Entry(ViewCustomerWin, textvariable=customerIDvar, font=EB, state='readonly')
            customerIDent.pack()
            customerIDvar.set(CustomerList[index][0])

            customerForenamelbl = Label(ViewCustomerWin, text="Customer Forename", font=SH1)
            customerForenamelbl.pack()
            customerForenamevar = StringVar()
            customerForenameent = Entry(ViewCustomerWin, textvariable=customerForenamevar, font=EB, state='readonly')
            customerForenameent.pack()
            customerForenamevar.set(CustomerList[index][1])

            customerSurnamelbl = Label(ViewCustomerWin, text="Customer Surname", font=SH1)
            customerSurnamelbl.pack()
            customerSurnamevar = StringVar()
            customerSurnameent = Entry(ViewCustomerWin, textvariable=customerSurnamevar, font=EB, state='readonly')
            customerSurnameent.pack()
            customerSurnamevar.set(CustomerList[index][2])

            customerTelephoneNumlbl = Label(ViewCustomerWin, text="Customer TelephoneNum", font=SH1)
            customerTelephoneNumlbl.pack()
            customerTelephoneNumvar = StringVar()
            customerTelephoneNument = Entry(ViewCustomerWin, textvariable=customerTelephoneNumvar, font=EB, state='readonly')
            customerTelephoneNument.pack()
            customerTelephoneNumvar.set(CustomerList[index][3])

            customerPostcodelbl = Label(ViewCustomerWin, text="Customer Postcode", font=SH1)
            customerPostcodelbl.pack()
            customerPostcodevar = StringVar()
            customerPostcodeent = Entry(ViewCustomerWin, textvariable=customerPostcodevar, font=EB, state='readonly')
            customerPostcodeent.pack()
            customerPostcodevar.set(CustomerList[index][4])

            customerAddressLine1lbl = Label(ViewCustomerWin, text="Customer Address Line 1", font=SH1)
            customerAddressLine1lbl.pack()
            customerAddressLine1var = StringVar()
            customerAddressLine1ent = Entry(ViewCustomerWin, textvariable=customerAddressLine1var, font=EB, state='readonly')
            customerAddressLine1ent.pack()
            customerAddressLine1var.set(CustomerList[index][5])

            customerAddressLine2lbl = Label(ViewCustomerWin, text="Customer Address Line 2", font=SH1)
            customerAddressLine2lbl.pack()
            customerAddressLine2var = StringVar()
            customerAddressLine2ent = Entry(ViewCustomerWin, textvariable=customerAddressLine2var, font=EB, state='readonly')
            customerAddressLine2ent.pack()
            customerAddressLine2var.set(CustomerList[index][6])

            customerCitylbl = Label(ViewCustomerWin, text="Customer City", font=SH1)
            customerCitylbl.pack()
            customerCityvar = StringVar()
            customerCityent = Entry(ViewCustomerWin, textvariable=customerCityvar, font=EB, state='readonly')
            customerCityent.pack()
            customerCityvar.set(CustomerList[index][7])

            def submitfunct():
                def customerIDregen():
                    def getCustomerID():
                        customerIDvar.set(listCustomer[index].customerID)
                        editbtn.forget()
                    submitbtn.forget()
                    exitbtn.forget()
                    editbtn = Button(ViewCustomerWin, text="Old Customer ID", command = getCustomerID)
                    readbtn.pack()
                    editbtn.pack()
                    submitbtn.pack()
                    exitbtn.pack()
                # Validation of all the date here:
                # using a check number we can easily tell if one or more of the data pieces are incorrect.
                check = "1234567"
                
                if CustomerFNameentry.get() == "":
                    check = check.replace("1","a")

                if  CustomerSNameentry.get() == "":
                    check = check.replace("2","a")

                if CustomerTelephoneNumentry.get() == "":
                    check = check.replace("3","a")
                elif CustomerTelephoneNumentry.get().isnumeric() != True:
                    check = check.replace("3","b")
                elif len(CustomerTelephoneNumentry.get()) != 11:
                    check = check.replace("3","c")

                if CustomerPostcodeentry.get() == "":
                    check = check.replace("4","a")
                elif len(CustomerPostcodeentry.get()) > 7:
                    check = check.replace("4","b")
                elif len(CustomerPostcodeentry.get()) < 5:
                    check = check.replace("4","c")

                if CustomerAddressLine1entry.get() == "":
                    check = check.replace("5","a")

                if CustomerAddressLine2entry.get() == "":
                    check = check.replace("6","a")

                if CustomerCityentry.get() == "":
                    check = check.replace("7","a")

                if check != "1234567":
                    if "a" == check[0]:
                        messagebox.showerror("Wait!", "The Customer Forename field is blank")
                            
                    if "a" == check[1]:
                        messagebox.showerror("Wait!", "The Customer Surname field is blank")
                            
                    if "a" == check[2]:
                        messagebox.showerror("Wait!", "The Customer Telephone Number field is blank")
                    elif "b" == check[2]:
                        messagebox.showerror("Wait!", "The Customer Telephone Number contains non-numeric characters")
                    elif "c" == check[2]:
                        messagebox.showerror("Wait!", "The Customer Telephone Number is not of standard length 11\nif the number is 10 digits long add an extra 0 at the front of the number")

                    if "a" == check[3]:
                        messagebox.showerror("Wait!", "The Customer Postcode field is blank")
                    elif "b" == check[3]:
                        messagebox.showerror("Wait!", "The Customer Postcode field is too long")
                    elif "c" == check[3]:
                        messagebox.showerror("Wait!", "The Customer Postcode field is too short")

                    if "a" == check[4]:
                        messagebox.showerror("Wait!", "The Customer Address Line 1 field is blank")
                            
                    if "a" == check[5]:
                        messagebox.showerror("Wait!", "The Customer Address Line 2 field is blank")
                            
                    if "a" == check[6]:
                        messagebox.showerror("Wait!", "The Customer City field is blank")
                else:
                    listCustomer[index].forename = customerForenameent.get()
                    listCustomer[index].surname = customerSurnameent.get()
                    listCustomer[index].telephoneNum = customerTelephoneNument.get()
                    listCustomer[index].postcode = customerPostcodeent.get()
                    listCustomer[index].addressLine1 = customerAddressLine1ent.get()
                    listCustomer[index].addressLine2 = customerAddressLine2ent.get()
                    listCustomer[index].city = customerCityent.get()

                    listCustomerLB.delete(0,END)
                    
                    saveData()
                    ViewCustomerWin.withdraw()

            def editMode():
                def deleteMode():
                    confirmation = messagebox.askquestion("Wait!", "Are you sure you want to delete that?", icon="warning")
                    if confirmation == "yes":
                        customerForenamevar.set("#Deleted#")
                        customerSurnamevar.set("#Deleted#")
                        customerTelephoneNumvar.set("#Deleted#")
                        customerPostcodevar.set("#Deleted#")
                        customerAddressLine1var.set("#Deleted#")
                        customerAddressLine2var.set("#Deleted#")
                        customerCityvar.set("#Deleted#")

                        listCustomer[index].customerID = customerIDent.get()
                        listCustomer[index].forename = customerForenameent.get()
                        listCustomer[index].surname = customerSurnameent.get()
                        listCustomer[index].telephoneNum = customerTelephoneNument.get()
                        listCustomer[index].postcode = customerPostcodeent.get()
                        listCustomer[index].addressLine1 = customerAddressLine1ent.get()
                        listCustomer[index].addressLine2 = customerAddressLine2ent.get()
                        listCustomer[index].city = customerCityent.get()

                        saveData()
                        ViewCustomerWin.withdraw()

                customerForenameent.configure(state='normal')
                customerSurnameent.configure(state='normal')
                customerTelephoneNument.configure(state='normal')
                customerPostcodeent.configure(state='normal')
                customerAddressLine1ent.configure(state='normal')
                customerAddressLine2ent.configure(state='normal')
                customerCityent.configure(state='normal')

                ViewCustomerWin.title("Edit Customer Details")
                exitbtn.configure(text="Close Without Saving")
                
                editbtn.forget()
                exitbtn.forget()

                readbtn.pack()
                deletebtn.pack()
                submitbtn.pack()
                exitbtn.pack()
                
            def readMode():
                customerForenameent.configure(state='readonly')
                customerSurnameent.configure(state='readonly')
                customerTelephoneNument.configure(state='readonly')
                customerPostcodeent.configure(state='readonly')
                customerAddressLine1ent.configure(state='readonly')
                customerAddressLine2ent.configure(state='readonly')
                customerCityent.configure(state='readonly')
            
                ViewCustomerWin.title("View Customer Details")
                exitbtn.configure(text="Close")

                readbtn.forget()
                submitbtn.forget()
                deletebtn.forget()
                exitbtn.forget()
                
                editbtn.pack()
                exitbtn.pack()

            editbtn = Button(ViewCustomerWin, text="Edit Mode", command = editMode)
            editbtn.pack()

            readbtn = Button(ViewCustomerWin, text="View Mode", command = readMode)

            deletebtn = Button(ViewCustomerWin, text="Delete Record", command = lambda: deleteMode)

            submitbtn = Button(ViewCustomerWin,text="Save Customer Record", command = submitfunct)
            
            exitbtn = Button(ViewCustomerWin,text="Close", command = lambda: ViewCustomerWin.withdraw())
            exitbtn.pack()

    viewbtn = Button(ChooseCustomerWin, text="View Customer", command = viewCustomer)
    viewbtn.pack()
