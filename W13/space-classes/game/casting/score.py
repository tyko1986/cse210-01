from game.casting.actor import Actor

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points of each player, if a ship is hit by
    a bullet that player loses one point, if a ship is hit  time, is game over
    It contains methods to reduce points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._points = 10
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_points(self):
        return self._points

    def get_id(self):
        return self._id