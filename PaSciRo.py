#
# Author : Ibrahim Malik
# ID : 20207593
#
# COMP1005 - Fundamentals of Programming
#
# PaSciRo.py - Main code to run program
# PaSciRo_Classes.py - Imported file containing classes and functions
#
# Revisions: 
#
# 01/10/2020 – Base version for assignment
# 25/10/2020 - Final version of assignment
#
import time
from PaSciRo_Classes import *

#   Introductory Phrases
print("Welcome to Planet PaSciRo!\n")
time.sleep(1)                                
print("Preparing Planet for simulation...\n")
time.sleep(2)
print("Initiation --- Successful\n")
time.sleep(1)

#   Main program function
def main():
    
    #   Defining Limits for x-axis and y-axis
    XMAX = 200
    YMAX = 100
    
    #   Input for POP value and ensuring it is an integer between 4 and 1000
    while True:
        POP = input("\nEnter the total population of the lifeforms:\n")
        try:
            val = int(POP)
            POP = int(POP)
            while POP < 5 or POP > 1000:
                if POP < 5:
                    print("Population level too low. Please re-enter.")
                if POP > 1000:
                    print("Population level too high. Please re-enter.")
                POP2 = int(input())
                POP = POP2 
            break;
        except ValueError:
            print("'", POP, "'", "is not a valid population size, please try again!")
    
    #   Expanding ranges for x-axis and y-axis depending on POP size
    if POP > 500:
        XMAX = XMAX + 200
        YMAX = YMAX + 200
    elif POP > 200:
        XMAX = XMAX + 100
        YMAX = YMAX + 100
    
    time.sleep(1)
    
    #   Input for Time STEPS value and ensuring it is an integer between 3 and 100
    while True:
        STEPS = input("Enter the amount of time steps the population would advance:\n")
        try:
            val = int(STEPS)
            STEPS = int(STEPS)
            while STEPS < 3 or STEPS > 100:
                if STEPS < 3:
                    print("STEP level too low. Please re-enter.")
                if STEPS > 100:
                    print("STEP level too high. Please re-enter.")
                STEPS2 = int(input())
                STEPS = STEPS2
            break;
        except ValueError:
            print("'", STEPS, "'", "is not a valid time step amount, please try again!")
    
    #   Time interval between each Time STEP
    STEPS_TIME = 0.75

    time.sleep(1)

    #   Input for saving each Time STEP and ensuring input value is "Y" or "N"
    figs = input("Do you want to save each Time-Step [y/n]: ")
    figs = figs.upper()
    while figs not in ("Y", "N"):
        figs = input("Invalid Entry. Try Again: ")
        figs = figs.upper()
    
    #   Input for method of saving and ensuring input is "A" or "B" or "C" or "D"
    if figs == "Y":
        time.sleep(1)
        print("\nHow would you like to save your file?")
        print("A - PDF File")
        print("B - Images")
        print("C - CSV File")
        print("ABC - PDF File, Images and CSV File")
        print("D - None")
        
        save = input("Choice: ")
        save = save.upper()
        while save not in ("A", "B", "C", "D", "ABC"):
            save = input("Invalid Entry. Try Again: ")
            save = save.upper()
    else:
        save = "D"
    
    time.sleep(1)
    
    #   Menu to select planet operation
    print("\nPaSciRo")
    time.sleep(1)
    print("Choose from the following: ")
    print("S - Simulate planet")
    print("W - Simulate war between lifeforms")
    print("R - Simulate reproduction between lifeforms")
    print("I - Simulate presence of intruders")
    print("E - Exit")
    
    #   Input for operation and ensuring input is "S" or "W" or "R" or "I" or "E"
    option=input("Choice: ")
    option=option.upper()
    while option not in ("S", "W", "R", "I", "E"):
        option = input("Invalid Option. Please select an option from the menu: ")
        option = option.upper()
    
    time.sleep(1)
    
    #   Selecting imported function based on planet operation
    if option == 'S':
        simulate(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save)
    elif option == 'W':
        if __name__ == "__main__":
            war(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save)
    elif option == 'R':
        if __name__ == "__main__":
            reproduce(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save)
    elif option == 'I':
        if __name__ == "__main__":
            intruderz(POP, XMAX, YMAX, STEPS, STEPS_TIME, figs, save)
    elif option == "E":
        print("Exiting...")
        time.sleep(1)
    
    #   Input if another simulation is required
    if option != "E":
        choice = input("Would you like to do another simulation [y/n]: ")
        choice = choice.upper()
        while choice not in ("Y", "N"):
            choice = input("Invalid Entry. Try Again: ")
            choice = choice.upper()
    
        #   Repeat or Exit based on choice
        if choice == 'Y':
            #   Repeat function
            if __name__ == "__main__":
                main()
        else:
            #   Outroductory Phrases
            print("\nLeaving Planet...")
            time.sleep(2)
            print("\nGoodbye!\n")
            time.sleep(1)
            
    else:
        #   Outroductory Phrases
        print("\nLeaving Planet...")
        time.sleep(2)
        print("\nGoodbye!\n")
        time.sleep(1)

#   Where the program starts
if __name__ == "__main__":
    main()
