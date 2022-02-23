from seeker import Seeker
from location import Location

class Hider:
    """It's a person who leads the game.
    
    The responsibility of a Hider is to called for a random number and then help with hints 
    the seeker to find a random location
    
    Attributes:
        name: a string. The Seeker's name
        user_choice: a string. It can be "l"(lower) or "h"(higher)
        first_number: a string. The value of the showed card
        second_number: a string. The value of the next card
        score: an integer. The player's score. It starts with 300
        quit: a "y"(yes) character. If the player inputs this, the game is over
        game_over : a string. The messege that players will see when the game is over
    """
    
    def __init__(self):
        """Constructs a new Dealer
        """
        self.name = ""
        self.location = 0
        self.guess = 0
        self.distance = 0
        self.balance = 1000
        self.colder_warmer = ""
        
        pass

    def game(self):
        """Calls the other functions and attributes in order
        """
        self.name = Seeker.name()
        print(f'\nHi {self.name}... WELCOME TO SEEKER !!!')
        print('Try to find the Location of the seeker by guessing a number between 1 and 1000')
        print('The Hider will help you with hints letting you know if you are closer to the right location')
        
        self.location = Location.random_location()
        

        while self.location != self.guess:
            Hider.get_guess(self)
            Hider.get_distance(self)
            if self.distance != 0:
                Hider.cold_warm(self)
                print(self.colder_warmer)
            else:
                break
        
        print(f"You guess correctly, the right location is {self.location}")
            



    pass



    def get_guess(self):

        self.guess = int(input('Please choose a location between 1 and 1000: '))
        while self.guess < 1 and self.guess > 1000:
            self.guess = int(input('Please choose a location between 1 and 1000: '))    
    

    def get_distance(self):
        self.distance = self.guess - self.location 
        pass

    def cold_warm(self):
        if self.distance < 0:
            self.distance = self.distance * (-1)
        else:
            self.distance = self.distance * 1
        
        if self.distance < self.balance:
            self.colder_warmer = "You are getting Warmer"
            self.balance = self.distance
        else:
            self.colder_warmer = "You are getting Colder"
            self.balance = self.distance
        pass
            
        

    
