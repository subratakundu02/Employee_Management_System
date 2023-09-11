'''
Contains UI of the Employee management system and function calls of different modules

    EmpId | Name | Age | Gender | Designation | Salary | Email | Phno
    _________________________________________________________________
          |      |     |        |             |        |       |


UserID :- admin 
Password :- BCREC

'''

# import custom_modules
import os
import time
import msvcrt # only exclusive for windows users
from custom_modules import newentry as NE
from custom_modules import printdata as PD
from custom_modules import update as UP
from custom_modules import password as PW
from custom_modules import deletedata as DD


banner = r'''
        ╔═╗╔╦╗╔═╗╦  ╔═╗╦ ╦╔═╗╔═╗      ╔╦╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╔═╗╔╗╔╔╦╗      ╔═╗╦ ╦╔═╗╔╦╗╔═╗╔╦╗
        ║╣ ║║║╠═╝║  ║ ║╚╦╝║╣ ║╣       ║║║╠═╣║║║╠═╣║ ╦║╣ ║║║║╣ ║║║ ║       ╚═╗╚╦╝╚═╗ ║ ║╣ ║║║
        ╚═╝╩ ╩╩  ╩═╝╚═╝ ╩ ╚═╝╚═╝      ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╝╚╝ ╩       ╚═╝ ╩ ╚═╝ ╩ ╚═╝╩ ╩
'''

# Hiding password entry on screen
def custom_input(prompt):
    print(prompt, end="", flush=True)
    input_string = ""
    while True:
        char = msvcrt.getch().decode('utf-8')  # Get a single character without printing it
        if char == '\r' or char == '\n':
            print("")  # Print a newline when Enter is pressed
            break
        elif char == '\b':
            if input_string:
                input_string = input_string[:-1]  # Remove the last character
                print("\b \b", end="", flush=True)  # Clear the last character on the screen
        else:
            input_string += char
            print("*", end="", flush=True)  # Print an asterisk for each character
    return input_string


def main():
    while 1 :

        print(banner)

        print("<<"*50 + "\n\n")
        print("\t\t1. Enter new employee data")
        print("\t\t2. Update existing data")
        print("\t\t3. View data")
        print("\t\t4. Delete data")
        print("\t\t5. Exit")
        print("\n\n" + ">>"*50)

        inp = input("Enter choice : ")

        # ***************************** Insert record ***************************** 
        if inp == "1":
            # call the function in dataentry.py
            NE.add_new_data()
        # ***************************** Update record ***************************** 
        elif inp == "2":
            # call the function in update.py
            UP.update_data()
        # ***************************** Viewing data ***************************** 
        elif inp == "3":
            print("Search by category :-")
            print("1. EmpId") # generates unique output(only 1)
            print("2. Name") # may generate 1 or more based on pattern matching
            print("3. Age")
            print("4. Gender")
            print("5. Designation")
            # no searching on salary or email or phone(personal details can't be used to search)

            # ========================== Criteria selection for Viewing data ==========================
            inp = None
            allowedval = ["1","2","3","4","5","6"]
            while inp not in allowedval:
                inp = input("Select criteria to search data : ")
                if inp not in allowedval:
                    print("Incorrect Selection!!!Try again.")

            # ========================== Admin privilege for viewing personal data ==========================
            adminprivilege = None
            allowedval = ['y','n','Y','N']
            while adminprivilege not in allowedval :
                adminprivilege = input("View Employee mail and phone(y/n) : ")
                if adminprivilege not in allowedval:
                    print("Incorrect Input!!! Please try again.")

            if adminprivilege == 'y':
                # call the secret passcode and catcha functions
                if PW.demand_password():
                    print("\n\nAdmin Privileges granted!!!\n\n")
                else:
                    adminprivilege = 'n'
                    print("\n\nSorry!!! Cannot grant admin privileges\n\n")

            # Finally call the print function 
            PD.printdata(inp, adminprivilege)

            tmp = input("\n\n\nPress Enter to exit...")

        # ***************************** Delete data code **********************

        elif inp=="4":
            # first verify as admin then delete as per userID provided
            DD.delete_data()

        # ***************************** Exit code *****************************
        elif inp=="5":
            break
        # ***************************** Incorrect selection *****************************
        else:
            print("Invalid Choice!!!\n\n Refreshing Page")

        # ~~~~~~~~~~~ REFRESH PAGE ~~~~~~~~~~~~~
        os.system("cls")
    # if someone exits loop breaks then function returns to caller
    return

# dictonary of the userid and password (admin,manager,employee)
users = {'admin': 'BCREC', 'manager': 'BCREC1', 'employee': 'BCREC2'}

if __name__ == "__main__":

    print(banner)

    print("<<"*50 + "\n\n")

    tries_left=3

    while tries_left:

        # give the user input for userid and password
        userid=input("Enter admin UserID : ")
        password=custom_input("Enter admin password: ")

        # If the user id and password is correct then it will call delete function to delete the Column
        if userid in users and users[userid] == password: 
            print("Permission Granted!!!!!")
            print("Login successful!")
            time.sleep(2)

            os.system("cls")
            # Here we call the main function.
            # ***************** MAIN FUNCTION *****************
            main()

            time.sleep(2)
            break

        # the next three if condition for either wrong userid or wrong password

        else:
            print("Invalid username or password. Please try again.") 
        # here we decrease the tries_left variable
        tries_left-=1
        print("Tries left : ",tries_left)

    
    if tries_left==0:
        time.sleep(2)
        
        print("\n\nSorry you gave wrong userid and password thrice. So application access denied!") 
    # End of session
    time.sleep(2)
    print("\n"*5 + "~"*50 + "\nProgram Terminated. Changes Saved!\n"+ "~"*50)
