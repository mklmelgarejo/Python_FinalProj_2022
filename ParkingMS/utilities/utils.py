import io
import math
import os
import sys
import time
import json
import datetime

from classes.vehicle_info import Vehicle
from classes.space import Space
from classes.children.car_sub_v import Car
from classes.children.motorcycle_sub_v import Motorcycle
from classes.children.truck_sub_v import Truck

spaces = []
avail_spaces = 0
total_spaces = 0
rows = 0

space_count = 0
border = ""

linux = 0


def print_row(row):
    output = ""
    output += "|"
    for s in range(space_count * row, space_count * (row + 1)):
        if not spaces[s].is_available():
            output += "[ ]"
        else:
            output += "["
            output += "c" if spaces[s].vehicle_info().get_type() == 1 \
                else "t" if spaces[s].vehicle_info().get_type() == 2 \
                else "m"
            output += "]"
        if s < space_count * (row + 1) - 1:
            output += " "
    output += "|"

    return output


def display_lot():
    global spaces, avail_spaces, total_spaces, rows
    
    output = "\nSPOTS AVAILABLE: " + str(avail_spaces) + "\n"

    output += border
    for row in range(rows):
        output += print_row(row) + "\n"
    output += border
   
    if linux == 1:
        os.system("clear")
    print(output)


def display_row_selection():
    global spaces, avail_spaces, total_spaces, rows
    
    output = "\nSPOTS AVAILABLE: " + str(avail_spaces) + "\n"

    output += border
    for row in range(rows):
        output += print_row(row)
        output += " <" + str(row) + ">\n"
    output += border
    
    if linux == 1:
        os.system("clear")
    print(output)


def display_space_selection(row):
    global spaces, avail_spaces, total_spaces, rows

    output = "\nVIEWING ROW: " + row + "\n"

    output += border
    output += print_row(int(row)) + "\n"

    output += " "
    for count in range(space_count):
        if count < 10:
            output += "<" + str(count) + "> "
        else:
            output += "<" + str(count) + ">"

    output += "\n"
    output += border

    if linux == 1:
        os.system("clear")
    print(output)

    return space_count


def enter_vehicle(v_type, plate, row, space):
    global spaces, avail_spaces, total_spaces, rows
    
    if avail_spaces == 0:
        display_lot()
        print("Error: No Available Spaces")
        input("\n*Press Enter to Return to Menu")
        return
    
    if spaces[(int(row) * space_count) + int(space)].is_available():
        display_space_selection(row)
        print("Error: Vehicle Already In Space")
        input("\n*Press Enter to Pick New Space")
        return -1
    
    for uniq in spaces:
        if uniq.is_available():
            if uniq.vehicle_info().get_plate() == plate:
                display_lot()
                print("Error: Vehicle Already In Lot")
                input("\n*Press Enter to Park New Vehicle")
                return

    new_vehicle = Vehicle(v_type, plate)
    spaces[(int(row) * space_count) + int(space)].add_vehicle(new_vehicle)
    avail_spaces -= 1
    display_lot()
    print("Vehicle Added to Lot!\n"
          "Time Entered: " + str(time.strftime('%I:%M %p',
                                               time.localtime(new_vehicle.get_entry_time())))
                                               +"\n")
    input("\n*Press Enter to Return to Menu")

    log_vehicle_details(new_vehicle,0)

    return new_vehicle


def fare_calculation(vehicle):
    if vehicle.get_type() == 1:
        return Car(vehicle.get_plate()).compute_fare()
    elif vehicle.get_type() == 2:
        return Truck(vehicle.get_plate(), vehicle.get_weight()).compute_fare()
    elif vehicle.get_type() == 3:
        return Motorcycle(vehicle.get_plate()).compute_fare()



def log_vehicle_details(vehicle, exit_time):
    entry_time = vehicle.get_entry_time()
    time_spent = datetime.timedelta(seconds=(exit_time - entry_time))
    if time_spent.days < 0:
        time_spent = 0
    vehicle_cost = vehicle.compute_fare()

    with open('vehicle_log.json', 'a') as file:
        vehicle_data = {
            'vehicle_type': vehicle.get_type_string(),
            'license_plate': vehicle.get_plate(),
            'entry_time': time.strftime('%m/%d/%Y %I:%M %p', time.localtime(entry_time)),
            'exit_time': time.strftime('%m/%d/%Y %I:%M %p', time.localtime(exit_time)),
            'time_spent': str(time_spent),
            'vehicle_cost': vehicle_cost
        }
        json.dump(vehicle_data, file)
        file.write('\n')

def exit_lot(row, space):
    global spaces, avail_spaces, total_spaces, rows

    vehicle = spaces[(int(row) * space_count) + int(space)].remove_vehicle()
    if vehicle is None:
        print("Error: No vehicle in specified space.")
        input("\n*Press Enter to Return to Menu")
        return

    vehicle_exit_time = time.time()

    time_spent = vehicle_exit_time - vehicle.get_entry_time()
    time_spent_str = time.strftime("%H:%M:%S", time.gmtime(time_spent))

    log_vehicle_details(vehicle, vehicle_exit_time)
    
    avail_spaces += 1

    display_lot()
    print("Vehicle Removed!")
    print("Time spent in parking lot: " + time_spent_str)
    print("Cost: $"+ "{:.2f}".format(fare_calculation(vehicle)))
    input("\n*Press Enter to Return to Menu")


def view_vehicle(row, space):
    
    if not spaces[(int(row) * space_count) + int(space)].is_available():
        display_space_selection(row)
        print("Error: No Vehicle In Space")
        input("\n*Press Enter to Return to Menu")
    
    else:
        vehicle = spaces[(int(row) * space_count) + int(space)].vehicle_info()
        display_space_selection(row)
        input("Vehicle Type: " + vehicle.get_type_string() + "\n"
                                                             "Plate Number: " + vehicle.get_plate() + "\n"
                                                                                                      "Entry Time: " + str(
            time.strftime('%m-%d-%Y %I:%M %p',
                          time.localtime(vehicle.get_entry_time()))) + "\n"
                                                                       "\n*Press Enter to Return to Menu")


def command_handler(command):
    
    if command == "1":
        while True:
            display_lot()
            new_type = input("Enter Vehicle Type:\n"
                             "1. Car\n"
                             "2. Truck\n"
                             "3. Motorcycle\n"
                             "   > ")
            if new_type == "1" or new_type == "2" or new_type == "3":
                break
        
        display_lot()
        new_plate = input("Enter New Vehicle Plate Number:\n"
                          "   > ")
        
        ret_val = -1
        while ret_val == -1:
            while True:
                display_row_selection()
                row = input("Select Row to Park In:\n"
                            "   > ")
                if row.isnumeric():
                    if int(row) < rows:
                        break
            while True:
                display_space_selection(row)
                space = input("Select Space to Park In:\n"
                              "   > ")
                if space.isnumeric():
                    if int(space) < space_count:
                        break
            ret_val = enter_vehicle(int(new_type), new_plate, row, space)
    
    elif command == "2":
        
        while True:
            display_row_selection()
            row = input("Select Row of Vehicle:\n"
                        "   > ")
            if row.isnumeric():
                if int(row) < rows:
                    break

        while True:
            display_space_selection(row)
            space = input("Select Space of Vehicle:\n"
                          "   > ")
            if space.isnumeric():
                if int(space) < space_count:
                    break
        exit_lot(row, space)
    
    elif command == "3":

        if avail_spaces != total_spaces:

            while True:
                display_row_selection()
                row = input("Select Row to View:\n"
                            "   > ")
                if row.isnumeric():
                    if int(row) < rows:
                        break

            while True:
                display_space_selection(row)
                space = input("Select Space to View:\n"
                              "   > ")
                if space.isnumeric():
                    if int(space) < space_count:
                        break
            view_vehicle(row, space)

        else:
            print("There are currently no Parked Vehicles.")
            display_lot()
    
    elif command == "4":
        display_lot()
        input("Current Parking Rates:\n"
              "Cars - $20.00 first hour + $10.00/additional hour\n"
              "Trucks - $30.00 first hour + $10.00/additional hour\n"
              "Motorcycles - $10.00 first hour + $10.00/additional hour\n"
              "\n*Press Enter to Return to menu")
    
    elif command == "5":
        demo_mode()

    elif command == "0":
        return
    
    else:
        display_lot()
        print("Error: Invalid Command")
        input("\n*Press Enter to Return to Menu")
        



def read_config():
    global spaces, total_spaces, avail_spaces, rows, linux, space_count, border

    config = open('config.txt', 'r')
    while True:
        line = config.readline()

        if line.find("total_spaces") != -1:
            total_spaces = int(line[13:16])
            avail_spaces = total_spaces

        elif line.find("rows") != -1:
            rows = int(line[5:7])
        
        elif line.find("linux") != -1:
            linux = int(line[6:7])

        elif line.find("demo_mode") != -1:
            if int(line[10:11]) != 1:
                demo_mode()
                break
            else:
                for i in range(total_spaces):
                    spaces.append(Space())
              
                space_count = int(total_spaces / rows)
                
                border = "|"
                for i in range(space_count - 1):
                    for j in range(4):
                        border += "-"
                border += "---|\n"
                break

    config.close()


def demo_mode():
    global spaces, total_spaces, avail_spaces, rows, space_count, border

    for i in range(total_spaces):
        spaces.append(Space())

    total_spaces = 20
    avail_spaces = 20
    rows = 4
    
    space_count = int(total_spaces / rows)
   
    border = "|"
    for i in range(space_count - 1):
        for j in range(4):
            border += "-"
    border += "---|\n"

    v1 = enter_vehicle(1, "aaa-bbbb", 0, 3)
    v2 = enter_vehicle(3, "ccc-dddd", 1, 2)
    v3 = enter_vehicle(2, "eee-ffff", 2, 0)
    v4 = enter_vehicle(1, "ggg-hhhh", 3, 1)
    v5 = enter_vehicle(2, "iii-jjjj", 2, 4)
   
    v1.set_entry_time(1620561600)
    v2.set_entry_time(1620570600)
    v3.set_entry_time(1620577800)
    v4.set_entry_time(1620576000)
    v5.set_entry_time(1620586800)