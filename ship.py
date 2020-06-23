import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initializes the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('../Ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def bliteme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
