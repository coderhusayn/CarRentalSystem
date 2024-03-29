choice = input("Would you like to create or update a customer account? (Create/Update)\n>>> ").lower()
if choice == 'create':
    print("Succesfully Created")

elif choice == 'update':
    # Check for invalid search value
    nameCheck = 0

    with open('customer.txt') as customer_file:
        accounts = customer_file.readlines()


        # Modify data
        for index, line in enumerate(accounts):
            data = line.split(';')
            del data[-1]
            if data[1] == "Hussain Rana": #Check for inputted name
                data[1] = "Pavin Raj" #Updated Name
                accounts[index] = ';'.join(data)
                print(accounts)
            else:
                nameCheck += 1

        if nameCheck == len(accounts):
            print("Invalid Name")
        else:
            print("Name succesfully updated!")


    # Write modified data back to file
    with open('customer.txt', 'w') as customer_file:
        for line in accounts:
            customer_file.write(f'{line}')
            # print(line.split(';'))
