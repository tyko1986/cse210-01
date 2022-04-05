from turtle import position
import constants
from game.casting.actor import Actor
from game.shared.point import Point
import pygame

class Spaceship(Actor):
    """
    A flying artifact that flies over the space.
    
    The responsibility of Spaceship is to avoid its rival bullets and 
    at the same time shoots bullets against its rival.

    Attributes:
    _position: Where the Ship starts in the game.
    _image: Distinguish the color of the ship
    
    """
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._prepare_body()

    def moveLeft(self):
        """Makes the spaceship move to the left
        """
        x = self._position.get_x()
        y = self._position.get_y()
        if self._id == 1:
            if x - constants.VEL > 0:
                position = Point(x - constants.VEL, y)
                self.set_position(position)
        else:
            if x - constants.VEL > constants.BORDER.x + constants.BORDER.width:
                position = Point(x - constants.VEL, y)
                self.set_position(position)

    def moveRight(self):
         """Makes the spaceship move to the right
        """
        x = self._position.get_x()
        y = self._position.get_y()
        if self._id == 1:
            if x + constants.VEL + constants.SPACESHIP_WIDTH < constants.BORDER.x:
                position = Point(x + constants.VEL, y)
                self.set_position(position)
        else:
            if x + constants.VEL + constants.SPACESHIP_WIDTH < constants.WIDTH:
                position = Point(x + constants.VEL, y)
                self.set_position(position)

    def moveUp(self):
        """Makes the spaceship move to up
        """
        x = self._position.get_x()
        y = self._position.get_y()
        if self._id == 1:
            if y - constants.VEL > 0:
                position = Point(x, y - constants.VEL)
                self.set_position(position)
        else:
            if y - constants.VEL > 0:
                position = Point(x, y - constants.VEL)
                self.set_position(position)

    def moveDown(self):
        """Makes the spaceship to move down
        """
        x = self._position.get_x()
        y = self._position.get_y()
        if self._id == 1:
            if y + constants.VEL + constants.SPACESHIP_HEIGHT < constants.HEIGHT - 15:
                position = Point(x, y + constants.VEL)
                self.set_position(position)
        else:
            if y + constants.VEL + constants.SPACESHIP_HEIGHT < constants.HEIGHT - 15:
                position = Point(x, y + constants.VEL)
                self.set_position(position)

    def shoot(self, cast):
         """Makes the ship to shoot a bullet.

        Args:
            cast : What makes the bullets to be added.
        """
        if self._id == 1:
            bulletObj1 = cast.get_actor("bullets", 0)
            bulletObj1.add_bullet(self)
        else:
            bulletObj2 = cast.get_actor("bullets", 1)
            bulletObj2.add_bullet(self)

    def _prepare_body(self):
        """Sets the images and the sizes for the ships.
        """

        if self._id == 1:
            position = Point(100, 300)
            self.set_position(position)
            self.set_image('spaceship_yellow.png')
            self.set_rotation(90)
        else:
            position = Point(700, 300)
            self.set_position(position)
            self.set_image('spaceship_red.png')
            self.set_rotation(270)
