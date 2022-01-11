""" TIC - TAC - TOE - Alberto de la Rosa """



def main():

    x_player = input('Who is going to be "X": ')
    o_player = input('Who is going to be "O": ')

    
    

    boxes = ['1','2','3','4','5','6','7','8','9']

    
    continue_game = True
    last_turn = 'O'
    

    while continue_game == True:

        display_game(boxes)
        
        print()

        if last_turn =='O':

            choice = int(input((f"{x_player}'s Turn, Please Choose a box(1-9): " )))
            
        else:
            choice = int(input((f"{o_player}'s Turn, Please choose a box(1-9): " )))
        
        play(last_turn,choice,boxes)
        last_turn=switch(last_turn)

        continue_game = end_game(boxes)
        
    display_game(boxes)
    
    winner_looser_tie(boxes,x_player,o_player)

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