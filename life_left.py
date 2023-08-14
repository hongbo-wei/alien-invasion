import pygame

from pygame.sprite import Sprite


class Life(Sprite):
    """A class to manage the left life."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/life.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.topleft = self.screen_rect.topleft

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
