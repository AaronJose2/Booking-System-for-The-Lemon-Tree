from tkinter import *
from pickle import *
from datastructures import *
from FontStyleSheet import *

def CustomerDetailsMenuWindow():
    #creates the Customer Details Menu window
    customerDetailsMenuWin = Toplevel()
    customerDetailsMenuWin.geometry("400x400")
    customerDetailsMenuWin.title("Customer Details Menu")

    # main title
    mainTitle = Label(customerDetailsMenuWin, text="Customer Menu", font=Heading)
    mainTitle.pack()

    viewCustomerbtn = Button(customerDetailsMenuWin, text="View Customer", font=BTN, command=ViewCustomerDetailsWindow)
    viewCustomerbtn.pack()
    
    AddCustomerbtn = Button(customerDetailsMenuWin, text="Add a Customer", font=BTN, command=AddCustomerDetailsWindow)
    AddCustomerbtn.pack()

    EditCustomerbtn = Button(customerDetailsMenuWin, text="Edit Customer Details", font=BTN, command=EditCustomerDetailsWindow)
    EditCustomerbtn.pack()

def ViewCustomerDetailsWindow():
    global listCustomerLB
    #creates the View Customer window
    ViewCustomerWin = Toplevel()
    ViewCustomerWin.geometry("650x400")
    ViewCustomerWin.title("View Customer")

    # main title
    mainTitle = Label(ViewCustomerWin, text="View Customers", font=Heading)
    mainTitle.pack()

    listCustomerLB = Listbox(ViewCustomerWin, width=75, font=SH2)
    listCustomerLB.pack()

    listCustomerLB.delete(0, END)
    for customer in listCustomer:
        listCustomerLB.insert(END, customer.customerID + customer.forename + customer.surname + customer.telephoneNum + customer.postcode + customer.addressLine1 + customer.addressLine2 + customer.city)

def AddCustomerDetailsWindow():
    #creates the View Customer window
    AddCustomerWin = Toplevel()
    AddCustomerWin.geometry("400x600")
    AddCustomerWin.title("Add Customer")

    # main title
    mainTitle = Label(AddCustomerWin, text="Add Customer", font=Heading)
    mainTitle.pack()

    #labels and respseective entries.
    def genreateCustomerID():
        prefix = "CR"
        ID = prefix + str(len(listCustomer)+1).zfill(3)
        CustomerIDvar.set(ID)

    CustomerIDvar = StringVar()
    CustomerIDentry= Entry(AddCustomerWin, textvariable=CustomerIDvar, font=EB)
    CustomerIDentry.pack()
    submitbtn = Button(AddCustomerWin, text="Generate CustomerID", font=BTN, command=genreateCustomerID)
    submitbtn.pack()

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
        #validation

        if True == True:
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

def EditCustomerDetailsWindow():
    ChooseCustomerWin = Toplevel()
    ChooseCustomerWin.geometry("650x400")
    ChooseCustomerWin.title("Choose a Customer's Details to Edit")

    # main title
    mainTitle = Label(ChooseCustomerWin, text="Edit Customers", font=Heading)
    mainTitle.pack()

    listCustomerLB = Listbox(ChooseCustomerWin, font=SH2)
    listCustomerLB.pack()

    listCustomerLB.delete(0,END)
    for customer in listCustomer:
        listCustomerLB.insert(END, customer.customerID + customer.forename + customer.surname + customer.telephoneNum + customer.postcode + customer.addressLine1 + customer.addressLine2 + customer.city)

    def editCustomer():      
        if len(listCustomerLB.curselection()) > 0:
            index = listCustomerLB.curselection()[0]

            EditCustomerWin = Toplevel()
            EditCustomerWin.geometry("400x900")
            EditCustomerWin.title("Edit Customer Details")

            customerIDlbl = Label(EditCustomerWin, text="Customer ID", font=SH1)
            customerIDlbl.pack()
            customerIDvar = StringVar()
            customerIDent = Entry(EditCustomerWin, textvariable=customerIDvar, font=EB)
            customerIDent.pack()
            customerIDvar.set(listCustomer[index].customerID)

            customerForenamelbl = Label(EditCustomerWin, text="Customer Forename", font=SH1)
            customerForenamelbl.pack()
            customerForenamevar = StringVar()
            customerForenameent = Entry(EditCustomerWin, textvariable=customerForenamevar, font=EB)
            customerForenameent.pack()
            customerForenamevar.set(listCustomer[index].forename)

            customerSurnamelbl = Label(EditCustomerWin, text="Customer Surname", font=SH1)
            customerSurnamelbl.pack()
            customerSurnamevar = StringVar()
            customerSurnameent = Entry(EditCustomerWin, textvariable=customerSurnamevar, font=EB)
            customerSurnameent.pack()
            customerSurnamevar.set(listCustomer[index].surname)

            customerTelephoneNumlbl = Label(EditCustomerWin, text="Customer TelephoneNum", font=SH1)
            customerTelephoneNumlbl.pack()
            customerTelephoneNumvar = StringVar()
            customerTelephoneNument = Entry(EditCustomerWin, textvariable=customerTelephoneNumvar, font=EB)
            customerTelephoneNument.pack()
            customerTelephoneNumvar.set(listCustomer[index].telephoneNum)

            customerPostcodelbl = Label(EditCustomerWin, text="Customer Postcode", font=SH1)
            customerPostcodelbl.pack()
            customerPostcodevar = StringVar()
            customerPostcodeent = Entry(EditCustomerWin, textvariable=customerPostcodevar, font=EB)
            customerPostcodeent.pack()
            customerPostcodevar.set(listCustomer[index].postcode)

            customerAddressLine1lbl = Label(EditCustomerWin, text="Customer Address Line 1", font=SH1)
            customerAddressLine1lbl.pack()
            customerAddressLine1var = StringVar()
            customerAddressLine1ent = Entry(EditCustomerWin, textvariable=customerAddressLine1var, font=EB)
            customerAddressLine1ent.pack()
            customerAddressLine1var.set(listCustomer[index].addressLine1)

            customerAddressLine2lbl = Label(EditCustomerWin, text="Customer Address Line 2", font=SH1)
            customerAddressLine2lbl.pack()
            customerAddressLine2var = StringVar()
            customerAddressLine2ent = Entry(EditCustomerWin, textvariable=customerAddressLine2var, font=EB)
            customerAddressLine2ent.pack()
            customerAddressLine2var.set(listCustomer[index].addressLine2)

            customerCitylbl = Label(EditCustomerWin, text="Customer City", font=SH1)
            customerCitylbl.pack()
            customerCityvar = StringVar()
            customerCityent = Entry(EditCustomerWin, textvariable=customerCityvar, font=EB)
            customerCityent.pack()
            customerCityvar.set(listCustomer[index].city)

            def submitfunct():
                if True == True:
                    listCustomer[index].customerID = customerIDent.get()
                    listCustomer[index].forename = customerForenameent.get()
                    listCustomer[index].surname = customerSurnameent.get()
                    listCustomer[index].telephoneNum = customerTelephoneNument.get()
                    listCustomer[index].postcode = customerPostcodeent.get()
                    listCustomer[index].addressLine1 = customerAddressLine1ent.get()
                    listCustomer[index].addressLine2 = customerAddressLine2ent.get()
                    listCustomer[index].city = customerCityent.get()

                    listCustomerLB.delete(0,END)
                    for customer in listCustomer:
                        listCustomerLB.insert(END, customer.customerID + customer.forename + customer.surname + customer.telephoneNum + customer.postcode + customer.addressLine1 + customer.addressLine2 + customer.city)

                    saveData()
                    EditCustomerWin.withdraw()

            submitbtn = Button(EditCustomerWin,text="submit changes", command = submitfunct)
            submitbtn.pack()

    editbtn = Button(ChooseCustomerWin, text="Edit Record", command=editCustomer)
    editbtn.pack()

    
