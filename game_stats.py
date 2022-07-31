class GameStats:
    """Tracking game statistics"""

    def __init__(self, ai_game):
        """Initialization of statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game in an active state
        self.game_active = False

    
    def reset_stats(self):
        """Initialization of statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit