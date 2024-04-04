def CSS1():
    mainMenu = '''\033[1mCar Rental System | Customer Detail            \033[0;31m[q] Logout\033[0m\n
    [1] Register customer detail \033[0;31m[In Development]\033[0m
    [2] Update customer details
    [3] View registered customers \033[0;31m[In Development]\033[0m
    [4] Update own profile \033[0;31m[In Development]\033[0m
    
    Enter \033[1;32m1, 2, 3, 4\033[0m or \033[0;31mQ\033[0m to Logout\n'''

    print(mainMenu)

    registerCustomer = '1'
    updateCustomer = '2'
    viewCustomer = '3'
    customerProfile = '4'
    logout = 'q'

    CSS1_BACK = 'b'

    while True:
        choice = input('>>> ').lower()
        if choice not in [registerCustomer, updateCustomer, viewCustomer, customerProfile, logout]:
            print(f'\033[0;31m\033[1mError: Please enter {registerCustomer}, {updateCustomer}, {viewCustomer}, {customerProfile} or {logout} as an option.\033[0m')
        else:
            if choice == updateCustomer:
                def updateCustomer():
                    def changeName():
                        while True:
                            currentName = input("Enter the name you wish to update.Type 'q' to exit to main menu (Name is case sensitive).\n>>> ")
                            if currentName.lower() in ['q']:
                                print('\033[1;31mAction terminated, going back to menu\033[0m')
                                updateCustomer()
                            newName = input("Enter the new name.\n>>> ")

                            reNewName = input(f'Name will be changed from \033[1;31m{currentName}\033[0m to \033[1;32m{newName}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            if reNewName not in ['y', 'n']:
                                reNewName = input(f'Name will be changed from \033[1;31m{currentName}\033[0m to \033[1;32m{newName}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            elif reNewName == 'n':
                                changeName()
                            else:
                                nameCheck = 0

                                with open('customer.txt') as customer_file:
                                    accounts = customer_file.readlines()


                                    # Modify data
                                    for index, line in enumerate(accounts):
                                        data = line.split(';')
                                        if data[1] == currentName:
                                            data[1] = newName
                                            accounts[index] = ';'.join(data)
                                        else:
                                            nameCheck += 1

                                    if nameCheck == len(accounts):
                                        print("\033[0;31mUnable to find customer's name\033[0m")
                                        changeName()
                                    else:
                                        print("\033[1;32mCustomer name has been successfully updated!\033[0m")


                                    # Write modified data back to file
                                    with open('customer.txt', 'w') as customer_file:
                                        for line in accounts:
                                            customer_file.write(f'{line}')
                                    print(updateMenu)
                                    return
                    
                    def changeID():
                        while True:
                            currentIdName = input("Enter the customer's name you wish to update.Type 'q' to exit to main menu (Name is case sensitive).\n>>> ")
                            if currentIdName.lower() in ['q']:
                                print('\033[1;31mAction terminated, going back to menu\033[0m')
                                updateCustomer()
                            newId = input("Enter the new ID.\n>>> ")

                            reNewID = input(f'Customer\'s ID will be changed to \033[1;32m{newId}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            if reNewID not in ['y', 'n']:
                                reNewID = input(f'Customer\'s ID will be changed from \033[1;31m{currentIdName}\033[0m to \033[1;32m{newId}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            elif reNewID == 'n':
                                changeID()
                            else:
                                idCheck = 0

                                with open('customer.txt') as customer_file:
                                    accounts = customer_file.readlines()


                                    # Modify data
                                    for index, line in enumerate(accounts):
                                        data = line.split(';')
                                        if data[1] == currentIdName: 
                                            data[2] = newId
                                            accounts[index] = ';'.join(data)
                                        else:
                                            idCheck += 1

                                    if idCheck == len(accounts):
                                        print("\033[0;31mUnable to find customer's name\033[0m")
                                        changeID()
                                    else:
                                        print("\033[1;32mCustomer ID has been successfully updated!\033[0m")


                                    # Write modified data back to file
                                    with open('customer.txt', 'w') as customer_file:
                                        for line in accounts:
                                            customer_file.write(f'{line}')
                                    print(updateMenu)
                                    return
                    
                    def changeLicense():
                        while True:
                            currentLicenseName = input("Enter the customer's name you wish to update.Type 'q' to exit to main menu (Name is case sensitive).\n>>> ")
                            if currentLicenseName.lower() in ['q']:
                                print('\033[1;31mAction terminated, going back to menu\033[0m')
                                updateCustomer()
                            newLicense = input("Enter the new License.\n>>> ")

                            reNewLicense = input(f'Customer\'s License will be changed to \033[1;32m{newLicense}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            if reNewLicense not in ['y', 'n']:
                                reNewLicense = input(f'Customer\'s License will be changed to \033[1;32m{newLicense}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            elif reNewLicense == 'n':
                                changeLicense()
                            else:
                                licenseCheck = 0

                                with open('customer.txt') as customer_file:
                                    accounts = customer_file.readlines()


                                    # Modify data
                                    for index, line in enumerate(accounts):
                                        data = line.split(';')
                                        if data[1] == currentLicenseName: 
                                            data[3] = newLicense
                                            accounts[index] = ';'.join(data)
                                        else:
                                            licenseCheck += 1

                                    if licenseCheck == len(accounts):
                                        print("\033[0;31mUnable to find customer's name\033[0m")
                                        changeLicense()
                                    else:
                                        print("\033[1;32mCustomer License has been successfully updated!\033[0m")


                                    # Write modified data back to file
                                    with open('customer.txt', 'w') as customer_file:
                                        for line in accounts:
                                            customer_file.write(f'{line}')
                                    print(updateMenu)
                                    return
                    
                    def changeAddress():
                        while True:
                            currentAddressName = input("Enter the customer's name you wish to update.Type 'q' to exit to main menu (Name is case sensitive).\n>>> ")
                            if currentAddressName.lower() in ['q']:
                                print('\033[1;31mAction terminated, going back to menu\033[0m')
                                updateCustomer()
                            newAddress = input("Enter the new Address.\n>>> ")

                            reNewAddress = input(f'Customer\'s Address will be changed to \033[1;32m{newAddress}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            if reNewAddress not in ['y', 'n']:
                                reNewAddress = input(f'Customer\'s Address will be changed to \033[1;32m{newAddress}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            elif reNewAddress == 'n':
                                changeAddress()
                            else:
                                addressCheck = 0

                                with open('customer.txt') as customer_file:
                                    accounts = customer_file.readlines()


                                    # Modify data
                                    for index, line in enumerate(accounts):
                                        data = line.split(';')
                                        if data[1] == currentAddressName: 
                                            data[4] = newAddress
                                            accounts[index] = ';'.join(data)
                                        else:
                                            addressCheck += 1

                                    if addressCheck == len(accounts):
                                        print("\033[0;31mUnable to find customer's name\033[0m")
                                        changeAddress()
                                    else:
                                        print("\033[1;32mCustomer Address has been successfully updated!\033[0m")


                                    # Write modified data back to file
                                    with open('customer.txt', 'w') as customer_file:
                                        for line in accounts:
                                            customer_file.write(f'{line}')
                                    print(updateMenu)
                                    return
                    
                    def changeContact():
                        while True:
                            currentContactName = input("Enter the customer's name you wish to update.Type 'q' to exit to main menu (Name is case sensitive).\n>>> ")
                            if currentContactName.lower() in ['q']:
                                print('\033[1;31mAction terminated, going back to menu\033[0m')
                                updateCustomer()
                            newContact = input("Enter the new Contact.\n>>> ")

                            reNewContact = input(f'Customer\'s Contact will be changed to \033[1;32m{newContact}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            if reNewContact not in ['y', 'n']:
                                reNewContact = input(f'Customer\'s Contact will be changed to \033[1;32m{newContact}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                            elif reNewContact == 'n':
                                changeAddress()
                            else:
                                contactCheck = 0

                                with open('customer.txt') as customer_file:
                                    accounts = customer_file.readlines()


                                    # Modify data
                                    for index, line in enumerate(accounts):
                                        data = line.split(';')
                                        if data[1] == currentContactName: 
                                            data[5] = newContact
                                            accounts[index] = ';'.join(data)
                                        else:
                                            contactCheck += 1

                                    if contactCheck == len(accounts):
                                        print("\033[0;31mUnable to find customer's name\033[0m")
                                        changeAddress()
                                    else:
                                        print("\033[1;32mCustomer Contact has been successfully updated!\033[0m")


                                    # Write modified data back to file
                                    with open('customer.txt', 'w') as customer_file:
                                        for line in accounts:
                                            customer_file.write(f'{line}')
                                    print(updateMenu)
                                    return
                    
                    updateMenu = '''\033[1mCar Rental System | Customer Detail | Update Customer Detail            \033[0;31m[q] Logout\033[0m\n
    [1] Update Customer Name
    [2] Update Customer IC/Passport
    [3] Update Cusomter License Number
    [4] Update Customer Address
    [5] Update Customer Contact Number
        
    Enter \033[1;32m1, 2, 3, 4, 5\033[0m or \033[0;31mQ\033[0m to go back to menu\n'''
                    
                    print(updateMenu)

                    while True:
                        updateMenuChoice = input('>>> ').lower()
                        if updateMenuChoice not in ['1', '2', '3', '4', '5', 'q']:
                            print(f'\033[0;31m\033[1mError: Please enter 1, 2, 3, 4, 5 or \'Q\' as an option.\033[0m')
                        elif updateMenuChoice == '1':
                            changeName()
                        elif updateMenuChoice == '2':
                            changeID()
                        elif updateMenuChoice == '3':
                            changeLicense()
                        elif updateMenuChoice == '4':
                            changeAddress()
                        elif updateMenuChoice == '5':
                            changeContact()
                        elif updateMenuChoice == 'q':
                            print('\033[1;31mAction terminated, going back to menu\033[0m')
                            return CSS1()
                        
                updateCustomer()
                
                

            elif choice == logout:
                raise SystemExit("\033[1;32mYou have logged out\033[0m")
                

CSS1()
