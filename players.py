import random

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, height, width):
        """Default constructor of Player

        :param height: height of maze
        :type height: int
        :param width: width of maze
        :type width: int
        """
        self.height = height
        self.width = width
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12, 12))
        self.image.fill("Green")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(self.width) * 20 + 10, random.randrange(self.height) * 20 + 10)

    def random_coordinates(self):
        """Generating random coordinates for player

        :returns: random x-coordinate and y-coordinate for player
        """
        self.rect.x = random.randrange(self.width) * 20 + 4
        self.rect.y = random.randrange(self.height) * 20 + 4

    def check_right_place(self, x, y):
        """Check if the solution is correct

        :param x: x-coordinate of final block
        :type x: int
        :param y: y-coordinate of final block
        :type y: int
        :returns: equality of coordinates of the current and final locations
        :rtype: bool
        """
        return self.rect.x == x * 20 + 4 and self.rect.y == y * 20 + 4
