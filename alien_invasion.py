import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """
    The main class that manages the game's resources and behavior
    """

    def __init__(self):
        """Initialize game, create game resources"""
        pygame.init()
        self.settings = Settings()
        
        #режим неповноекранний
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        #Повноекранний режим
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main game loop"""

        while True:
            self._check_events()  
            self.ship.update()
            self._update_bullets()
            self._update_screen()    

    
    def _check_events(self):
        """Tracks mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self, event):
        """Response when the key is pressed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_keyup_events(self, event):
        """Response when the key is not pressed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _create_fleet(self):
        """Create alien's fleet"""
        # створити прибульців та визначити кількість прибульців у ряду.
        # Відстань між врибульцями дорівнює 0ю5 ширині одного прибульця
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Створити перший ряд прибульців.
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)
            


    def _create_alien(self, alien_number):
        """Створити прибульця та поставити його в ряду"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)



    def _fire_bullet(self):
        """Create new bullet and add it to the bullet's group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    

    def _update_bullets(self):
        """Update the position of the bullets and get rid of the old bullets"""
        # Update bullet's position
        self.bullets.update()

        # Removing missing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):
        """Draw the screen every iteration of the cycle"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Show last screen
        pygame.display.flip()


if __name__ == "__main__":
    # Create the game and run it
    ai = AlienInvasion()
    ai.run_game()


