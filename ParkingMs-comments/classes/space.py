import time

class Space:
    # Initialize the Space object with no vehicle and unoccupied status
    def __init__(self):
        self.vehicle = None
        self.occupied = False

    # Add a vehicle to the space and mark it as occupied
    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.vehicle.exit_time = None
        self.occupied = True

    # Remove the vehicle from the space and mark it as unoccupied
    # Return the vehicle that was removed
    def remove_vehicle(self):
        v_exit = self.vehicle
        v_exit.exit_time = time.time()
        self.vehicle = None
        self.occupied = False
        return v_exit

    # Return the vehicle currently occupying the space
    def vehicle_info(self):
        return self.vehicle

    # Return whether the space is currently occupied or not
    def is_available(self):
        return self.occupied
