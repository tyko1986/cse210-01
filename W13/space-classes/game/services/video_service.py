#import pyray
import pygame
import constants
import os

class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug
        pygame.font.init()

    def draw_border(self):
        pygame.draw.rect(constants.WIN, constants.BLACK, constants.BORDER)

    def draw_space(self, actor):
        """Draws the space based on actor.

        Args:
            actor: The representation of the space.
        """
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        image = actor.get_image()

        actor_object = pygame.transform.scale(pygame.image.load(os.path.join('space-classes/game/assets', image)), (constants.WIDTH, constants.HEIGHT))
                
        constants.WIN.blit(actor_object, (x, y))

    def draw_ship(self, actor):
        """Draws the ship based on actor.

        Args:
            actor: The representation of the ship.
        """
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        image = actor.get_image()
        rotation = actor.get_rotation()

        SPACESHIP_IMAGE = pygame.image.load(os.path.join('space-classes/game/assets', image))
        actor_object = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE, (constants.SPACESHIP_WIDTH, constants.SPACESHIP_HEIGHT)), rotation)
        
        constants.WIN.blit(actor_object, (x, y))

    def draw_bullets(self, actors):

        """Draws the bullets fired by the spaceship.

        Args:
            actors : The representation of the bullet.
        """
        for actor in actors:
            self.draw_bullet(actor)

    def draw_bullet(self, actor):
        """Draws one single bullet fired by the ship.

        Args:
            actor : The representation of the bullet
        """

        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        if actor.get_color() == constants.YELLOW:
            bullet = pygame.Rect(x + constants.SPACESHIP_WIDTH, y + constants.SPACESHIP_HEIGHT//2, 10, 5)
        else:
            bullet = pygame.Rect(x, y + constants.SPACESHIP_HEIGHT//2, 10, 5)
        
        pygame.draw.rect(constants.WIN, actor.get_color(), bullet)
    
    def draw_score(self, actor):
        """Draw the points that every player got.

        Args:
            actor : The representation of the points.
        """
        text = actor.get_text()
        id = actor.get_id()
        health_text = constants.HEALTH_FONT.render("Health: " + str(text), 1, constants.WHITE)
        if id == 1:
            constants.WIN.blit(health_text, (10, 10))
        else:
            constants.WIN.blit(health_text, (constants.WIDTH - health_text.get_width() - 10, 10))

    def draw_winner(self, actor):
        """Shows the winner ship.

        Args:
            actor : The representation of the winner ship.
        """
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        text = actor.get_text()

        draw_text = constants.WINNER_FONT.render(text, 1, constants.WHITE)
        constants.WIN.blit(draw_text, (x - draw_text.get_width() / 2, y - draw_text.get_height()/2))

    def update_window(self):
        """Updates the screen
        """
        pygame.display.update()
