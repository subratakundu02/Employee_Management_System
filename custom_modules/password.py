'''
Simple password & captcha implementation

functions present :-
    user_entry()
    generate_captcha_img()
    captcha() --> returns a boolean value confirming if user passed the test or not
    ============
    demand_password() --> returns a boolean value

***Only 3 tries given to user for captcha and unlimited refresh given to user else  user FAILS test.
***Only 3 tries allowed and at the same time must pass the captcha test

====

* Hide the user entered password if possible later
'''

import random


# ========================= Generate captcha image ==========================

def generate_captcha_img():

    '''
        This function "generate_captcha_image" generates a random 4-digit number and 
        displays it in a 7-segmented display format. The function uses a dictionary called 
        numdict to map each digit to its corresponding 7-segmented display pattern. The function 
        then returns the random number generated.

    '''
    # generate a random 4 digit number
    r = random.randint(1000, 9999)
    print("\nEnter the captcha carefully(for security reasons) :-\n")

    #three unit space for each element in list(adjust space accordingly)
    numdict={
        '1':['   ', ' | ', ' | '],
        '2':[' _ ', ' _|', '|_ '],
        '3':['__ ', '__|', '__|'],
        '4':['   ', '|_|', '  |'],
        '5':[' _ ', '|_ ', ' _|'],
        '6':[' _ ', '|_ ', '|_|'],
        '7':['__ ', '  |', '  |'],
        '8':[' _ ', '|_|', '|_|'],
        '9':[' _ ', '|_|', '  |'],
        '0':[' _ ', '| |', '|_|']
    }

    # print the 4 digit number in 7 segmented display format like clock time
    for i in range(3):
        for j in str(r):
            print(numdict[j][i], end=" ")
        print()

    # return the random number generated 
    return r


# ========================= User entry function for visible captcha =========================
def user_entry(num):

    '''
        This function "user_entry" prompts the user to enter a captcha shown on the screen. The function allows 
        the user to refresh the captcha by entering ‘r’ or ‘R’. The function then checks if the user’s 
        input is a valid integer. If the input is valid, the function checks if it matches the actual 
        answer. If it does, the function returns True. If it does not, the function decrements a counter 
        for the number of tries remaining and repeats the process. If there are no more tries remaining, the 
        function returns False.

    '''
    actual_ans = num
    # max three tries allowed for each refresh(unlimited refresh)
    tries_left = 3
    while tries_left :
        ch = input("\nEnter captcha shown above (to refresh captcha press 'r' or 'R')\nAny other input will be considered invalid : ")
        if ch in ['r', 'R']:
            # call captcha again for new number and update the number of tries
            actual_ans = generate_captcha_img()
            tries_left = 3

        elif ch.isdigit():
            # if valid entry
            if int(ch) == actual_ans:
                return True

            # if not valid entry
            print("\nPlease enter a valid input !\n ")
            tries_left -= 1
            print("Tries left : ", tries_left)

        else:
            print("\nPlease enter a valid input !\n ")
            tries_left -= 1
            print("Tries left : ", tries_left)

    # no more tries left
    return False


#======================== MAIN CAPTCHA FUNCTION =======================

def captcha():

    '''
        The captcha() function generates a random 4-digit number and displays it in a 7-segmented display format. 
        It then prompts the user to enter the displayed value. The function allows the user to refresh the captcha 
        by entering ‘r’ or ‘R’. The function then checks if the user’s input is a valid integer. If the input is 
        valid, the function checks if it matches the actual answer. If it does, the function returns True. If it 
        does not, the function decrements a counter for the number of tries remaining and repeats the process. If 
        there are no more tries remaining, the function returns False.

    '''
    # generate the image
    ans_to_captcha = generate_captcha_img()

    # ask user to enter the dislayed value and return at end if he suceeds in 3 tries
    return user_entry(ans_to_captcha)











PASSWORD = "admin"

# ***************************** DEMAND PASSWORD FROM USER *******************************
def demand_password():

    '''
        The demand_password() function prompts the user to enter a password. If the user enters 
        the correct password, the function calls another function called captcha() to generate a captcha. 
        If the user enters an incorrect password, the function prints an error message and decrements a 
        counter for the number of tries remaining. The function repeats this process until either the 
        correct password is entered or there are no more tries remaining. If there are no more tries remaining, 
        the function returns False.

    '''
    tries_left = 3
    while tries_left:
        password = input("Enter the password : ")
        if password == PASSWORD:
            return captcha()
        tries_left -=1
        print("Tries left : ", tries_left)
    return False
