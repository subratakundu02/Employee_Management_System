'''

Note :- need to install tabulate using pip install tabulate

We will first search for data using different search methods for different categories then view or print it on console

Function defined below :-

    print_data()
    --------------------------

'''

import time
import pandas as pd
from tabulate import tabulate
# reference dictionary used in code below, no search by salary, email or phone
Dict={
    '1':'Emp_Id',
    '2':'Name',
    '3':'Age',
    '4':'Gender',
    '5':'Designation',
}

#******************* PRINT FUNCTION *****************

def printdata(opt, privilege_granted):

    '''
        The printdata(opt, privilege_granted) function takes two arguments: opt and privilege_granted. 
        The function prompts the user to enter a search term for a specific field of an employee record. 
        The function then reads a CSV file called emp_details.csv into a pandas DataFrame. The function 
        creates two new DataFrames: one that contains all columns of the original DataFrame, and one that 
        contains all columns except for ‘Email’ and ‘Phno’. The function then filters the appropriate 
        DataFrame based on the search term entered by the user and whether or not the user has administrative 
        privileges. If there are any matching records, the function uses the tabulate library to format the 
        data as a table and prints it to the console. If there are no matching records, the function prints a 
        message indicating that no data was found.

    '''
    req = input("Enter the " + Dict[opt] + " of the Employee: ")
    data_for_admin_only = pd.read_csv('emp_details.csv')
    data_for_admin_only['Age'] = data_for_admin_only['Age'].astype(str)
    data_for_general_use = data_for_admin_only.loc[:, ~data_for_admin_only.columns.isin(['Email', 'Phno'])]

    if privilege_granted in ['y', 'Y']:
        filtered_data = data_for_admin_only[data_for_admin_only[Dict[opt]].str.contains(req, case=False, na=False)]
    else:
        filtered_data = data_for_general_use[data_for_general_use[Dict[opt]].str.contains(req, case=False, na=False)]

    if not filtered_data.empty:
        # Use the tabulate library for formatting
        print(tabulate(filtered_data, headers='keys', tablefmt='grid', showindex=False))
    else:
        print("No data found.")

