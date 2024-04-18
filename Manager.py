def Manager():
    print("\nWelcome Manager what would you like to do?")
    print("1. View Staff Records")
    print("2. Register New Records")
    print("3. Update Staff Records")
    print("4. Delete Staff Records")
    print("5. Exit")

    def view_staff_records():
        with open ("credentials.txt") as credentials:
            credentials = credentials.readlines()
            print("")
            for user in credentials:
                print(user.strip())
        Manager()
    def register_new_records():
        print("Registering New Staff Member...")
        status_validate = staff_role_validate = username_validate = password_validate = name_validate = date_validate = True
        record = []
        while username_validate:
            username = input("Enter username of new staff: ")
            if len(username) < 4:
                print("Username too short, please enter at least 4 characters.")
            elif len(username) > 12:
                print("Username too long, please enter at max 13 characters.")
            else:
                username_validate = False
        while password_validate:
            password = input("Enter password: ")
            if len(password) < 6:
                print("Password too short, please enter at least 6 characters.")
            elif len(password) > 16:
                print("Password too long, please enter at max 16 characters.")
            else:
                password_validate = False
        while staff_role_validate:
            staff_role = input("Enter staff role: ")
            match staff_role.lower():
                case "manager":
                    staff_role_validate = False
                    staff_role = "Manager"
                case "stfcss1":
                    staff_role_validate = False
                    staff_role = "STFCSS1"
                case "stfcss2":
                    staff_role_validate = False
                    staff_role = "STFCSS2"
                case "stfcar":
                    staff_role_validate = False
                    staff_role = "STFCAR"
            if staff_role_validate:
                print("Invalid Staff Role")
        while name_validate:
            name = input("Enter name of new staff: ")
            if len(name) < 2:
                print("Please enter a valid name")
            elif len(name) > 30:
                print("Maximum 30 characters allowed")
            else:
                name_validate = False
        while date_validate:
            date_of_register = input("Enter Date of registration(DD/MM/YYYY): ")
            date_array = date_of_register.split("/")
            if len(date_of_register) < 8:
                print("Invalid Date")
            elif len(date_of_register) > 10:
                print("Invalid Date")
            elif len(date_array) != 3:
                print("Invalid Date")
            elif not date_array[0].isdigit() and not date_array[1].isdigit() and not date_array[2].isdigit():
                print("Invalid Date")
            elif int(date_array[0]) > 31 or int(date_array[1]) > 12 or int(date_array[2]) > 2050 or int(date_array[2]) < 2000:
                print("Invalid Date")
            elif len(date_array[2]) != 4:
                print("Invalid Date")
            else:
                date_validate = False
        while status_validate:
            status = input("Enter status(Active/Inactive): ")
            match status.lower():
                case "active":
                    status = "Active"
                    status_validate = False
                case "inactive":
                    status = "Inactive"
                    status_validate = False
                case _:
                    print("Invalid Status")
        record.append([username, password, staff_role, name, date_of_register, status, "\n"])
        with open ("credentials.txt") as credentials:
            credentials_read = credentials.readlines()
            credentials_read.append(';'.join(record[0]))
        with open("credentials.txt", "w") as credentials:
            credentials.writelines(credentials_read)
    def update_staff_records():
        user_choice = input("Enter username of staff to update: ")
        credentials_array = []
        username_found = False
        staff_index = 0
        status_validate = staff_role_validate = username_validate = password_validate = name_validate = date_validate = True
        with open ("credentials.txt") as credentials:
            credentials_read = credentials.readlines()
            for i in range(len(credentials_read)):
                credentials_array.append(credentials_read[i].split(";"))
            for j in range(len(credentials_array)):
                username = credentials_array[j][0]
                if user_choice == username:
                    print("Staff Found!")
                    staff_index = j
                    username_found = True
        def update_in_file(clmn, rplcmnt):
            credentials_array[staff_index][clmn] = rplcmnt
            writable_credentials = []
            for m in range(len(credentials_array)):
                writable_credentials.append(";".join(credentials_array[m]))
            with open("credentials.txt", "w") as credentials_file:
                credentials_file.writelines(writable_credentials)
                print("Successfully updated")
                credentials_file.close()
            Manager()
        if username_found:
            column = input("Which Entry would you like to change?(Username, Password, Role, Name, Date of Register, Status:\n")
            match column.lower():
                case "username":
                    while username_validate:
                        replacement = input("Enter new username: ")
                        if len(replacement) < 4:
                            print("Username too short, please enter at least 4 characters.")
                        elif len(replacement) > 12:
                            print("Username too long, please enter at max 13 characters.")
                        else:
                            username_validate = False
                            update_in_file(0, replacement)
                case "password":
                    while password_validate:
                        replacement = input("Enter new password: ")
                        if len(replacement) < 6:
                            print("Password too short, please enter at least 6 characters.")
                        elif len(replacement) > 16:
                            print("Password too long, please enter at max 16 characters.")
                        else:
                            password_validate = False
                            update_in_file(1, replacement)
                case "role":
                    while staff_role_validate:
                        replacement = input("Enter new staff role: ")
                        match replacement.lower():
                            case "manager":
                                staff_role_validate = False
                                replacement = "Manager"
                                update_in_file(2, replacement)
                            case "stfcss1":
                                staff_role_validate = False
                                replacement = "STFCSS1"
                                update_in_file(2, replacement)
                            case "stfcss2":
                                staff_role_validate = False
                                replacement = "STFCSS2"
                                update_in_file(2, replacement)
                            case "stfcar":
                                staff_role_validate = False
                                replacement = "STFCAR"
                                update_in_file(2, replacement)
                        if staff_role_validate:
                            print("Invalid Staff Role")
                case "name":
                    while name_validate:
                        replacement = input("Enter name of new staff: ")
                        if len(replacement) < 2:
                            print("Please enter a valid name")
                        elif len(replacement) > 30:
                            print("Maximum 30 characters allowed")
                        else:
                            name_validate = False
                            update_in_file(3, replacement)
                case "date of register":
                    while date_validate:
                        replacement = input("Enter New Date of registration(DD/MM/YYYY): ")
                        date_array = replacement.split("/")
                        if len(replacement) < 8:
                            print("Invalid Date")
                        elif len(replacement) > 10:
                            print("Invalid Date")
                        elif len(date_array) != 3:
                            print("Invalid Date")
                        elif not date_array[0].isdigit() and not date_array[1].isdigit() and not date_array[
                            2].isdigit():
                            print("Invalid Date")
                        elif int(date_array[0]) > 31 or int(date_array[1]) > 12 or int(date_array[2]) > 2050 or int(
                                date_array[2]) < 2000:
                            print("Invalid Date")
                        elif len(date_array[2]) != 4:
                            print("Invalid Date")
                        else:
                            date_validate = False
                            update_in_file(4, replacement)
                case "status":
                    while status_validate:
                        replacement = input("Enter status(Active/Inactive): ")
                        match replacement.lower():
                            case "active":
                                replacement = "Active"
                                status_validate = False
                                update_in_file(5, replacement)
                            case "inactive":
                                replacement = "Inactive"
                                status_validate = False
                                update_in_file(5, replacement)
                            case _:
                                print("Invalid Status")
                case _:
                    print("Invalid Entry Please choose from existing entries")
        else:
            print("Username not found")
            update_staff_records()
    def delete_staff_records():
        delete_query = input("Enter username of user to delete: ")
        credentials_array = []
        writable_credentials = []
        username_found = False
        with open("credentials.txt") as credentials:
            credentials_read = credentials.readlines()
            for credential in credentials_read:
                credentials_array.append(credential.split(";"))
            for x in range(len(credentials_array)):
                if credentials_array[x][0].lower() == delete_query.lower():
                    credentials_array.pop(x)
                    username_found = True
                    break
            for y in range(len(credentials_array)):
                writable_credentials.append(";".join(credentials_array[y]))
        with open("credentials.txt", "w") as credentials:
            credentials.writelines(writable_credentials)
        if not username_found:
            print("Username not found")
            delete_staff_records()
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            view_staff_records()
        case "2":
            register_new_records()
        case "3":
            update_staff_records()
        case "4":
            delete_staff_records()
        case "5":
            raise SystemExit("Exit")
        case _:
            print("Invalid")

#Moved Manager() to index.py Run code from there