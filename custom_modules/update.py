'''
All the updation functions for code

Function defined below :-

    update()
    update_data()
    
    --------------------------

'''

import csv
import time

def update(id,a):

    '''
        The update(id,a) function takes two arguments: id and a. The function opens a CSV file 
        called emp_details.csv in read mode and reads its contents into a list of lists. The 
        function then searches the list for a row with an ID that matches the id argument. If a 
        matching row is found, the function prompts the user to enter new values for one or more 
        fields of the record. The function then updates the appropriate fields of the record and 
        sets a flag called found to 1. The function then appends the updated record to a new list 
        called ml. If no matching row is found, the function sets found to 0.
        
        Finally, if found is 0, the function prints a message indicating that no data was found. 
        If found is 1, the function opens the CSV file in write mode and writes all of the rows in 
        ml to the file. The function then closes the file.
        
    '''

    # open the csv file as read mode 
    f=open("emp_details.csv",'r')

    # set the found veriable for 0
    found=0


    csvr=csv.reader(f)

    # we create an empty list
    ml=[]
    for r in csvr:
        if(r[0]==id):
            if a==1:
                r[1]=input("Enter the new name of the Employee  :")
            if a==2:
                r[2]=input("Enter the new designation of the Employee  :")
            if a==3:
                r[3]=input("Enter the new salary of the Employee  :")
            if a==4:
                r[4]=input("Enter the new age of the Employee  :")
            if a==5:
                r[6]=input("Enter the new Email id of the Employee  :")
            if a==6:
                r[7]=input("Enter the new Phone no. of the Employee  :")

            found=1

        # we append all the updated row in the list
        ml.append(r)


    if found==0:
        print("No data Found!!!!")

    else:

        # here we open the csv file in write mode
        f=open("emp_details.csv","w",newline="")
        csvr=csv.writer(f)

        # write all the rows
        csvr.writerows(ml)

        # close the 
        f.close()



# ************************* Main function **************************************

def update_data():

    '''
        The update_data() function takes no arguments and is used to update the data of an employee.
        
        The function prompts the user to enter the ID of the employee whose data they want to update. 
        It then enters a while loop that displays a menu of options for updating the employee’s data. 
        The user is prompted to enter their choice of what they want to update. The function then calls 
        another function named update() with the ID of the employee and the choice made by the user as arguments.
        
        After updating the data, the function prompts the user if they want to update anything else. If yes, 
        it continues with the loop, otherwise it breaks out of it.
        
        Finally, it prints a message indicating that the data has been updated successfully.
        
        Unfortunately, I don’t have enough context to determine what update() function does. If you 
        could provide more information about it, I would be happy to help you further.

    '''


    # Enter the id of the columns whose data you want to update
    id=input("Enter the ID of the Employee : ")



    while 1:

        print("1. Update Name ")
        print("2. Update Designation")
        print("3. Update Salary")
        print("4. Update Age")
        print("5. Update Email")
        print("6. Update Phone No. ")

        # enter the choice we want to update 
        a=int(input("Enter your choice :  "))

        # here we give the EMp_id and the choice to the update function 
        update(id,a)

        # if you want to update other columns then enter y and if you don't want to update other things then enter n
        x=input("Do you want update anything (y/n) : ")


        if x=='y':
            pass

        if x=='n':
            break

    #end of updation 
    print("\n\nData has been updated successfully!")
    time.sleep(2)
