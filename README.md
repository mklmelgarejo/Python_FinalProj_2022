# Parking Management System
A console application written in Python programming language. This system helps an employee manage a parking lot. It automatically displays parking vacancies and computes for the cost of using the parking space. 


# Features
1. Park a Vehicle
2. Exit the Lot
3. View a Parked Vehicle
4. Display Vehicle Rates
5. Run Demo


## Dependencies
 - All codes are written in `Python 3`.
 - Some codes depend on `os` module
	- `utils.py`  
 - Some codes depend on `time` module
	 - `utils,py`
	 - `vehicle_info.py`
	 - `space.py`
	 - `car.py`
	 - `motorcycle.py`
	 - `truck.py`
 - Some codes depend on `json` module
	 - `utils.py`
 - Some codes depend on datetime module
	 - `utils.py`
 - Some codes depend on math module
	 - `car.py`
	 - `motorcycle.py`
	 - `truck.py`

## Description of Files

Non-python files:
|     File Name     |Description                                       |
|-------------------|--------------------------------------------------|
|`README.md`   	    |Text file, description of the project             |
|`vehicle_log.json` |JSON file, used as database for vehicle logs      |
|`config.txt`       |Text file, used as configuration of parking space |

Python files:
|     File Name     |Description|
|-------------------|--------------------------------------------------------------|
|`index.py`   	    |Displays the options the user can choose from         	   |
|`utils.py` 	    |Controls the choice what user selected in the choices 	   |
|`vehicle_info.py`  |Gets the information about the vehicle			   | 
|`car.py`	    |Computes the fare if the vehicle type is "car"		   |
|`motorcycle.py`    |Computes the fare if the vehicle type is "motorcycle"	   |
|`truck.py`	    |Computes the fare if the vehicle type is "truck"		   |
|`space.py`	    |Gives information about a space whether it is occupied or not |

## UML Diagram
![318645114_5604183832984580_1063135367212618092_n](https://user-images.githubusercontent.com/114204913/206947287-c0c2de0f-5637-4392-99a6-a18a662cb04c.png)
    
The `index.py file` is the main entry point of the application. It imports the command_handler, 
display_lot, and read_config functions from the utilities.utils module and uses them to run 
the main loop of the application.

The `utilities.utils module` contains several utility functions that are used by the Main.py file 
to perform various tasks such as handling user input, displaying the parking lot, and logging 
vehicle information to a file.

The `classes.vehicle_info.Vehicle class` represents a vehicle in the parking lot. It contains 
information about the vehicle's type, license plate number, and entry time, as well as methods 
for computing the fare and accessing this information.

The `classes.space.Space class` represents a space in the parking lot. It has a Vehicle object 
that can be added to or removed from the space, and a Boolean value that indicates whether the 
space is currently occupied or not.

The `classes.vehicles.car.Car`, `classes.vehicles.motorcycle.Motorcycle`, and 
`classes.vehicles.truck.Truck` classes all inherit from the classes.vehicle_info.Vehicle class 
and add additional functionality specific to each type of vehicle. For example, the Car class 
has a compute_fare method that calculates the fare for a car based on the amount of time it has 
been parked.

Together, these classes and modules work to create a parking management system that 
allows users to park vehicles, view parked vehicles, and compute fares for each vehicle.


## Self Assessment
The group evaluated the system using the provided grading rubric, which resulted in the following:
|       		|4|3|2|1|
|-----------------------|-|-|-|-|
|Code Reusability 	|✔| | | |
|Maintainability	|✔| | | |
|Scalability		|✔| | | |
|Execution		|✔| | | | 
|Originality	 	|✔| | | |
|Overall Impression	|✔| | | |

## Youtube Video Link
To watch explanation, click [here](https://www.youtube.com/watch?v=uxXS-KZAYOI)

## Contributors

 - [Mikaela Melgarejo](https://github.com/mklmelgarejo)
 - [Rod Vincent Dilag](https://github.com/rdvncntdlg)

