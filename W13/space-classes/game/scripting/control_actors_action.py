import pygame
import constants
from game.scripting.action import Action
from game.shared.point import Point

class ControlActorsAction(Action):
    """
    An input action that controls the space ships
    
    The responsibility of ControlActorsAction is to get the direction and move the ships and 
    the bullet shooting.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        #self._direction = Point(0, constants.CELL_SIZE)
        #self._direction2 = Point(0, constants.CELL_SIZE) # FCO

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        keys_pressed = pygame.key.get_pressed()
        #print(keys_pressed)

        ship1 = cast.get_actor("spaceship", 0)

        # left
        if self._keyboard_service.is_key_down(keys_pressed, 'a'):
            ship1.moveLeft()
        
        # right
        if self._keyboard_service.is_key_down(keys_pressed, 'd'):
            ship1.moveRight()
        
        # up
        if self._keyboard_service.is_key_down(keys_pressed, 'w'):
            ship1.moveUp()
        
        # down
        if self._keyboard_service.is_key_down(keys_pressed, 's'):
            ship1.moveDown()

        # ctrl left
        if self._keyboard_service.is_key_down(keys_pressed, 'ctrll'):
            ship1.shoot(cast)
        

        ship2 = cast.get_actor("spaceship", 1)

        # left
        if self._keyboard_service.is_key_down(keys_pressed, 'left'):
            ship2.moveLeft()
        
        # right
        if self._keyboard_service.is_key_down(keys_pressed, 'right'):
            ship2.moveRight()
        
        # up
        if self._keyboard_service.is_key_down(keys_pressed, 'up'):
            ship2.moveUp()
        
        # down
        if self._keyboard_service.is_key_down(keys_pressed, 'down'):
            ship2.moveDown()
        
        # ctrl right
        if self._keyboard_service.is_key_down(keys_pressed, 'ctrlr'):
            ship2.shoot(cast)