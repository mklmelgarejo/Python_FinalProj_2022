# Parking Management System
A console application written in Python programming language. This system will help you manage a parking lot. You can easily identify if there is still available space for a vehicle. It also contributes on computing how much will a vehicle will pay.


# Features
1. Park a Vehicle

2. Exit the Lot

3. View a Parked Vehicle

4. Display Vehicle Rates

5. Run Demo

## Dependencies

 - All codes are written in Python 3.
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
|      File Name  |Description|
|-----------------|-------------------------------|
|`README.md`   	  |Text file, description of the project            |
|`vehicle_log.json` |JSON file, used as database for vehicle logs            |
|`config.txt`       |Text file, used as configuration of parking space

Python files:
|     File Name  |Description|
|----------------|-------------------------------------------------------------|
|`index.py`   	 |Displays the options the user can choose from.         	   |
|`utils.py` 	 	|Controls the choice what user selected in the choices. 	   |
|`vehicle_info.py` |Gets the information about the vehicle				 	   |
|`car.py`			 |Computes the fare if the vehicle type is car				   |
|`motorcycle.py`	 |Computes the fare if the vehicle type is motorcycle		   |
|`truck.py`		 |Computes the fare if the vehicle type is truck			   |
|`space.py`		 |Gives information about a space whether it is occupied or not|

## UML Diagram
![umldiagram](https://photos.app.goo.gl/5sTCvgHQ545c6qCZ7)

## Self Assessment
The group evaluated the system using the provided grading rubric, which resulted in the following:
|       			|4|3|2|1|
|-------------------|-|-|-|-|
|Code Reusability 	|✔| | | |
|Maintainability	|✔| | | |
|Scalability		|✔| | | |
|Execution		 	|✔| | | | 
|Originality	 	|✔| | | |
|Overall Impression	|✔| | | |
## Youtube Video Link
To watch out video, click [here]()

## Contributors

 - Mikaela Melgarejo
 - Rod Vincent Dilag

