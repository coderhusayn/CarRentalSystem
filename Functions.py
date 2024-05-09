# Used in carServiceStaff.py and CSS1.py
def UpdateProfile():
    print('Please enter your username and password')

    loginAttempt = 3

    while loginAttempt >= 1:
        print('\n\033[1mLogin\033[0m')
        userName = input('Username: ').strip()
        userPass = input('Password: ').strip()

        with open('credentials.txt', 'r') as loginDetail:
            loginDetail = loginDetail.readlines()

        for line_index, line in enumerate(loginDetail):
            data = line.strip().split(';')

            if userName == data[0] and userPass == data[1]:
                while True:
                    updateMenu = '''\033[1mPlease select what you would like to change            \033[0;31m[q] Logout\033[0m\n
[1] Username
[2] Password

>>> '''
                    updateChoice = input(updateMenu)
                    if updateChoice == '1':
                        newUser = input("Please enter your new username\n>>> ")
                        data[0] = newUser
                    elif updateChoice == '2':
                        newPass = input("Please enter your new password\n>>> ")
                        data[1] = newPass
                    elif updateChoice.lower() == 'q':
                        break
                    else:
                        print("Invalid choice!")

                # Update the line in loginDetail with the modified data
                loginDetail[line_index] = ';'.join(data) + '\n'

                # Write the updated loginDetail back to the file
                with open('credentials.txt', 'w') as credentials_file:
                    credentials_file.writelines(loginDetail)

                print('\033[1;32mSucessfully updated account. Please login again\033[0m')
                from index import index
                index()

        loginAttempt -= 1
        if loginAttempt > 0:
            print(f'\n\033[0;31m\033[1mIncorrect username or password. {loginAttempt} tries left.\033[0m')
        else:
            raise SystemExit('\033[0;31m\033[1mLogin failed after 3 attempts.\033[0m')



# Used in carServiceStaff.py and CSS1.py
def InputDate(prompt):
    START_YEAR = 2010
    END_YEAR = 2024

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



# Used in carServiceStaff.py
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
