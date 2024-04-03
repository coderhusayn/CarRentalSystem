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
                def changeName():
                    while True:
                        currentName = input("Enter the name you wish to update.Type 'q' to exit to main menu (Name is case sensitive).\n>>> ")
                        if currentName in ['q', 'Q']:
                            print('\033[1;31mAction terminated, going back to menu\033[0m')
                            print(updateMenu)
                            return
                        newName = input("Enter the new name.\n>>> ")

                        reNewName = input(f'Name will be changed from \033[1;31m{currentName}\033[0m to \033[1;32m{newName}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                        if reNewName not in ['y', 'n']:
                            reNewName = input(f'Name will be changed from \033[1;31m{currentName}\033[0m to \033[1;32m{newName}\033[0m. Please confirm. (Y/N)\n>>> ').lower()
                        elif reNewName == 'n':
                            changeName()
                        else:
                            nameCheck = 0 # Check for invalid search value

                            with open('customer.txt') as customer_file:
                                accounts = customer_file.readlines()


                                # Modify data
                                for index, line in enumerate(accounts):
                                    data = line.split(';')
                                    # print(data)
                                    if data[1] == currentName: #Check for inputted name
                                        data[1] = newName #Updated Name
                                        accounts[index] = ';'.join(data)
                                    else:
                                        nameCheck += 1

                                if nameCheck == len(accounts):
                                    print("\033[0;31mInvalid Name\033[0m")
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
                    print('Change ID')
                    print(updateMenu)
                    return
                
                def changeLicense():
                    print('Change License')
                    print(updateMenu)
                    return
                
                def changeAddress():
                    print('Change Address')
                    print(updateMenu)
                    return
                
                def changeContact():
                    print('Change Contact')
                    print(updateMenu)
                    return
                
                updateMenu = '''\033[1mCar Rental System | Customer Detail | Update Customer Detail            \033[0;31m[q] Logout\033[0m\n
    [1] Update Customer Name
    [2] Update Customer IC/Passport \033[0;31m[In Development]\033[0m
    [3] Update Cusomter License Number \033[0;31m[In Development]\033[0m
    [4] Update Customer Address \033[0;31m[In Development]\033[0m
    [5] Update Customer Contact Number \033[0;31m[In Development]\033[0m
    
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
                        
                
                
                

            elif choice == logout:
                print("\033[1;32mYou have logged out\033[0m")
                break

CSS1()
