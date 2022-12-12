import os
import time
import json
import datetime

from classes.vehicle_info import Vehicle
from classes.space import Space
from classes.vehicles.car import Car
from classes.vehicles.motorcycle import Motorcycle
from classes.vehicles.truck import Truck

spaces = []
avail_spaces = 0
total_spaces = 0
rows = 0

space_count = 0
border = ""

linux = 0


def print_row(row):
    # Initialize the output string
    output = ""
    
    # Add the left border of the row
    output += "|"

    # Loop through each space in the row
    for s in range(space_count * row, space_count * (row + 1)):
        # Check if the space is available
        if not spaces[s].is_available():
            # Add an empty space to the output
            output += "[ ]"
        else:
            # Add a space with the appropriate vehicle type to the output
            output += "["
            output += "c" if spaces[s].vehicle_info().get_type() == 1 \
                else "t" if spaces[s].vehicle_info().get_type() == 2 \
                else "m"
            output += "]"
        # Add a space between each space in the row, except for the last one
        if s < space_count * (row + 1) - 1:
            output += " "
    
    # Add the right border of the row
    output += "|"

    # Return the completed row
    return output


def display_lot():
    # Import global variables
    global spaces, avail_spaces, total_spaces, rows
    
    # Initialize the output string
    output = "\nSPOTS AVAILABLE: " + str(avail_spaces) + "\n"

    # Add the top border of the parking lot
    output += border
    
    # Loop through each row in the parking lot
    for row in range(rows):
        # Add the current row to the output
        output += print_row(row) + "\n"
    
    # Add the bottom border of the parking lot
    output += border
   
    # Clear the terminal (only works on Linux)
    if linux == 1:
        os.system("clear")
    
    # Print the completed parking lot to the terminal
    print(output)


def display_row_selection():
    # Import global variables
    global spaces, avail_spaces, total_spaces, rows
    
    # Initialize the output string
    output = "\nSPOTS AVAILABLE: " + str(avail_spaces) + "\n"

    # Add the top border of the parking lot
    output += border
    
    # Loop through each row in the parking lot
    for row in range(rows):
        # Add the current row to the output
        output += print_row(row)

        # Add a row selection indicator to the output
        output += " <" + str(row) + ">\n"
    
    # Add the bottom border of the parking lot
    output += border
    
    # Clear the terminal (only works on Linux)
    if linux == 1:
        os.system("clear")
    
    # Print the completed parking lot to the terminal
    print(output)


def display_space_selection(row):
    # Import global variables
    global spaces, avail_spaces, total_spaces, rows

    # Initialize the output string
    output = "\nVIEWING ROW: " + row + "\n"

    # Add the top border of the parking lot
    output += border
    
    # Add the specified row to the output
    output += print_row(int(row)) + "\n"

    # Add the space selection indicators to the output
    output += " "
    for count in range(space_count):
        # Add a zero before single-digit space numbers
        if count < 10:
            output += "<" + str(count) + "> "
        else:
            output += "<" + str(count) + ">"

    # Add a newline after the space selection indicators
    output += "\n"
    
    # Add the bottom border of the parking lot
    output += border

    # Clear the terminal (only works on Linux)
    if linux == 1:
        os.system("clear")
    
    # Print the completed parking lot to the terminal
    print(output)

    # Return the number of spaces in the row
    return space_count


def enter_vehicle(v_type, plate, row, space):
    # Import global variables
    global spaces, avail_spaces, total_spaces, rows
    
    # Check if there are any available spaces
    if avail_spaces == 0:
        # Display the parking lot
        display_lot()
        # Print an error message
        print("Error: No Available Spaces")
        # Prompt the user to return to the menu
        input("\n*Press Enter to Return to Menu")
        return

    # Check if the specified space is available
    if spaces[(int(row) * space_count) + int(space)].is_available():
        # Display the space selection menu
        display_space_selection(row)
        # Print an error message
        print("Error: Vehicle Already In Space")
        # Prompt the user to pick a new space
        input("\n*Press Enter to Pick New Space")
        return -1
    
    # Check if the specified vehicle is already in the parking lot
    for uniq in spaces:
        if uniq.is_available():
            if uniq.vehicle_info().get_plate() == plate:
                # Display the parking lot
                display_lot()
                # Print an error message
                print("Error: Vehicle Already In Lot")
                # Prompt the user to park a new vehicle
                input("\n*Press Enter to Park New Vehicle")
                return

    # Create a new vehicle with the specified type and license plate
    new_vehicle = Vehicle(v_type, plate)
    
    # Add the vehicle to the specified space in the parking lot
    spaces[(int(row) * space_count) + int(space)].add_vehicle(new_vehicle)
    
    # Decrement the number of available spaces
    avail_spaces -= 1
    
    # Display the parking lot
    display_lot()
    # Print a success message
    print("Vehicle Added to Lot!\n"
          "Time Entered: " + str(time.strftime('%I:%M %p',
                                               time.localtime(new_vehicle.get_entry_time())))
                                               +"\n")
    # Prompt the user to return to the menu
    input("\n*Press Enter to Return to Menu")

    # Create a json file to store vehicle log
    log_vehicle_details(new_vehicle,0)

    return new_vehicle


def fare_calculation(vehicle):
    # Check the vehicle type
    if vehicle.get_type() == 1:
        # Return the fare for a car
        return Car(vehicle.get_plate()).compute_fare()
    elif vehicle.get_type() == 2:
        # Return the fare for a truck
        return Truck(vehicle.get_plate()).compute_fare()
    elif vehicle.get_type() == 3:
        # Return the fare for a motorcycle
        return Motorcycle(vehicle.get_plate()).compute_fare()


def log_vehicle_details(vehicle, exit_time):
    # Calculate the fare for the vehicle
    fare = fare_calculation(vehicle)

    # Calculate the duration of the vehicle's stay in the parking lot
    duration = exit_time - vehicle.get_entry_time()

    # Create a new log entry for the vehicle
    entry = {"entry_time": vehicle.get_entry_time(),
             "exit_time": exit_time,
             "duration": duration,
             "vehicle_type": vehicle.get_type(),
             "plate_number": vehicle.get_plate(),
             "fare": fare}

    # Open the log file in append mode
    with open("log.json", "a") as log_file:
        # Write the log entry to the log file
        log_file.write(json.dumps(entry))
        # Add a newline after the entry
        log_file.write("\n")


def exit_lot(row, space):
    # Import global variables
    global spaces, avail_spaces, total_spaces, rows

    # Remove the vehicle from the specified space
    vehicle = spaces[(int(row) * space_count) + int(space)].remove_vehicle()

    # Check if there was a vehicle in the specified space
    if vehicle is None:
        # Print an error message
        print("Error: No vehicle in specified space.")
        # Prompt the user to return to the menu
        input("\n*Press Enter to Return to Menu")
        return

    # Get the current time
    vehicle_exit_time = time.time()

    # Calculate the duration of the vehicle's stay in the parking lot
    time_spent = vehicle_exit_time - vehicle.get_entry_time()
    # Convert the duration to a string in the HH:MM:SS format
    time_spent_str = time.strftime("%H:%M:%S", time.gmtime(time_spent))

    # Log the vehicle's details
    log_vehicle_details(vehicle, vehicle_exit_time)
    
    # Increment the number of available spaces
    avail_spaces += 1

    # Display the parking lot
    display_lot()
    # Print a success message
    print("Vehicle Removed!")
    print("Time spent in parking lot: " + time_spent_str)
    # Print the fare for the vehicle
    print("Cost: $"+ "{:.2f}".format(fare_calculation(vehicle)))
    input("\n*Press Enter to Return to Menu")


def view_vehicle(row, space):
    # Check if the space is available
    if not spaces[(int(row) * space_count) + int(space)].is_available():
        display_space_selection(row)
        print("Error: No Vehicle In Space")
        input("\n*Press Enter to Return to Menu")
    else:
        # Get the vehicle information from the space
        vehicle = spaces[(int(row) * space_count) + int(space)].vehicle_info()
        display_space_selection(row)
        # Display the vehicle information
        input("Vehicle Type: " + vehicle.get_type_string() + "\n"
                                                             "Plate Number: " + vehicle.get_plate() + "\n"
                                                                                                      "Entry Time: " + str(
            time.strftime('%m-%d-%Y %I:%M %p',
            time.localtime(vehicle.get_entry_time()))) + "\n"
                                       "\n*Press Enter to Return to Menu")


def command_handler(command):
    # Check the command
    if command == "1":
        # Keep asking for vehicle type until a valid type is entered
        while True:
            # Display the parking lot
            display_lot()
            # Prompt the user to enter the vehicle type
            new_type = input("Enter Vehicle Type:\n"
                             "1. Car\n"
                             "2. Truck\n"
                             "3. Motorcycle\n"
                             "   > ")
            # Check if the entered type is valid
            if new_type == "1" or new_type == "2" or new_type == "3":
                break

        # Display the parking lot
        display_lot()
        # Prompt the user to enter the vehicle's plate number
        new_plate = input("Enter New Vehicle Plate Number:\n"
                          "   > ")

        # Set the return value to -1
        ret_val = -1
        # Keep asking for row and space until a valid one is entered
        while ret_val == -1:
            # Keep asking for a row until a valid one is entered
            while True:
                # Display the row selection menu
                display_row_selection()
                # Prompt the user to enter a row
                row = input("Select Row to Park In:\n"
                            "   > ")
                # Check if the entered row is valid
                if row.isnumeric():
                    if int(row) < rows:
                        break
                        # Keep asking for a space until a valid one is entered
            while True:
                # Display the space selection menu for the selected row
                display_space_selection(row)
                # Prompt the user to enter a space
                space = input("Select Space to Park In:\n"
                              "   > ")
                # Check if the entered space is valid
                if space.isnumeric():
                    if int(space) < space_count:
                        break
            # Try to enter the vehicle in the selected space
            ret_val = enter_vehicle(int(new_type), new_plate, row, space)
    
    # Check if the command is "2" (exit vehicle)
    elif command == "2":
        try:
            # Keep asking for a row until a valid one is entered
            while True:
                # Display the row selection menu
                display_row_selection()
                # Prompt the user to enter a row
                row = input("Select Row of Vehicle:\n"
                            "   > ")
                # Check if the entered row is valid
                if row.isnumeric():
                    if int(row) < rows:
                        break

            # Keep asking for a space until a valid one is entered
            while True:
                # Display the space selection menu for the selected row
                display_space_selection(row)
                # Prompt the user to enter a space
                space = input("Select Space of Vehicle:\n"
                            "   > ")
                    # Check if the entered space is valid
                if space.isnumeric():
                    if int(space) < space_count:
                        break
            # Try to remove the vehicle from the selected space
            exit_lot(row, space)
           except:
            print("Lot is empty!")
    
    # Check if the command is "3" (view vehicle)
    elif command == "3":
        # Check if there are any parked vehicles
        if avail_spaces != total_spaces:
            # Keep asking for a row until a valid one is entered
            while True:
                # Display the row selection menu
                display_row_selection()
                # Prompt the user to enter a row
                row = input("Select Row to View:\n"
                            "   > ")
                # Check if the entered row is valid
                if row.isnumeric():
                    if int(row) < rows:
                        break

            # Keep asking for a space until a valid one is entered
            while True:
                # Display the space selection menu for the selected row
                display_space_selection(row)
                # Prompt the user to enter a space
                space = input("Select Space to View:\n"
                              "   > ")
                # Check if the entered space is valid
                if space.isnumeric():
                    if int(space) < space_count:
                        break
            # View the vehicle in the selected space
            view_vehicle(row, space)

        # If there are no parked vehicles
        else:
            # Inform the user
            print("There are currently no Parked Vehicles.")
            # Display the parking lot
            display_lot()
    
    # Check if the command is "4" (display rates)
    elif command == "4":
        # Display the parking lot
        display_lot()
        # Display the current parking rates
        input("Current Parking Rates:\n"
              "Cars - $20.00 first hour + $20.00/additional hour\n"
              "Trucks - $30.00 first hour + $10.00/additional hour\n"
              "Motorcycles - $10.00 first hour + $10.00/additional hour\n"
              "\n*Press Enter to Return to menu")
    
    # Check if the command is "5" (enter demo mode)
    elif command == "5":
        # Enter demo mode
        demo_mode()

    # Check if the command is "0" (exit program)
    elif command == "0":
        # Exit the program
        return
    
    # If the entered command is invalid
    else:
        # Display the parking lot
        display_lot()
        # Inform the user
        print("Error: Invalid Command")
        # Prompt the user to return to the menu
        input("\n*Press Enter to Return to Menu")
       

def read_config():
    # Set global variables
    global spaces, total_spaces, avail_spaces, rows, linux, space_count, border

    # Open the config file for reading
    config = open('config.txt', 'r')

    # Read each line of the file
    while True:
        line = config.readline()

        # Check for the "total_spaces" keyword
        if line.find("total_spaces") != -1:
            # Set the "total_spaces" variable to the value specified on this line
            total_spaces = int(line[13:16])
            # Set the "avail_spaces" variable to the same value
            avail_spaces = total_spaces

        # Check for the "rows" keyword
        elif line.find("rows") != -1:
            # Set the "rows" variable to the value specified on this line
            rows = int(line[5:7])

        # Check for the "linux" keyword
        elif line.find("linux") != -1:
            # Set the "linux" variable to the value specified on this line
            linux = int(line[6:7])

        # Check for the "demo_mode" keyword
        elif line.find("demo_mode") != -1:
            # If the value is not "1", call the "demo_mode()" function
            if int(line[10:11]) != 1:
                demo_mode()
                break
            # If the value is "1", set up the parking lot
            else:
                # Create "Space" objects and append them to the "spaces" list
                for i in range(total_spaces):
                    spaces.append(Space())
                # Calculate the "space_count" by dividing "total_spaces" by "rows"
                space_count = int(total_spaces / rows)
                # Set the "border" variable to a string containing the border for the parking lot display
                border = "|"
                for i in range(space_count - 1):
                    for j in range(4):
                        border += "-"
                border += "---|\n"
                break

    # Close the config file
    config.close()
 

def demo_mode():
    # Set global variables
    global spaces, total_spaces, avail_spaces, rows, space_count, border

    # Create "Space" objects and append them to the "spaces" list
    for i in range(total_spaces):
        spaces.append(Space())

    # Set the "total_spaces" and "avail_spaces" variables to predefined values
    total_spaces = 20
    avail_spaces = 20
    # Set the "rows" variable to a predefined value
    rows = 4
    # Calculate the "space_count" by dividing "total_spaces" by "rows"
    space_count = int(total_spaces / rows)
    # Set the "border" variable to a string containing the border for the parking lot display
    border = "|"
    for i in range(space_count - 1):
        for j in range(4):
            border += "-"
    border += "---|\n"

    # Create some "Vehicle" objects and park them in the parking lot
    v1 = enter_vehicle(1, "aaa-bbbb", 0, 3)
    v2 = enter_vehicle(3, "ccc-dddd", 1, 2)
    v3 = enter_vehicle(2, "eee-ffff", 2, 0)
    v4 = enter_vehicle(1, "ggg-hhhh", 3, 1)
    v5 = enter_vehicle(2, "iii-jjjj", 2, 4)

    # Set the entry time of each vehicle to a predefined value
    v1.set_entry_time(1620561600)
    v2.set_entry_time(1620570600)
    v3.set_entry_time(1620577800)
    v4.set_entry_time(1620576000)
    v5.set_entry_time(1620586800)
