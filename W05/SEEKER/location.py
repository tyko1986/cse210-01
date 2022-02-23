import random

class Location:
    """An integer number
    
    The Location is a place between 1 and 1000 where the seeker will find the hider 
    
    Attributes:
        
    """

    def random_location():
        """Chooses a random number between 1 and 1000

        """
        location = random.randrange(1, 1001)
        return location