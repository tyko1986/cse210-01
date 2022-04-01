from game.casting.actor import Actor
from game.shared.point import Point

class Space(Actor):
    """
    A background area that shows the space where the ships move around

    Attributes:

    _position: It is place as background
    _image: It shows an ouyer space image
    
    """
    def __init__(self):
        super().__init__()
        
        position = Point(0, 0)
        self.set_position(position)
        self.set_image('space.png')
        self.set_rotation(0)
