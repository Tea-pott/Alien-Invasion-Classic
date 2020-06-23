import sys

import pygame

from setting import Setting
from ship import Ship


class AlienInvasion:
    """overall class to manage the game assets and behaviour"""

    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.setting = Setting()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion Classic")

        self.ship = Ship(self)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            # Watch for mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.setting.bg_color)
            self.ship.bliteme()

            # Make the most recent drawn screen visible (screen updates with each event)
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
