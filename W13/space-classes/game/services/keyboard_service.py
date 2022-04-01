import pygame
from game.shared.point import Point

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pygame.K_w
        self._keys['a'] = pygame.K_a
        self._keys['s'] = pygame.K_s
        self._keys['d'] = pygame.K_d

        self._keys['left'] = pygame.K_LEFT
        self._keys['right'] = pygame.K_RIGHT
        self._keys['up'] = pygame.K_UP
        self._keys['down'] = pygame.K_DOWN

        self._keys['ctrll'] = pygame.K_LCTRL
        #self._keys['ctrlr'] = pygame.K_RCTRL
        self._keys['ctrlr'] = pygame.K_RSHIFT
        
    def is_key_up(self, keys_pressed, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        return keys_pressed[self._keys[key.lower()]]
        #return pyray.is_key_up(pyray_key)

    def is_key_down(self, keys_pressed, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        return keys_pressed[self._keys[key.lower()]]
        #return pyray.is_key_down(pyray_key)