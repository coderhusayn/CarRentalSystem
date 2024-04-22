import os

# Import updateOwnProfile() function from updateProfile.py
from updateProfile import updateOwnProfile

def CarSerStaff():
    CSS_REGISTER = '1'
    CSS_UPDATE = '2'
    CSS_VIEW = '3'
    CSS_DELETE = '4'
    CSS_PROFILE = '5'

    CSS_BACK = 'B'
    CSS_LOGOUT = 'Q'

    START_YEAR = 2010
    END_YEAR = 2024

    MIN_CAPACITY = 1
    MAX_CAPACITY = 11

    ERR_FILE_NOT_FOUND = '\n\033[0;31;1mError: The .txt file does not exist.\033[0m\n'
    ERR_FILE_NO_PERM = '\n\033[0;31;1mError: You do not have permission to access the .txt file.\033[0m\n'


    pageCarSerStaff = f'''\033[1mCar Rental System | Car Service            \033[0;31m[{CSS_LOGOUT}] Logout\033[0m\n
    [1] Register a new car
    [2] Update car details
    [3] View registered cars
    [4] Delete disposed cars
    [5] Update own profile\n
    Enter \033[1;32m1, 2, 3, 4, 5\033[0m or \033[0;31m{CSS_LOGOUT}\033[0m to Logout\n'''

    print(pageCarSerStaff)


    def InputDate(prompt):
        while True:
            try:
                date = input(prompt)
                day, month, year = date.split('-')

                if len(day) != 2 or not day.isdigit() or int(day) < 1 or int(day) > 31:
                    print('\033[0;31;1mError: Please enter a day between 01 and 31.\033[0m')
                    continue
                elif len(month) != 2 or not month.isdigit() or int(month) < 1 or int(month) > 12:
                    print('\033[0;31;1mError: Please enter a month between 01 and 12.\033[0m')
                    continue
                elif len(year) != 4 or not year.isdigit() or int(year) < START_YEAR or int(year) > END_YEAR:
                    print(f'\033[0;31;1mError: Please enter a four digit year between {START_YEAR} and {END_YEAR}.\033[0m')
                    continue
                else:
                    break
            except ValueError:
                print('\033[0;31;1mError: Please enter a date in the format of DD-MM-YYYY.\033[0m')
        return date

    def InputFloat(prompt):
        while True:
            try:
                flt = float(input(prompt))
            except ValueError:
                print('\033[0;31;1mError: Please enter a valid float.\033[0m')
                continue
            else:
                truncated_flt = format(flt, '.2f')
                break
        return truncated_flt


    while True:
        option = input('>>> ').upper()

        if option not in [CSS_REGISTER, CSS_UPDATE, CSS_VIEW, CSS_DELETE, CSS_PROFILE, CSS_LOGOUT]:
            print(f'\033[0;31;1mError: Please enter {CSS_REGISTER}, {CSS_UPDATE}, {CSS_VIEW}, {CSS_DELETE}, {CSS_PROFILE}, or {CSS_LOGOUT} as an option.\033[0m')
        else:
            # Option 1 - Register a new car
            if option == CSS_REGISTER:

                def CarRegister():
                    print('\033[1mCar Details\033[0m\n')

                    registration_no = input('Registration Number: ').upper()                # string [KV 2926 E]
                    manufacturer = input('Manufacturer: ').upper()                          # string [PERODUA]
                    model = input('Model: ').upper()                                        # string [BEZZA]

                    while True:
                        try:
                            year_of_manufacture = int(input(f'Year Of Manufacture (between {START_YEAR} and {END_YEAR}): '))      # integer [2016]
                        except ValueError:
                            print('\033[0;31;1mError: Please enter a valid integer.\033[0m')
                            continue

                        if not (START_YEAR <= year_of_manufacture <= END_YEAR):
                            print(f'\033[0;31;1mError: Please enter a four digit year between {START_YEAR} and {END_YEAR}.\033[0m')
                        else:
                            break

                    while True:
                        try:
                            seating_capacity = int(input(f'Seating Capacity (between {MIN_CAPACITY} and {MAX_CAPACITY} persons): '))   # integer [5 persons]
                        except ValueError:
                            print('\033[0;31;1mError: Please enter a valid integer.\033[0m')
                            continue

                        if not (MIN_CAPACITY <= seating_capacity <= MAX_CAPACITY):
                            print(f'\033[0;31;1mError: Please enter a seating capacity between {MIN_CAPACITY} and {MAX_CAPACITY} persons.\033[0m')
                        else:
                            break

                    last_service_date = InputDate(f'Last Service Date (between {START_YEAR} and {END_YEAR} in DD-MM-YYYY): ')                   # date [30-12-2023]
                    insurance_policy_no = input('Insurance Policy Number: ').upper()                                                            # string [XA123456]
                    insurance_expiry_date = InputDate(f'Insurance Expiry Date (between {START_YEAR} and {END_YEAR} in DD-MM-YYYY): ')           # date [31-12-2024]
                    road_tax_expiry_date = InputDate(f'Road Tax Expiry Date (between {START_YEAR} and {END_YEAR} in DD-MM-YYYY): ')             # date [31-12-2024]

                    rent_rate = 'null'                      # To be filled by Manager (null by default)
                    rent_availability = 'Available'

                    rent_start_date = 'null'                # To be filled by Customer Service Staff II (null by default)
                    rent_end_date = 'null'                  # To be filled by Customer Service Staff II (null by default)

                    try:
                        with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='a') as file: # 'a' - open a file for appending the text or creates a new file if the file does not exist
                            file.write(f'{registration_no};{manufacturer};{model};{year_of_manufacture};{seating_capacity};{last_service_date};{insurance_policy_no};{insurance_expiry_date};{road_tax_expiry_date};{rent_rate};{rent_availability};{rent_start_date};{rent_end_date}\n')

                        print('\033[0;33mSuccessfully registered a new car in the system.\033[0m\n')
                        CarSerStaff()

                    except PermissionError:
                        print(f'{ERR_FILE_NO_PERM}')
                        CarSerStaff()

                CarRegister()

            # Option 2 - Update car details
            if option == CSS_UPDATE:

                def UpdateOptions(export_registration_no):
                    pageCarUpdateOpt = f'''\033[1mUpdate Options for {export_registration_no}                        \033[0;33m[{CSS_BACK}] Go back\033[0m\n
    \033[1mInsurance\033[0m
    [1] Policy Number
    [2] Expiry Date\n
    \033[1mRoad Tax\033[0m
    [3] Expiry Date\n
    \033[1mRental\033[0m
    [4] Rate (per day)
    [5] Availability\n'''

                    print(f'{pageCarUpdateOpt}')

                    CSS_UPDATE_INSNUM = '1'
                    CSS_UPDATE_INSDTE = '2'
                    CSS_UPDATE_TAXDTE = '3'
                    CSS_UPDATE_RTLDAY = '4'
                    CSS_UPDATE_RTLAVL = '5'

                    while True:
                        option = input('>>> ')

                        if option not in [CSS_UPDATE_INSNUM, CSS_UPDATE_INSDTE, CSS_UPDATE_TAXDTE, CSS_UPDATE_RTLDAY, CSS_UPDATE_RTLAVL, CSS_BACK]:
                            print(f'\033[0;31;1mError: Please enter {CSS_UPDATE_INSNUM}, {CSS_UPDATE_INSDTE}, {CSS_UPDATE_TAXDTE}, {CSS_UPDATE_RTLDAY}, {CSS_UPDATE_RTLAVL}, or {CSS_BACK} as an option.\033[0m')
                        else:
                            # Option 2.1 - Update Insurance Policy Number
                            if option == CSS_UPDATE_INSNUM:

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                                    data = file.readlines()

                                for i in range(len(data)):
                                    details = data[i].split(';')
                                    # print(details) # For debugging purpose only
                                    if details[0] == export_registration_no:
                                        print(f'\033[1mThe current Insurance Policy Number for {export_registration_no} is {details[6]}\033[0m\n\nEnter a new value to change:')
                                        newInsNum = input('>>> ').upper()

                                        details[6] = newInsNum
                                        data[i] = ';'.join(details)

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='w') as file:
                                    file.writelines(data)

                                return UpdateOptions(export_registration_no)

                            # Option 2.2 - Update Insurance Expiry Date
                            if option == CSS_UPDATE_INSDTE:

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                                    data = file.readlines()

                                for i in range(len(data)):
                                    details = data[i].split(';')
                                    if details[0] == export_registration_no:
                                        print(f'\033[1mThe current Insurance Policy Expiry Date for {export_registration_no} is {details[7]}\033[0m\n\nEnter a new value to change (between {START_YEAR} and {END_YEAR} in DD-MM-YYYY):')
                                        newInsDte = InputDate('>>> ')

                                        details[7] = newInsDte
                                        data[i] = ';'.join(details)

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='w') as file:
                                    file.writelines(data)

                                return UpdateOptions(export_registration_no)

                            # Option 2.3 - Update Road Tax Expiry Date
                            if option == CSS_UPDATE_TAXDTE:

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                                    data = file.readlines()

                                for i in range(len(data)):
                                    details = data[i].split(';')
                                    if details[0] == export_registration_no:
                                        print(f'\033[1mThe current Road Tax Expiry Date for {export_registration_no} is {details[8]}\033[0m\n\nEnter a new value to change (between {START_YEAR} and {END_YEAR} in DD-MM-YYYY):')
                                        newTaxDte = InputDate('>>> ')

                                        details[8] = newTaxDte
                                        data[i] = ';'.join(details)

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='w') as file:
                                    file.writelines(data)

                                return UpdateOptions(export_registration_no)

                            # Option 2.4 - Update Rental Rate (per day)
                            if option == CSS_UPDATE_RTLDAY:

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                                    data = file.readlines()

                                for i in range(len(data)):
                                    details = data[i].split(';')
                                    if details[0] == export_registration_no:
                                        print(f'\033[1mThe current Rental Rate (per day) for {export_registration_no} is {details[9]}\033[0m\n\nEnter a new value to change:')
                                        newRtlDay = InputFloat('>>> ')

                                        details[9] = newRtlDay
                                        data[i] = ';'.join(details)

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='w') as file:
                                    file.writelines(data)

                                return UpdateOptions(export_registration_no)

                            # Option 2.5 - Update Rental Availability
                            if option == CSS_UPDATE_RTLAVL:

                                statusDict = {'1': 'Available', '2': 'Reserved', '3': 'Rented', '4': 'Under Service', '5': 'Disposed'}

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                                    data = [line.split(';') for line in file.readlines()]

                                for details in data:
                                    if details[0] == export_registration_no:
                                        pageOptRtlAvl = f'''\033[1mThe current Rental Availability for {export_registration_no} is {details[10]}\n
    Select a new status:\033[0m
    [1] Available
    [2] Reserved
    [3] Rented
    [4] Under Service
    [5] Disposed\n'''

                                        print(f'{pageOptRtlAvl}')

                                        while True:
                                            newRtlAvl = input('>>> ')
                                            if newRtlAvl in statusDict:
                                                details[10] = statusDict[newRtlAvl]
                                                break
                                            else:
                                                print('\033[0;31;1mError: Please enter 1, 2, 3, 4, or 5 as an option.\033[0m')

                                with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='w') as file:
                                    file.writelines(';'.join(details) for details in data)

                                return UpdateOptions(export_registration_no)

                            # Option 2.b - Go back
                            if option == CSS_BACK:
                                CarSerStaff()

                            break


                def CarUpdate():
                    print('\033[1mEnter a car registration number:\033[0m')

                    try:
                        with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                            lines = file.readlines()
                            result = []

                            for i in lines:
                                result.append(i.split(';')[0])

                            # print(result) # For debugging purpose only

                            while True:
                                export_registration_no = input('>>> ').upper()

                                if export_registration_no in result:
                                    UpdateOptions(export_registration_no)
                                    break
                                else:
                                    print('\033[0;31;1mError: No such car found.\033[0m')

                    except FileNotFoundError:
                        print(f'{ERR_FILE_NOT_FOUND}')
                        CarSerStaff()
                    except PermissionError:
                        print(f'{ERR_FILE_NO_PERM}')
                        CarSerStaff()

                CarUpdate()

            # Option 3 - View registered cars
            if option == CSS_VIEW:

                def CarView():
                    try:
                        with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                            pageCarView = f'''\033[1mList of Registered Cars                        \033[0;33m[{CSS_BACK}] Go back\033[0m\n
    \033[1mRegistration No.     Manufacturer         Model                Manufacture Year     Seating Capacity     Last Service         Ins. Policy No.      Ins. Expiry          Road Tax Expiry      Rent Rate            Rent Availibility    Rent Start           Rent End\033[0m\n'''

                            print(f'{pageCarView}')

                            for i, line in enumerate(file, start=1):
                                data = line.strip().split(';')
                                formatted_data = ' '.join(f'{item:<20}' for item in data)
                                print(f"{str(i) + '.' :<3} {formatted_data}")

                            print('\n', end='')

                            while True:
                                option = input('>>> ').upper()
                                if option not in CSS_BACK:
                                    print(f'\033[0;31;1mError: Please enter {CSS_BACK} as an option.\033[0m')
                                elif option == CSS_BACK:
                                    CarSerStaff()
                                    break

                    except FileNotFoundError:
                        print(f'{ERR_FILE_NOT_FOUND}')
                        CarSerStaff()
                    except PermissionError:
                        print(f'{ERR_FILE_NO_PERM}')
                        CarSerStaff()

                CarView()

            # Option 4 - Delete disposed cars
            if option == CSS_DELETE:

                def CarDelete():
                    print(f'\033[1;37mEnter \033[0;31;1mDELETE \033[1;37mto remove disposed cars                        \033[0;33m[{CSS_BACK}] Go back\033[0m\n')

                    while True:
                        option = input('>>> ')

                        if option not in ['DELETE', CSS_BACK.lower(), CSS_BACK.upper()]:
                            print(f'\033[0;31;1mError: Please enter DELETE or {CSS_BACK} as an option.\033[0m')
                        else:
                            if option == 'DELETE':
                                try:
                                    with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='r') as file:
                                        data = file.readlines()
                                        notDisposedData = [line for line in data if not line.split(';')[10] == 'Disposed']

                                    with open(os.path.join(os.path.dirname(__file__), 'car_db.txt'), mode='w') as file:
                                        file.writelines(notDisposedData)

                                    print('\033[0;33mSuccessfully removed disposed cars from the system.\033[0m\n')
                                    CarSerStaff()

                                except FileNotFoundError:
                                    print(f'{ERR_FILE_NOT_FOUND}')
                                    CarSerStaff()
                                except PermissionError:
                                    print(f'{ERR_FILE_NO_PERM}')
                                    CarSerStaff()

                            if option.upper() == CSS_BACK:
                                CarSerStaff()

                            break

                CarDelete()

            # Option 5 - Update own profile
            if option == CSS_PROFILE:
                updateOwnProfile()

            # Option q - Logout
            if option == CSS_LOGOUT:
                raise SystemExit("\033[1;32mYou have logged out\033[0m")

            break

# Moved CarSerStaff() to index.py, run code from there