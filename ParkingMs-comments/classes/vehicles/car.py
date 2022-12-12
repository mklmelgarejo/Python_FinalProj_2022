import math
import time

from classes.vehicle_info import Vehicle

class Car(Vehicle):
    # Initialize the Car object by calling the parent class (Vehicle) constructor and passing in the appropriate arguments
    def __init__(self, plate):
        super().__init__(1, plate)

    # Compute the fare for the car based on the amount of time it has been parked
    def compute_fare(self):
        # Calculate the total time the car has been parked
        total_time = time.time() - self.get_entry_time()
        
        # If the car has been parked for less than one hour, the fare is 20 dollars
        if total_time < 3600:
            hours = 1
            extra = 0
            tot_hours = hours + extra
            fare = 20 * tot_hours
        
        # If the car has been parked for more than one hour, the fare is 20 dollars plus an additional charge per hour
        else:
            hours = math.ceil(total_time / 3600)  # Calculate the number of hours the car has been parked
            extra = hours - 1  # Calculate the number of extra hours the car has been parked
            tot_hours = hours + extra  # Calculate the total number of hours for which the fare will be charged
            fare = 20 * tot_hours  # Calculate the fare by multiplying the hourly rate by the total number of hours
        
        # Return the calculated fare
        return fare
