import math
import time

from classes.vehicle_info import Vehicle

class Truck(Vehicle):
    # Initialize the Truck object by calling the parent class (Vehicle) constructor and passing in the appropriate arguments
    def __init__(self, plate):
        super().__init__(2, plate)

    # Compute the fare for the truck based on the amount of time it has been parked and its weight
    def compute_fare(self):
        # Calculate the total time the truck has been parked
        total_time = time.time() - self.get_entry_time()

        # Calculate the number of hours the truck has been parked
        hours = math.ceil(total_time / 3600)

        # Initialize the number of extra hours to zero
        extra = 0

        # Calculate the total number of hours for which the fare will be charged
        tot_hours = hours + extra

        # Calculate the fare by multiplying the hourly rate by the total number of hours
        fare = 10 * tot_hours

        # Return the calculated fare
        return fare
