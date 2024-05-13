def CSS2():
    def renting():
        print("Customer requirements for car")
        brand = input("Enter desired brand of car: ")
        model = input("Enter desired model of car: ")
        with open("car_db.txt", "r") as car_db:
            car_db = car_db.readlines()
            cars = []
            for i in range(len(car_db)):
                cars.append(car_db[i].split(";"))
            for j in range(len(cars)):
                if cars[j][1] == brand and cars[j][2]:
                    print(cars[j])
            license_ = input("Enter license plate of car desired: ")
            license_valid = False
            for k in range(len(cars)):
                if cars[k][0] == license_:
                    license_valid = True
                    if cars[k][10] == "Available":
                        carindex = k
                        customer_id = input("Enter customer ID: ")
                        with open("customer.txt", "r") as customer_db:
                            customer_db = customer_db.readlines()
                            customers = []
                            for l in range(len(customer_db)):
                                customers.append(customer_db[l].split(";"))
                            idfound = False
                            for m in range(len(customers)):
                                if customers[m][0] == customer_id:
                                    idfound = True
                                    rental_date = input("Enter rental date (DD-MM-YYY): ")
                                    return_date = input("Enter return date (DD-MM-YYY): ")
                                    rental_day, rental_month, rental_year = map(int, rental_date.split('-'))
                                    return_day, return_month, return_year = map(int, return_date.split('-'))
                                    renting_period = str((return_year - rental_year) * 365 + (
                                                return_month - rental_month) * 30 + (return_day - rental_day))
                                    rent_total = float(cars[carindex][9]) * float(renting_period)
                                    rent_total = str(rent_total)
                                    print("Rent Total is " + rent_total)
                                    transactions = [license_, customer_id, rental_date, return_date, renting_period, rent_total + "\n"]
                                    with open("transaction_history.txt", "a") as transaction_history:
                                        transaction_history.write(";".join(transactions))
                                    print("Transaction Successfully Saved")
                                    cars[carindex][10] = "Rented"
                                    cars[carindex][11] = rental_date
                                    cars[carindex][12] = return_date + "\n"
                                    cars_written = []
                                    for x in range(len(cars)):
                                        cars_written.append(";".join(cars[x]))
                                    with open("car_db.txt", "w") as car_db_w:
                                        car_db_w.writelines(cars_written)
                            if not idfound:
                                print("Customer Not Found")
                                CSS2()
                    else:
                        print("This vehicle is not available, please select another.")
                        CSS2()
            if not license_valid:
                print("Not found")
                CSS2()

    def returning():
        print("Which car are you returning")
        brand = input("Enter brand of car: ")
        model = input("Enter model of car: ")
        with open("car_db.txt", "r") as car_db:
            car_db = car_db.readlines()
            cars = []
            for i in range(len(car_db)):
                cars.append(car_db[i].split(";"))
            for j in range(len(cars)):
                if cars[j][1] == brand and cars[j][2]:
                    print(cars[j])
            license_ = input("Enter license plate of car: ")
            license_valid = False
            for k in range(len(cars)):
                if cars[k][0] == license_:
                    license_valid = True
                    if cars[k][10] == "Rented" or cars[k][10] == "Reserved":
                        carindex = k
                        customer_id = input("Enter customer ID: ")
                        with open("customer.txt", "r") as customer_db:
                            customer_db = customer_db.readlines()
                            customers = []
                            for l in range(len(customer_db)):
                                customers.append(customer_db[l].split(";"))
                            idfound = False
                            for m in range(len(customers)):
                                if customers[m][0] == customer_id:
                                    idfound = True
                                    cars[carindex][10] = "Available"
                                    cars[carindex][11] = "null"
                                    cars[carindex][12] = "null" + "\n"
                                    cars_written = []
                                    for x in range(len(cars)):
                                        cars_written.append(";".join(cars[x]))
                                    with open("car_db.txt", "w") as car_db_w:
                                        car_db_w.writelines(cars_written)
                                    print("Car returned.")
                            if not idfound:
                                print("Customer Not Found")
                                CSS2()
                    else:
                        print("This vehicle is not available, please select another.")
                        CSS2()
            if not license_valid:
                print("Not found")
                CSS2()

    def booking():
        print("Customer requirements for car")
        brand = input("Enter desired brand of car: ")
        model = input("Enter desired model of car: ")
        with open("car_db.txt", "r") as car_db:
            car_db = car_db.readlines()
            cars = []
            for i in range(len(car_db)):
                cars.append(car_db[i].split(";"))
            for j in range(len(cars)):
                if cars[j][1] == brand and cars[j][2]:
                    print(cars[j])
            license_ = input("Enter license plate of car desired: ")
            license_valid = False
            for k in range(len(cars)):
                if cars[k][0] == license_:
                    license_valid = True
                    if cars[k][10] == "Available":
                        carindex = k
                        customer_id = input("Enter customer ID: ")
                        with open("customer.txt", "r") as customer_db:
                            customer_db = customer_db.readlines()
                            customers = []
                            for l in range(len(customer_db)):
                                customers.append(customer_db[l].split(";"))
                            idfound = False
                            for m in range(len(customers)):
                                if customers[m][0] == customer_id:
                                    idfound = True
                                    rental_date = input("Enter booking date (DD-MM-YYY): ")
                                    return_date = input("Enter return date (DD-MM-YYY): ")
                                    rental_day, rental_month, rental_year = map(int, rental_date.split('-'))
                                    return_day, return_month, return_year = map(int, return_date.split('-'))
                                    renting_period = str((return_year - rental_year) * 365 + (
                                            return_month - rental_month) * 30 + (return_day - rental_day))
                                    rent_total = float(cars[carindex][9]) * float(renting_period)
                                    rent_total = str(rent_total)
                                    print("Rent Total is " + rent_total)
                                    transactions = [license_, customer_id, rental_date, return_date, renting_period,
                                                    rent_total + "\n"]
                                    with open("transaction_history.txt", "a") as transaction_history:
                                        transaction_history.write(";".join(transactions))
                                    print("Transaction Successfully Saved")
                                    cars[carindex][10] = "Reserved"
                                    cars[carindex][11] = rental_date
                                    cars[carindex][12] = return_date + "\n"
                                    cars_written = []
                                    for x in range(len(cars)):
                                        cars_written.append(";".join(cars[x]))
                                    with open("car_db.txt", "w") as car_db_w:
                                        car_db_w.writelines(cars_written)
                            if not idfound:
                                print("Customer Not Found")
                                CSS2()
                    else:
                        print("This vehicle is not available, please select another.")
                        CSS2()
            if not license_valid:
                print("Not found")
                CSS2()

    css2_choice = input("Would you like to\n1. Rent a car\n2. Return a car\n3. Book a car\nInput a number 1, 2, or 3: ")
    match css2_choice:
        case "1": renting()
        case "2": returning()
        case "3": booking()
