import unittest
from bet.main import (
    AbstractUser,
    Player,
    Bet,
    Commission,
    Agent,
    AbstractGameApp,
    BaccaratGameApp,
    Game,
)

class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = Player("player", "password", 100.0)
        
    def test_create_player(self):
        self.assertEqual(self.player.username, "player")
        self.assertEqual(self.player.password, "password")
        self.assertEqual(self.player.balance, 100.0)
    
    