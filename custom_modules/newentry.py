"""
Writing into the emp_details.csv file stored within main folder

Functions defined below :-

    create_csv_if_not_exists()
    get_employee_ids()
    generate_new_id()
    gather_data()
    entry()
    --------------------------
    add_new_data()

====
TODO
====
    * Add email checker
    * Add mobile number checker
    * Add wrong gender checker
    * Add wrong data type checkers for each user enterable type

"""


import os
import csv
import time
import random


# ======================== CSV File creation ========================
def create_csv_if_not_exists():
    """
        This function "create_csv_if_not_exists()" checks if the file named emp_details.csv exists in the current directory.
        If the file does not exist, it creates a new file with that name and writes a header row to it. The header row
        contains the following fields:
        -> Emp_Id
        -> Name
        -> Designation,
        -> Salary
        -> Age
        -> Gender
        -> Email
        -> Phno.
        If the file already exists, the function prints a message indicating that the file already exists.
    """
    file_path = "./emp_details.csv"

    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as csvfile:
            header = [
                "Emp_Id",
                "Name",
                "Designation",
                "Salary",
                "Age",
                "Gender",
                "Email",
                "Phno",
            ]

            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()

        print("\n\nemp_details.csv file created.\n\n")

    else:
        print("\n\nemp_details.csv file already exists.\n\n")


# ======================== Obtain list of integer value of employee ids of all old employees ========================
def get_employee_ids():
    """
        This function reads the contents of a CSV file named emp_details.csv located in the current directory.
        If the file exists, it reads the Emp_Id column of each row and extracts the numeric portion of the string
        (excluding the first three characters) and appends it to a list called employee_ids. If the file does 
        not exist, it prints a message indicating that the file does not exist. Finally, it returns the list of employee IDs.
    
    """
    file_path = "./emp_details.csv"
    employee_ids = []

    if os.path.exists(file_path):
        with open(file_path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee_ids.append(int(row["Emp_Id"][3:]))
    else:
        # this will never hit for sure, yet kept for clarity
        print("emp_details.csv file does not exist.")

    return employee_ids


# ======================== Generate new unique ID for employee ========================
def generate_new_id():
    # search for the existence of all old ids and truncate "EID" from them
    """
        We are sure that csv file exists since we created it if not. Now we just want all employee IDs out of it
        They will be of the format `EIDxxxxxx` , we need only the `xxxxxx` so we need to remove EID by slicing
        Then generate a random number which does not exist in list
    """
    existing_ids = get_employee_ids()

    # generate a 6 digit random number which does not match any old id
    while True:
        new_id = random.randint(100000, 999999)
        if new_id not in existing_ids:
            break

    # final id generated
    print("Generating new Employee ID\n")
    time.sleep(1)
    new_id = "EID" + str(new_id)
    return new_id


# ======================== Gather data ========================
def gather_data():

    '''
        This function prompts the user to enter various details about an employee, including their name,
        designation, salary, age, gender, email, and phone number. It then generates a new employee ID 
        using the generate_new_id() function and displays it to the user. The ID is automatically 
        deleted after 5 seconds. Finally, the function returns a list containing the employee’s ID and 
        the details entered by the user.
    '''
    
    name = input("Enter the full name of Employee : ")
    pos = input("Enter the Designation of Employee : ")
    salary = float(input("Enter the monthly salary of the Employee(in Rs.) : "))
    age = int(input("Enter the age of Employee(in yrs.) : "))
    gender = input("Enter the gender of Employee(M/F/N) : ")  # N for non-binary
    email = input("Enter the Email-ID of the Employee : ")
    phone = int(input("Enter the Phone Number : "))
    # allocate a new employee ID to the employee
    newid = generate_new_id()
    print(
        "New Employee ID generated : ",
        newid,
        "\nPlease Note it down for future use(will be deleted automatically in 5s)\n\n",
    )
    time.sleep(5)

    return [newid, name, pos, salary, age, gender, email, phone]


# ======================== enter data in csv ========================
def entry(newid, name, pos, salary, age, gender, email, phone):
    '''
        This function takes in several parameters, including an employee ID, name, designation, salary, 
        age, gender, email, and phone number. It then opens a CSV file called emp_details.csv in append 
        mode and writes a new row to the file containing the information passed to the function. The 
        row contains the following fields: Emp_Id, Name, Designation, Salary, Age, Gender, Email, and Phno.
    '''
    with open("emp_details.csv", mode="a", newline="") as csvfile:
        header = [
            "Emp_Id",
            "Name",
            "Designation",
            "Salary",
            "Age",
            "Gender",
            "Email",
            "Phno",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=header)
        # final entry
        writer.writerow(
            {
                "Emp_Id": newid,
                "Name": name,
                "Designation": pos,
                "Salary": salary,
                "Age": age,
                "Gender": gender,
                "Email": email,
                "Phno": phone,
            }
        )


# ************************ ADDING NEW DATA ************************
def add_new_data():

    '''
        This function first checks if a file named emp_details.csv exists in the current directory. 
        If the file does not exist, it creates a new file with that name and writes a header row 
        to it. The header row contains the following fields: Emp_Id, Name, Designation, Salary, 
        Age, Gender, Email, and Phno. If the file already exists, the function does nothing.
        
        Next, the function prompts the user to enter various details about an employee, including 
        their name, designation, salary, age, gender, email, and phone number. It then generates 
        a new employee ID using the generate_new_id() function and displays it to the user. The 
        ID is automatically deleted after 5 seconds. Finally, the function writes a new row to 
        the CSV file containing the information entered by the user. The row contains the following 
        fields: Emp_Id, Name, Designation, Salary, Age, Gender, Email, and Phno.
    '''

    # check for existence of csv file where we need to append data
    create_csv_if_not_exists()

    # gather needed data from user
    data = gather_data()

    # enter the data into csv, note that data is unpacked before passing using *
    entry(*data)

    print(
        "\n\n" + "=" * 50 + "\n\nData entered into system successfully!\n\n" + "=" * 50
    )
    time.sleep(2)
