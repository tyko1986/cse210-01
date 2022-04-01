import pygame
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the bullet impacts
    the adversary space ship, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._id_game_over = 0
        self._counter = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_bullet_collision(cast)
            self._handle_game_over(cast)

    def _handle_bullet_collision(self, cast):
        """Updates the score when a bullet hits a space ship it is reduced one point from the 
        attacked ship.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_actor("score", 0)
        score2 = cast.get_actor("score", 1)

        ship1 = cast.get_actor("spaceship", 0)
        ship1_position = ship1.get_position()
        ship1_rect = pygame.Rect(ship1_position.get_x(), ship1_position.get_y() - constants.SPACESHIP_HEIGHT/2, constants.SPACESHIP_WIDTH, constants.SPACESHIP_HEIGHT)
        
        ship2 = cast.get_actor("spaceship", 1)
        ship2_position = ship2.get_position()
        ship2_rect = pygame.Rect(ship2_position.get_x(), ship2_position.get_y() - constants.SPACESHIP_HEIGHT/2, constants.SPACESHIP_WIDTH, constants.SPACESHIP_HEIGHT)

        bulletObj1 = cast.get_actor("bullets", 0)
        bullets1 = bulletObj1.get_bullets()

        for bullet in bullets1:
            bullet_position = bullet.get_position()
            bullet_rect = pygame.Rect(bullet_position.get_x() + constants.SPACESHIP_WIDTH, bullet_position.get_y(), 10, 5)
            if ship2_rect.colliderect(bullet_rect):
                constants.BULLET_HIT_SOUND.play()
                score2.add_points(-1)
                bullets1.remove(bullet)
                if score2.get_points() <= 0:
                    self._is_game_over = True
                    self._id_game_over = 2

        bulletObj2 = cast.get_actor("bullets", 1)
        bullets2 = bulletObj2.get_bullets()

        for bullet in bullets2:
            bullet_position = bullet.get_position()
            bullet_rect = pygame.Rect(bullet_position.get_x(), bullet_position.get_y(), 10, 5)
            if ship1_rect.colliderect(bullet_rect):
                constants.BULLET_HIT_SOUND.play()
                score1.add_points(-1)
                bullets2.remove(bullet)
                if score1.get_points() <= 0:
                    self._is_game_over = True
                    self._id_game_over = 1

    
    def _handle_game_over(self, cast):
        """Shows the a message calling the winner
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            x = constants.WIDTH // 2
            y = constants.HEIGHT // 2
            position = Point(x, y)

            message = Actor()
            message.set_position(position)

            if self._id_game_over == 1:
                message.set_text("Red Wins!")
            else:
                message.set_text("Yellow Wins!")
            
            cast.add_actor("messages", message)
            