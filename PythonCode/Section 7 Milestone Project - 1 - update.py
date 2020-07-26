# ------------------------ Section 7 "UPDATE" is from part 59-63   -----------------------------

# # # # # # # # # #  part 59 (Warm Up Project Exercises) # # # # # # # # #

#shwoing the XO layout
#getting the user input 
# Run a script
# showing it to the XO layout
#REDO the staff again and again


def displayboard(row1,row2,row3):
    '''
    Display the TIC TAC TOE grid
    '''
    print(row1)
    print(row2)
    print(row3)


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
row2[1] = 'X'
displayboard(row1,row2,row3)

# # # # # # # # # #  part 61-62 (Validating User Input) # # # # # # # # #
def user_choice():
    '''
    User inputs a number (0-10) and we return this in integer form.
    No parameter is passed when calling this function.
    '''
    checking = True
    while checking:
        choice = input("Please type an input between (0-10) ")
        if choice.isdigit() == True:
            checking == False
        else: 
            print('Sorry the value you entered in not a digit')
            continue
        
        if int(choice) in range(0,10):
            checking == False
            break
        else:
            print('Your values is not in range between(0-10)')
            continue

    return int(choice)


print(user_choice())

#----------------------------- TEACHER SOLUTION -------------------------
""" 
def user_choice():
    
    choice ='WRONG'
    within_range = False
    
    while choice.isdigit() == False or within_range == False:
        
    
    
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
            
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                within_range = False
        
    
    return int(choice)
"""

# # # # # # # # # #  part 63 (User interaction) # # # # # # # # #

def gameon_choice():
    choice = False
    while choice == False:
        user_choice = input('Do u want to play ? Y or N ')
        if user_choice.upper() == 'N':
            return False
        elif user_choice.upper() == 'Y':
            return True
        else:
            print('Please type Y or N')
            continue

print(gameon_choice())



# # # # # # # # # #  part 61 (Methods and the Python Documentation) # # # # # # # # #

