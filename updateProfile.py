def updateOwnProfile():
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
