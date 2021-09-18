import pygame
from Constants import *
vec = pygame.math.Vector2


class Enemy:
    """
    This class describe an Enemy class in Pacman game (Ghost).
    Now it is only for add AFK enemy. All mob functional will be added later, in next labs.
    """
    def __init__(self, application, start_position):
        self.type = None
        self.application = application
        self.position = start_position
        self.pix_position = self.get_pix_pos()

    def draw(self):
        """
        Drawing the Ghost with some parameters, like color, position and size
        :return:
        """
        pygame.draw.circle(self.application.screen, RED,
                           (self.pix_position.x, self.pix_position.y),
                           self.application.cell_width//2-2)

    def get_pix_pos(self):
        """
        This method finds a pixel position of Ghost to make more easier to draw it on map.
        :return: vector(x,y) where x is an X coordinate the center of Ghost. y - Y coordinate with same meaning.
        """
        return vec((self.position[0]*self.application.cell_width) + PADDING // 2 + self.application.cell_width // 2,
                   (self.position[1]*self.application.cell_height) +
                   PADDING // 2 + self.application.cell_height // 2)
