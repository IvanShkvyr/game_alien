class Settings:
    """
    Class that stores all game settings
    """

    def __init__(self):
        """Initialize game settings """
        # Screen settings
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (128, 128, 255)

        # Ship's setting
        self.ship_speed = 0.75

        # Bullet's setting
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (80, 80, 80)
        self.bullets_allowed = 3