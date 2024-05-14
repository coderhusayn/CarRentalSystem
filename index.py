from Manager import Manager
from CSS1 import CSS1
from CSS2 import CSS2
from CarServiceStaff import CarSerStaff

def index():
    loginAttempt = 3

    while loginAttempt >= 1:
        print('\n\033[1mLogin\033[0m')
        userName = input('Username: ').strip()
        userPass = input('Password: ').strip()

        with open('credentials.txt', 'r') as loginDetail:
            loginDetail = loginDetail.readlines()
        
        for line in loginDetail:
            data = line.split(';')
            del data[-1]
            # print(data) # Check how the data is listed

            if userName == data[0] and userPass == data[1]:
                if data[-1] == 'Active':
                    print(f'\n\033[0;32;1mWelcome, {data[3].title()}!\033[0m\n')
                    if data[2] == 'STFMAN':
                        Manager()
                    elif data[2] == 'STFCUST1':
                        CSS1()
                    elif data[2] == 'STFCUST2':
                        CSS2()
                    elif data[2] == 'STFCAR':
                        CarSerStaff()
                    else:
                        print('\033[0;31m\033[1mUnexpected error has occured, please contact an admin to get it fixed.\033[0m')
                else:
                    raise SystemExit('\033[0;31m\033[1mThere seems to be a problem with your account. Please contact an admin to get it fixed.\033[0m')
        
        loginAttempt -= 1
        if loginAttempt > 0:
            print(f'\n\033[0;31m\033[1mIncorrect username or password. {loginAttempt} tries left.\033[0m')
        else:
            raise SystemExit('\n\033[0;31m\033[1mLogin failed after 3 attempts.\033[0m')

index()