import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        """initialize the button attribute """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # Create a rect button object and center it
        self.rect = pygame.rect(0, 0, self.width, self.height)
        self.rect.centr = self.screen_rect.center

        # The message on the button must be shown only once
        self._prep_msg(msg)

    
    def _prep_msg(self, msg):
        """Convert text to image and center the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        """Let's draw an empty button, and then a message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)