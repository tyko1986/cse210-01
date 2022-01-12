"""      TIC - TAC - TOE  
       Alberto de la Rosa
CSE210 - Programming with Classes
"""

def main():
    #Ask the name of the players
    x_player = input('Who is going to be "X": ')
    o_player = input('Who is going to be "O": ')

    #Create a list called "boxes" which will store the number of each box
    #of the TIC TAC TOE
    boxes = ['1','2','3','4','5','6','7','8','9']
    
    #Regiter data for the While Loop
    continue_game = True
    last_turn = 'O'
    
    #Create a Loop that will be repeating until some player wins or all the boxes are taken
    while continue_game == True:

        #Call a funcion that will display the tic-tac-toe
        display_game(boxes)
        print()
        
        # Use the IF and ELSE to identify the player's turn 
        if last_turn =='O':
            choice = int(input((f"{x_player}'s Turn, Please Choose a box(1-9): " )))           
        else:
            choice = int(input((f"{o_player}'s Turn, Please choose a box(1-9): " )))

        # Call the Function to make the players move        
        play(last_turn,choice,boxes)
        
        # Call a function that will change the player's turn
        last_turn=switch(last_turn)

        # Verify if the game can continue or of there is a winner or a tie
        # the loop ends.
        continue_game = end_game(boxes)

    # Once the loop ends, it is called a function to display the tic tac toe 
    # to show the winner or a tie.   
    display_game(boxes)
    
    # Call a function that will congratulate the winner 
    # or will show a message that there has been a tie
    winner_looser_tie(boxes,x_player,o_player)

    # Print a Farewell message.
    print('Thank you for playing TIC-TAC-TOE')


def switch(last_turn):
    if last_turn == 'O':
        return 'X'
    else:
        return 'O'

def play(last_turn,choice,boxes):
    if last_turn == 'O':
        boxes[choice-1] = 'X'
    else:
        boxes[choice-1] = 'O'
 
def display_game(boxes):      
    print(f'{boxes[0]} | {boxes[1]} | {boxes[2]}')
    print('_________')
    print(f'{boxes[3]} | {boxes[4]} | {boxes[5]}')
    print('_________')
    print(f'{boxes[6]} | {boxes[7]} | {boxes[8]}')

def end_game(boxes):

    if ((boxes[0] == 'X' and boxes[1] == 'X' and boxes[2] == 'X') 
        or (boxes[3] == 'X' and boxes[4] == 'X' and boxes[5] == 'X') 
        or (boxes[6] == 'X' and boxes[7] == 'X' and boxes[8] == 'X') 
        or (boxes[0] == 'X' and boxes[3] == 'X' and boxes[6] == 'X') 
        or (boxes[1] == 'X' and boxes[4] == 'X' and boxes[7] == 'X')
        or (boxes[2] == 'X' and boxes[5] == 'X' and boxes[5] == 'X')
        or (boxes[0] == 'X' and boxes[4] == 'X' and boxes[8] == 'X')
        or (boxes[2] == 'X' and boxes[4] == 'X' and boxes[6] == 'X')):
        return False

    elif ((boxes[0] == 'O' and boxes[1] == 'O' and boxes[2] == 'O') 
        or (boxes[3] == 'O' and boxes[4] == 'O' and boxes[5] == 'O') 
        or (boxes[6] == 'O' and boxes[7] == 'O' and boxes[8] == 'O') 
        or (boxes[0] == 'O' and boxes[3] == 'O' and boxes[6] == 'O') 
        or (boxes[1] == 'O' and boxes[4] == 'O' and boxes[7] == 'O')
        or (boxes[2] == 'O' and boxes[5] == 'O' and boxes[5] == 'O')
        or (boxes[0] == 'O' and boxes[4] == 'O' and boxes[8] == 'O')
        or (boxes[2] == 'O' and boxes[4] == 'O' and boxes[6] == 'O')):
        return False

    elif (boxes[0] != '1' and boxes[1] !=  '2' and boxes[2] != '3' 
        and boxes[3] != '4' and boxes[4] != '5' and boxes[5] != '6' 
        and boxes[6] != '7' and boxes[7] != '8' and boxes[8] != '9'):
        return False
    
    else:
        return True

def winner_looser_tie(boxes,x_player,o_player):
    
    if ((boxes[0] == 'X' and boxes[1] == 'X' and boxes[2] == 'X') 
        or (boxes[3] == 'X' and boxes[4] == 'X' and boxes[5] == 'X') 
        or (boxes[6] == 'X' and boxes[7] == 'X' and boxes[8] == 'X') 
        or (boxes[0] == 'X' and boxes[3] == 'X' and boxes[6] == 'X') 
        or (boxes[1] == 'X' and boxes[4] == 'X' and boxes[7] == 'X')
        or (boxes[2] == 'X' and boxes[5] == 'X' and boxes[5] == 'X')
        or (boxes[0] == 'X' and boxes[4] == 'X' and boxes[8] == 'X')
        or (boxes[2] == 'X' and boxes[4] == 'X' and boxes[6] == 'X')):
        print(f'Congratulaions {x_player.upper()} You won this match')
        print(f'Sorry {o_player.upper()}, better luck next time')
        

    elif ((boxes[0] == 'O' and boxes[1] == 'O' and boxes[2] == 'O') 
        or (boxes[3] == 'O' and boxes[4] == 'O' and boxes[5] == 'O') 
        or (boxes[6] == 'O' and boxes[7] == 'O' and boxes[8] == 'O') 
        or (boxes[0] == 'O' and boxes[3] == 'O' and boxes[6] == 'O') 
        or (boxes[1] == 'O' and boxes[4] == 'O' and boxes[7] == 'O')
        or (boxes[2] == 'O' and boxes[5] == 'O' and boxes[5] == 'O')
        or (boxes[0] == 'O' and boxes[4] == 'O' and boxes[8] == 'O')
        or (boxes[2] == 'O' and boxes[4] == 'O' and boxes[6] == 'O')):
        print(f'Congratulaions {o_player.upper()} You won this match')
        print(f'Sorry {x_player.upper()}, better luck next time')

    elif (boxes[0] != '1' and boxes[1] !=  '2' and boxes[2] != '3' 
        and boxes[3] != '4' and boxes[4] != '5' and boxes[5] != '6' 
        and boxes[6] != '7' and boxes[7] != '8' and boxes[8] != '9'):
        print('It is a TIE')        
    
if __name__ == "__main__":
    main()