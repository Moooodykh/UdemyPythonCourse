# ------------------------ Section 7 "Milestone Project - 1" is from part 54 to 58   -----------------------------

grid_position=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#SHOWING the grid of TIC TAC TOC

def display_board():
    """ 
    This function is to displaying the board
    """
    # grid_position=['#','X','O','X','O','X','O','X','O','X']
    print(grid_position[7] +' | ' + grid_position[8] +' | '+ grid_position[9] )
    print(grid_position[4] +' | ' + grid_position[5] +' | '+ grid_position[6] )
    print(grid_position[1] +' | ' + grid_position[2] +' | '+ grid_position[3] )
# display_board()

#-------------------------------------------
def winner(marker1,marker2):
    """ 
    This function is to define if there is winner or not
    """
    # grid_position=['#','O','X','X','X','X','O','O','O','X']
    if  grid_position[1] == grid_position[2] == grid_position[3] == marker1 or \
        grid_position[4] == grid_position[5] == grid_position[6] == marker1 or \
        grid_position[7] == grid_position[8] == grid_position[9] == marker1 or \
        grid_position[1] == grid_position[4] == grid_position[7] == marker1 or \
        grid_position[2] == grid_position[5] == grid_position[8] == marker1 or \
        grid_position[3] == grid_position[6] == grid_position[9] == marker1 or \
        grid_position[1] == grid_position[5] == grid_position[9] == marker1 or \
        grid_position[3] == grid_position[5] == grid_position[7] == marker1 :
        return (f'The game is finished and player 1 who has a "{marker1}" marker won')

    elif ( 
        #this first three lines are for horizontal lines
           grid_position[1] == grid_position[2] == grid_position[3] == marker2  
        or grid_position[4] == grid_position[5] == grid_position[6] == marker2  
        or grid_position[7] == grid_position[8] == grid_position[9] == marker2  
        #this second three lines are for vertical linesmarker2 
        or grid_position[1] == grid_position[4] == grid_position[7] == marker2   
        or grid_position[2] == grid_position[5] == grid_position[8] == marker2   
        or grid_position[3] == grid_position[6] == grid_position[9] == marker2   
        #this third two lines are for diagnal linesmarker2 
        or grid_position[1] == grid_position[5] == grid_position[9] == marker2  
        or grid_position[3] == grid_position[5] == grid_position[7] == marker2  
        ): 
        return (f'The game is finished and player 2 who has a "{marker2}" marker won')
    else:
        return '' 
# print(winner('X','O'))

#-----------------------------------------

#INPUT from players
def user_input():
    """ 
    This function to take define which marker will be to each player
    """
    player2_marker = None
    player1_marker = None
    play = True

        
    while play:
        player_choice = input("Do you want to play TIC TAC TOC ?")
        if player_choice.lower() == 'yes':
            while player_choice.lower() == 'yes':
                player1_marker = input("As a first player , which is your favorite style  'X' or 'O' ")
                if player1_marker == 'X':
                    player2_marker = 'O'
                    player_choice = 'no'
                elif player1_marker == 'O':
                    player2_marker = 'X'
                    player_choice = 'no'
                else:    
                    print('Please choose either "O" or "X"')       
            
            return(player1_marker,player2_marker)
        else:
            play = False

    print('Thanks and hopefully see you again later on')
    exit() # to finish the program at all
       
    


# marker1, marker2 = user_input()
# print(f'player 1 has {marker1}\nplayer 2 has {marker2}')
#------------------------------------------

def grid_filling(marker1,marker2):
    """ 
    This function is to fill the grid with each marker for each player
     """
    loop=True
    counter = 1
    while counter < 9:
        while loop:
            player1_number = int(input("In which place would you place your marker ?"))
            if player1_number <= 9:
            
                if grid_position[player1_number] != ' ':
                    print('You need to choose another number,this place is already taken')
                    continue
                else:
                    grid_position[player1_number] = marker1
                    display_board()
                    win= winner(marker1,marker2)
                    if win == '':
                        loop = False # jump to the second player
                        counter +=1
                        
                        if counter == 8: # make the last round 
                            loop = True
                        break
                    else:
                        counter = 10
                        print(win)
                        break
            else:
                print('You need to enter a number between 0 and 9')

        while not loop:
            player2_number = int(input("As a second player, in which place would you place your marker ?"))
            if player2_number <= 9:
            
                if grid_position[player2_number] != ' ':
                    print('You need to choose another number,this place is already taken')
                    continue
                else:
                    grid_position[player2_number] = marker2
                    display_board()
                    win= winner(marker1,marker2)
                    if win == '':
                        loop = True # jump to first player
                        counter +=1
                        break
                    else:
                        counter = 10
                        print(win)
                        break     
            else:
                print('You need to enter a number between 0 and 9')
        


#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# # Calling the game
marker1,marker2 = user_input()    
grid_filling(marker1,marker2)


    

