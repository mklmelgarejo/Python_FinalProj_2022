import time

class Vehicle:
    def __init__(self, v_type, plate):
        self.type = v_type  # store the type of vehicle (1 for car, 2 for truck, 3 for motorcycle)
        self.plate = plate  # store the license plate number of the vehicle
        self.entry_time = time.time()  # store the time when the vehicle entered the parking lot
        self.exit_time = None  # store the time when the vehicle left the parking lot (set to None initially)

    def compute_fare(self):
        pass   
        # currently this method doesn't do anything, but it could be used to calculate the fare
        # for a vehicle based on its type, entry time, and exit time

    def get_type(self):
        return self.type
        # return the type of vehicle (1 for car, 2 for truck, 3 for motorcycle)

    def get_type_string(self):
        return "Car" if self.type == 1 else "Truck" if self.type == 2 else "Motorcycle"
        # return a string representation of the vehicle's type (e.g. "Car", "Truck", or "Motorcycle")

    def get_plate(self):
        return self.plate
        # return the license plate number of the vehicle

    def get_entry_time(self):
        return self.entry_time
        # return the time when the vehicle entered the parking lot

    def set_entry_time(self, new_time):
        self.entry_time = new_time
        # set the time when the vehicle entered the parking lot to the given time

    def get_vehicle(self):
        return self.type, self.plate, self.entry_time
        # return a tuple containing the type, license plate number, and entry time of the vehicle
