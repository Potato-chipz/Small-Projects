"""To scan a car when enters the parking lot, store the plate number in a list. When exits can put in the plate number on a person's phone, and if matches, can pay the pakring lot fee """

open = True # parking lot is open 
car_in = [] 

while open:
    # 1 for car coming in, 0 for car coming out 
    option = input("Please select the option, 1 for IN, 0 for OUT: ")

    if option == '1': 
        
        "Scan the car that comes into the parking lot"
        car = input("Car coming in! Enter the plate number: ")
        car_in.append(car)

    elif option == '0': 
        flag = 1
        while flag:
            "Enter the plate number in parking lot"
            car_out = input("Car going out! Enter the plate number: ")

            for i in car_in: 
                if i == car_out: 
                    print("Payment: $10")
                    car_in.remove(car_out) #remove the car in the park
                    print(f'Car still in PL: {car_in}')
                    flag = 0
                else: 
                    print("Please re-enter")
