"""
Writing into the emp_details.csv file stored within main folder

Functions defined below :-

    
    delete_data()
    --------------------------


"""


import time
import pandas as pd

# user id and password


#****************** MAIN DELETE FUNCTION ********************
def delete_data():

    '''
        This function "delete_data()" reads a CSV file called emp_details.csv into a pandas DataFrame. 
        It then prompts the user to enter an employee ID to delete. If the DataFrame does not contain 
        any rows with the specified ID, the function prints an error message. If the DataFrame contains 
        one or more rows with the specified ID, the function removes those rows from the DataFrame and 
        saves the updated DataFrame back to the CSV file. Finally, the function prints a message 
        indicating that the employee was deleted successfully.

    '''
    # First we store the dataframe in df
    df=pd.read_csv('emp_details.csv')

    # then call the loop
    while 1:
        # user input for the Employee id
        id=input("Enter the ID of the Employee to delete : ")

        # if the dataframe shape is 0 ,then it will show the print function 
        if(df[df.Emp_Id==id].shape[0]==0):
            print("NO DATA FOUND !!!! Please enter valid Employee ID.")

        # If the dataframe shape is not 0.
        else:

            # first we drop the columns whose Emp_id match with the delete Emp_id
            df=df.drop(df[df.Emp_Id==id].index)

            # Then it load the dataframe to the csv file
            df.to_csv('emp_details.csv',index=False)

            print("\n\nDeleted Employee ID no. "+id+" Sucessfully.")
            time.sleep(2)
            break
