import time

class Space:
    def __init__(self):
        self.vehicle = None
        self.occupied = False

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.vehicle.exit_time = None
        self.occupied = True

    def remove_vehicle(self):
        v_exit = self.vehicle
        v_exit.exit_time = time.time()
        self.vehicle = None
        self.occupied = False
        return v_exit

    def vehicle_info(self):
        return self.vehicle

    def is_available(self):
        return self.occupied