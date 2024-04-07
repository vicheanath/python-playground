from dataclasses import dataclass, field
from typing import List
from abc import ABC, abstractmethod
from datetime import datetime


@dataclass
class BaseModel(ABC):
    name: str
    description: str
    tags: List[str] = field(default_factory=list)


@dataclass
class User(BaseModel):
    balance: int
    username: str
    password: str
    email: str
    phone: str
    address: str
    bets: List = field(default_factory=list)
    
    def deduct_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
        
    def add_balance(self, amount):
        self.balance += amount
        
    def __str__(self):
        return f"User: {self.username} with balance: {self.balance}"

@dataclass
class Transaction(BaseModel):
    amount: int
    user: User
    description: str
    transaction_type: str
    date: datetime = datetime.now()
    def __str__(self):
        return f"Transaction: {self.amount} {self.transaction_type} by {self.user.username} on {self.date}"
    
@dataclass
class SportEvent(BaseModel):
    home_team: str
    away_team: str
    start_time: datetime
    end_time: datetime
    home_team_odds: float
    away_team_odds: float
    draw_odds: float
    
    def __str__(self):
        return f"SportEvent: {self.home_team} vs {self.away_team} on {self.start_time}"
    
@dataclass
class Bet(BaseModel):
    user: User
    amount: int
    outcome: str
    event: SportEvent
    transaction: Transaction
    
    def __str__(self):
        return f"Bet: {self.user.username} bet {self.amount} on {self.outcome} for {self.event.home_team} vs {self.event.away_team}"
    
@dataclass
class Permission(BaseModel):
    name: str
    description: str
    
    def __str__(self):
        return f"Permission: {self.name} with description: {self.description}"
    
@dataclass
class Role(BaseModel):
    name: str
    description: str
    permissions: List[Permission] = field(default_factory=list)
    
    def __str__(self):
        return f"Role: {self.name} with permissions: {self.permissions}"
    


@dataclass
class Commission(BaseModel):
    commission_rate: float
    description: str
    users: User
    
    def __str__(self):
        return f"Commission: {self.commission_rate} with description: {self.description}"
    