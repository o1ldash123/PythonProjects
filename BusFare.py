class Vehicle :
    def __init__(self, vehicle_type, base_fare):
        self.vehicle_type = vehicle_type
        self.base_fare = base_fare

    def get_base_fare(self):
        return self.base_fare
    def calculate_fare(self, distance):
        return self.base_fare * distance
class Bus(Vehicle):
    fare = 3.00
    def __init__(self , vehicle_type):
        super().__init__(vehicle_type,Bus.fare)
print("Bus Fare Calculation Program , 3.00$ per stop")  
stops = int(input("Enter number of stops traveled: "))
typeV = "Bus"
bus = Bus(typeV)
total_fare = bus.calculate_fare(stops)
print(f"Total bus fare for {stops} stops is: ${total_fare:.2f}")