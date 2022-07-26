from turtle import right
import pygame

class Ship:
    """A ship control class"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Upload the image of the ship and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Create a new ship at the bottom of the screen, in the center
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the horizontal position of the ship
        self.x = float(self.rect.x)

        # Motion indicator
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
         Update the ship's current position based on the motion indicator
        """
        #Update value ship.x, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update object rect whith self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)