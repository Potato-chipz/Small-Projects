"""To scan a car when enters the parking lot, store the plate number in a list. When exits can put in the plate number on a person's phone, and if matches, can pay the pakring lot fee """

car_in = [] 
"Scan the car that comes into the parking lot"
car = input("Car coming in! Enter the plate number: ")
car_in.append(car)

flag = True #Re-enter plate number

while (flag): 
    "Enter the plate number when exits the parking lot"
    car_out = input("Car going out! Enter the plate number: ")

    for i in car_in: 
        if i == car_out: 
            print("Payment: $10")
            flag = False
        else: 
            print("Please re-enter the plate number")
