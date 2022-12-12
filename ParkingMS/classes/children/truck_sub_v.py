import math
import time

from classes.vehicle_info import Vehicle

class Truck(Vehicle):
    def __init__(self, plate):
        super().__init__(2, plate)

    def compute_fare(self):
        total_time = time.time() - self.get_entry_time()
        hours = math.ceil(total_time / 3600)
        extra = 0
        tot_hours = hours + extra
        fare = 10 * tot_hours
        return fare
