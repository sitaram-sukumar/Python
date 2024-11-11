carsLst = [
    {"Make": "Ford", "Model": "Fiesta", "Mileage": 20000, "Gas_Consumed" : 500},
    {"Make": "Ford", "Focus": "Focus", "Mileage": 17000, "Gas_Consumed" : 300},
    {"Make": "Toyota", "Model": "Camry", "Mileage": 25000, "Gas_Consumed" : 350},
    {"Make": "Nissan", "Model": "Altima", "Mileage": 21000, "Gas_Consumed" : 450},
];


car1 ={
        "Make": "Ford",
        "Model": "Fiesta",
        "Mileage": 20000,
        "Gas_Consumed" : 500
    };

def calculate_mpg():
    car ={
        "Make": "Ford",
        "Model": "Fiesta",
        "Mileage": 20000,
        "Gas_Consumed" : 500
    };

    mpg = car["Mileage"]/car["Gas_Consumed"];
    name = f"{car['Make']} - {car['Model']}";
    print("Inside calculate_mpg NO param");
    print(f"{name} gives a mileage of {mpg} miles per gallon");

def calculate_mpg(car_Calc):
    print("Inside calculate_mpg with param");
    mpg = car_Calc["Mileage"]/car_Calc["Gas_Consumed"];
    name = f"{car_Calc['Make']} - {car_Calc['Model']}";
    print(f"{name} gives a mileage of {mpg} miles per gallon");

calculate_mpg(car1);
calculate_mpg({
    "Make": "Toyota",
    "Model": "Camry",
    "Mileage": 25000,
    "Gas_Consumed" : 550
});

for car in carsLst:
    calculate_mpg(car1);

