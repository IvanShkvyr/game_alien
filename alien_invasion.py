import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
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
        
        # Mode is not full screen
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        # Full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        #Create an instance to save game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main game loop"""

        while True:
            self._check_events()  

            if  self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()    


    def _check_aliens_bottom(self):
        """Check if any newcomer has reached the bottom edge of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Зреагувати так, ніби корабель було підпито
                self._ship_hit()
                break


    def _check_bullet_alien_collisions(self):
        """The reaction to the collision of the keel with the aliens"""
        # Remove all the bullets and aliens that collided
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing orbs and create a new fleet
            self.bullets.empty()
            self._create_fleet()  #!!!!!!Створює новий флот---------------------------!!!!!!


    def _check_events(self):
        """Tracks mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _change_fleet_direction(self):
        """Descent of the entire fleet and change of direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _check_fleet_edges(self):
        """
        Reacts according to whether one of the aliens has reached the edge of the screen
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


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
        # Create aliens and determine the number of aliens in a row
        # The distance between the vrybulys is equal to 0 and 5 of the width of one vrybuly
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine how many rows of aliens fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_heigth - (3 * alien_height) - ship_height) 
        number_rows = available_space_y // (2 * alien_height) + 1 #прибрати + 1 ===============

        # Create a full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            


    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number * 0.7  #прибрати * 0.7=========
        self.aliens.add(alien)



    def _fire_bullet(self):
        """Create new bullet and add it to the bullet's group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _ship_hit(self):
        """"React to the collision of the alien with the ship"""
        if self.stats.ships_left > 0:
            # Reduce ships_left
            self.stats.ships_left -= 1

            # Get rid of excess aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False


    def _update_aliens(self):
        """Check if the fleet is on the edge, then update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look to see if any of the aliens have reached the bottom of the screen.
        self._check_aliens_bottom()


    def _update_bullets(self):
        """Update the position of the bullets and get rid of the old bullets"""
        # Update bullet's position
        self.bullets.update()

        # Removing missing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()


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


