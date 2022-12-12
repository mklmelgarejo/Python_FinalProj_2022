import math
import time

from classes.vehicle_info import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plate):
        super().__init__(3, plate)

    def compute_fare(self):
        total_time = time.time() - self.get_entry_time()
        if total_time < 3600:
            hours = 1
            extra = 0
            tot_hours = hours + extra
            fare = 10 * tot_hours
        else:
            hours = math.ceil(total_time / 3600)
            extra = hours - 1
            tot_hours = hours + extra
            fare = 10 * tot_hours
        return fare