# Import the command_handler, display_lot, and read_config functions from the utilities.utils module
from utilities.utils import command_handler, display_lot, read_config


def main():
    # Read the configuration data from the config.txt file
    read_config()

    # Initialize the command variable
    command = ""

    # Run the loop until the user inputs the command to quit the application
    while command != "0":
        # Clear the screen
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # Display the current status of the parking lot
        display_lot()

        # Print the options the user can choose from
        print(#"\nSPOTS AVAILABLE: " + str(avail_spaces) +  # <-- This line is commented out
              "Please Select An Option:\n"
              "1 - Park a Vehicle\n"
              "2 - Exit the Lot\n"
              "3 - View a Parked Vehicle\n"
              "4 - Display Vehicle Rates\n"
              "5 - Run Demo\n"
              "0 - Quit Application")

        # Prompt the user to input a command
        command = input("   > ")

        # Handle the user's input
        command_handler(command)


if __name__ == '__main__':
    # Run the main function
    main()
