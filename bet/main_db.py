from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Bet(Base):
    __tablename__ = 'bets'

    id : Mapped[int] = mapped_column(primary_key=True)
    amount : Mapped[float] = mapped_column()
    outcome = Mapped[float] = mapped_column()
    player = Mapped[Optional["Player"]] = relationship(back_populates="bets")
    
    def __repr__(self):
        return f"Bet(amount={self.amount}, outcome={self.outcome})"

class Commission(Base):
    __tablename__ = 'commissions'

    id : Mapped[int] = mapped_column(primary_key=True)
    rate : Mapped[float] = mapped_column()
    
    def __repr__(self):
        return f"Commission(rate={self.rate})"

class Game(Base):
    __tablename__ = 'games'

    id : Mapped[int] = mapped_column(primary_key=True)
    odds : Mapped[float] = mapped_column()
    type : Mapped[str] = mapped_column()
    
    
    def __repr__(self):
        return f"Game(odds={self.odds}, type={self.type})"

class BaccaratGame(Game):
    __tablename__ = 'baccarat_games'

    id : Mapped[int] = mapped_column(primary_key=True)
    banker : Mapped[float] = mapped_column()
    player : Mapped[float] = mapped_column()
    
    def play(self):
        return "Banker" if self.banker > self.player else "Player"
    
    def __repr__(self):
        return f"BaccaratGame(banker={self.banker}, player={self.player})"

class GameRules(Base):
    __tablename__ = 'game_rules'

    id : Mapped[int] = mapped_column(primary_key=True)
    min_bet_amount : Mapped[float] = mapped_column()
    max_bet_amount : Mapped[float] = mapped_column()
    game : Mapped[Game] = relationship(back_populates="game_rules")
    user : Mapped["User"] = relationship(back_populates="game_rules")
    
    def validate_bet_amount(self, amount: float) -> bool:
        if not (self.min_bet_amount <= amount <= self.max_bet_amount):
            print(f"Bet amount must be between {self.min_bet_amount} and {self.max_bet_amount}.")
            return False
        return True

class User(Base):
    __tablename__ = 'users'

    id :  Mapped[int] = mapped_column(primary_key=True)
    username : Mapped[str] = mapped_column(String(50))
    password : Mapped[str] = mapped_column(String(50))
    balance : Mapped[float] = mapped_column()
    
    def __repr__(self):
        return f"User(username={self.username}, password={self.password}, balance={self.balance})"

class Player(User):
    __tablename__ = 'players'
    bets : Mapped[List[Bet]] = relationship("Bet", back_populates="player")
    game_rules : Mapped[List[GameRules]] = relationship("GameRules", back_populates="user")
    agent = Mapped[Optional["Agent"]] = relationship("Agent", back_populates="players")

class Agent(User):
    __tablename__ = 'agents'

    id : Mapped[int] = mapped_column(primary_key=True)
    commission : Mapped[Commission] = relationship("Commission", back_populates="agent")
    players : Mapped[List[Player]] = relationship("Player", back_populates="agent")
    


def main():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    
    session = Session(engine)
    
    player = Player(username="player", password="password", balance=100.0)
    agent = Agent(username="agent", password="password")
    commission = Commission(rate=0.1)
    
    session.add_all([player, agent, commission])
    session.commit()
 

if __name__ == "__main__":
    main()
    
    
    

