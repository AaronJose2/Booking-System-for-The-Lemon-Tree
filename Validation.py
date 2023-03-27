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
                check = "12345678"

                if customerIDent.get() == "":
                    check = check.replace("1","a")
                elif str(customerIDent.get()[:2]) != "CR":
                    check = check.replace("1","b")
                elif len(customerIDent.get()) != 5:
                    check = check.replace("1","c")
                elif str(customerIDent.get()[2:]).isnumeric() != True:
                    check = check.replace("1","d")
                
                if customerForenameent.get() == "":
                    check = check.replace("2","a")

                if  customerSurnameent.get() == "":
                    check = check.replace("3","a")

                if customerTelephoneNument.get() == "":
                    check = check.replace("4","a")
                elif customerTelephoneNument.get().isnumeric() != True:
                    check = check.replace("4","b")
                elif len(customerTelephoneNument.get()) != 11:
                    check = check.replace("4","c")

                if customerPostcodeent.get() == "":
                    check = check.replace("5","a")
                elif len(customerPostcodeent.get()) > 7:
                    check = check.replace("5","b")
                elif len(customerPostcodeent.get()) < 5:
                    check = check.replace("5","c")

                if customerAddressLine1ent.get() == "":
                    check = check.replace("6","a")

                if customerAddressLine2ent.get() == "":
                    check = check.replace("7","a")

                if customerCityent.get() == "":
                    check = check.replace("8","a")

                if check != "12345678":
                    if "a" == check[0]:
                        messagebox.showerror("Wait!", "The Customer ID field is blank\n To get the original ID back press the button")
                        customerIDregen()
                    elif "b" == check[0]:
                        messagebox.showerror("Wait!", "The Prefix for the Customer ID field is wrong. It should begin with a CR\n To get the original ID back press the button")
                        customerIDregen()
                    elif "c" == check[0]:
                        messagebox.showerror("Wait!", "The length of the Customer ID field is wrong. It should be 5 characters long\n To get the original ID back press the button")
                        customerIDregen()
                    elif "d" == check[0]:
                        messagebox.showerror("Wait!", "The format of the Customer ID field is wrong. It should be CRXXX where the XXX are numerical\n To get the original ID back press the button")
                        customerIDregen()

                    if "a" == check[1]:
                        messagebox.showerror("Wait!", "The Customer Forename field is blank")
                    
                    if "a" == check[2]:
                        messagebox.showerror("Wait!", "The Customer Surname field is blank")
                    
                    if "a" == check[3]:
                        messagebox.showerror("Wait!", "The Customer Telephone Number field is blank")
                    elif "b" == check[3]:
                        messagebox.showerror("Wait!", "The Customer Telephone Number contains non-numeric characters")
                    elif "c" == check[3]:
                        messagebox.showerror("Wait!", "The Customer Telephone Number is not of standard length 11\nif the number is 10 digits long add an extra 0 at the front of the number")

                    if "a" == check[4]:
                        messagebox.showerror("Wait!", "The Customer Postcode field is blank")
                    elif "b" == check[4]:
                        messagebox.showerror("Wait!", "The Customer Postcode field is too long")
                    elif "c" == check[4]:
                        messagebox.showerror("Wait!", "The Customer Postcode field is too short")

                    if "a" == check[5]:
                        messagebox.showerror("Wait!", "The Customer Address Line 1 field is blank")
                    
                    if "a" == check[6]:
                        messagebox.showerror("Wait!", "The Customer Address Line 2 field is blank")
                    
                    if "a" == check[7]:
                        messagebox.showerror("Wait!", "The Customer City field is blank")

                else:
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
                        listCustomerLB.insert(END, customer.customerID +" ~ "+ customer.forename +" "+ customer.surname)

                    saveData()
                    ViewCustomerWin.withdraw()