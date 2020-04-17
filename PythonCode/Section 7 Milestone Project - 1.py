# ------------------------ Section 7 "Milestone Project - 1" is from part 54 to 58   -----------------------------

#SHOWING the grid of TIC TAC TOC
# we need to clean the board each time and put the stored list value
grid_position=['#']
grid_position2=['#','X','O','X','O','X','O','X','O','X']
print(grid_position[7] +'|' + grid_position[8] +'|'+ grid_position[9] )
print(grid_position[4] +'|' + grid_position[5] +'|'+ grid_position[6] )
print(grid_position[1] +'|' + grid_position[2] +'|'+ grid_position[3] )


#INPUT from players
def user_input():
    player2_marker = None
    player_choice = input("Do you want to lay TIC TAC TOC")
    while player_choice.lower() == 'yes':

        player1_marker = input("As a first player , which is your favorite style  'X' or 'O' ")
        while(player1_marker == 'X' or player1_marker=='O'):
            if player1_marker == 'X':
                player2_marker = 'O'
            else:
                player2_marker = 'X'

    return((player1_marker,player2_marker))    


def grid_number(marker1,marker2):

    player1_number = int(input("In which place would you place your marker ?"))
    while player1_number <= 9:
        if grid_position[player1_number] != []:
            print('You need to choose another number,this place is already taken')
            continue
        else:
            grid_position.insert(player1_number,marker1)
          




















# # # # # # # # # #  part 54 () # # # # # # # # #

# # # # # # # # # #  part 55 () # # # # # # # # #

# # # # # # # # # #  part 56 () # # # # # # # # #

# # # # # # # # # #  part 57 () # # # # # # # # #

# # # # # # # # # #  part 58 () # # # # # # # # #

# ------------------------------------------------------------------------------------
### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

print('---------------------------------------------')

