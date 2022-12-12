import math
import time

from classes.vehicle_info import Vehicle

class Motorcycle(Vehicle):
    # Initialize the Motorcycle object by calling the parent class (Vehicle) constructor and passing in the appropriate arguments
    def __init__(self, plate):
        super().__init__(3, plate)

    # Compute the fare for the motorcycle based on the amount of time it has been parked
    def compute_fare(self):
        # Calculate the total time the motorcycle has been parked
        total_time = time.time() - self.get_entry_time()

        # If the motorcycle has been parked for less than one hour, the fare is 10 dollars
        if total_time < 3600:
            hours = 1
            extra = 0
            tot_hours = hours + extra
            fare = 10 * tot_hours

        # If the motorcycle has been parked for more than one hour, the fare is 10 dollars plus an additional charge per hour
        else:
            hours = math.ceil(total_time / 3600)  # Calculate the number of hours the motorcycle has been parked
            extra = hours - 1  # Calculate the number of extra hours the motorcycle has been parked
            tot_hours = hours + extra  # Calculate the total number of hours for which the fare will be charged
            fare = 10 * tot_hours  # Calculate the fare by multiplying the hourly rate by the total number of hours

        # Return the calculated fare
        return fare
