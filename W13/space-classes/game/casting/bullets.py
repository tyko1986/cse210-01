import pygame
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Bullets(Actor):
    """
    An ammo shooted by a space ship to damage its opponent 

    The responsability of the bullet is to move horizontally 
    until leace the screen or hit a sace ship

    Attribuites:
    _color: The color of the bullet 


    """
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._bullets = []

    def get_bullets(self):
        return self._bullets

    def add_bullet(self, ship):
        if len(self._bullets) >= constants.MAX_BULLETS:
            return False

        if ship._id == 1:
            color = constants.YELLOW
        else:
            color = constants.RED

        position = ship.get_position()

        bullet = Actor()
        bullet.set_color(color)
        bullet.set_position(position)
        self._bullets.append(bullet)

        constants.BULLET_FIRE_SOUND.play()
        

    def move_bullets(self):
        for each_bullet in self._bullets:
            position = each_bullet.get_position()
            x = position.get_x()
            y = position.get_y()
            if self._id == 1:
                new_position = Point(x + constants.BULLET_VEL, y)

                if new_position.get_x() > constants.WIDTH:
                    self._bullets.remove(each_bullet)
                else:
                    each_bullet.set_position(new_position)
            else:
                new_position = Point(x - constants.BULLET_VEL, y)

                if new_position.get_x() < 0:
                    self._bullets.remove(each_bullet)
                else:
                    each_bullet.set_position(new_position)
            

    def get_id(self):
        return self._id