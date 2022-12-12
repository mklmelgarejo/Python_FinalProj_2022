from utilities.utils import command_handler, display_lot, read_config


def main():
   
    read_config()
   
    command = ""
    while command != "0":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        display_lot()
        print(#"\nSPOTS AVAILABLE: " + str(avail_spaces) +
              "Please Select An Option:\n"
              "1 - Park a Vehicle\n"
              "2 - Exit the Lot\n"
              "3 - View a Parked Vehicle\n"
              "4 - Display Vehicle Rates\n"
              "5 - Run Demo\n"
              "0 - Quit Application")

        command = input("   > ")
        command_handler(command)


if __name__ == '__main__':
    main()
