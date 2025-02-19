class Car:
    def drive(self):
        return "Driving a car 🚗"

class Bike:
    def drive(self):
        return "Riding a bike 🏍️"

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type!")

# Testing
vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.drive())  # Output: Driving a car 🚗

vehicle = VehicleFactory.get_vehicle("bike")
print(vehicle.drive())  # Output: Riding a bike 🏍️
