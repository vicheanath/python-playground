from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Bet:
    amount: float
    outcome: float

@dataclass
class Commission:
    rate: float

@dataclass
class Game(ABC):
    odds: float

    @abstractmethod
    def play(self):
        pass

@dataclass
class BaccaratGame(Game):
    banker: float = 0.0
    player: float = 0.0

    def play(self):
        return "Banker" if self.banker > self.player else "Player"

@dataclass
class AbstractGameRules(ABC):
    @abstractmethod
    def validate_bet_amount(self, amount: float) -> bool:
        pass

@dataclass
class BaccaratGameRules(AbstractGameRules):
    min_bet_amount: float
    max_bet_amount: float

    def validate_bet_amount(self, amount: float) -> bool:
        if not (self.min_bet_amount <= amount <= self.max_bet_amount):
            print(f"Bet amount must be between {self.min_bet_amount} and {self.max_bet_amount}.")
            return False
        return True

@dataclass
class AbstractUser:
    username: str
    password: str
    balance: float = 0.0

@dataclass
class Player(AbstractUser):
    _bets = []

    def __init__(self, username: str, password: str, balance: float, game_rules: AbstractGameRules):
        super().__init__(username, password, balance)
        self.game_rules = game_rules

    def place_bet(self, amount: float, outcome: float) -> bool:
        if not self.game_rules.validate_bet_amount(amount):
            return False

        if amount > self.balance:
            print("Insufficient balance.")
            return False

        self.balance -= amount
        self._bets.append(Bet(amount, outcome))
        return True

    def receive_winnings(self, amount: float) -> None:
        self.balance += amount

@dataclass
class Agent(AbstractUser):
    def __init__(self, username: str, password: str, balance: float = 0.0, commission: Commission = None):
        super().__init__(username, password, balance)
        self.commission = commission if commission else Commission(0.05)
        self.player : list[Player] = []

    def calculate_commission(self, amount: float) -> float:
        self.receive_commission(amount * self.commission.rate)
        return amount * self.commission.rate

    def receive_commission(self, amount: float) -> None:
        self.balance += amount
        
    def get_commission(self):
        return self.commission.rate
    
    def get_balance(self):
        return self.balance
    
    def add_player(self, player : Player) -> None:
        self.player.append(player)
    
@dataclass
class AbstractGameApp(ABC):
    @abstractmethod
    def conduct_bet(self, player, amount, outcome):
        pass

@dataclass
class BaccaratGameApp(AbstractGameApp):
    agent: Agent
    game: Game

    def conduct_bet(self, player, amount, outcome):
        if player.place_bet(amount, outcome):
            commission = self.agent.calculate_commission(amount)
            amount -= commission
            if outcome == self.game.play():
                player.receive_winnings(amount * self.game.odds)
            else:
                print("You lost.")
        else:
            print("Bet failed.")

# Example Usage
# if __name__ == "__main__":
#     # Create a game
#     plyer = 1
#     banker = 2
#     odds = 1.5
#     game = BaccaratGame(odds, plyer, banker)

#     # Create a game rule
#     min_bet_amount = 10
#     max_bet_amount = 100
#     game_rules = BaccaratGameRules(min_bet_amount, max_bet_amount)

#     # Create a commission
#     rate = 0.05
#     commission = Commission(rate)

#     # Create an agent
#     agent = Agent("John", "1234", commission=commission)

#     # Create a player
#     player = Player("Alice", "1234", 1000, game_rules)

#     # Create a game app
#     game_app = BaccaratGameApp(agent, game)

#     # Conduct a bet
#     game_app.conduct_bet(player, 50, plyer)
#     print("Player balance: ", player.balance)
#     game_app.conduct_bet(player, 50, banker)
#     print("Player balance: ", player.balance)
    
#     # print agent commission
#     print("Agent Balance: ", agent.get_balance())
    


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "First FastAPI app"}