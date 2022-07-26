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

        # Ship's settings
        self.ship_speed = 0.75
        self.ship_limit = 3

        # Bullet's settings
        self.bullet_speed = 0.5
        self.bullet_width = 250 # 3 ========================
        self.bullet_height = 15
        self.bullet_color = (80, 80, 80)
        self.bullets_allowed = 3

        # Alien's settings
        self.alien_speed = 2 # 1.0 ========================
        self.fleet_drop_speed = 10
        # fleet_direction 1 means the direction of movement to the right -1 -- left
        self.fleet_direction = 1