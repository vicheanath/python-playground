from .models import User, Transaction, SportEvent, Bet, Permission, Role


class UserTransactionService:
    def __init__(self, user: User):
        self.user = user

    def deduct_balance(self, amount):
        if self.user.balance >= amount:
            self.user.balance -= amount
            return True
        else:
            return False

    def add_balance(self, amount):
        self.user.balance += amount

    def __str__(self):
        return f"User: {self.user.username} with balance: {self.user.balance}"
    

class RolePermissionService:
    def __init__(self, role: Role):
        self.role = role

    def add_permission(self, permission: Permission):
        self.role.permissions.append(permission)

    def remove_permission(self, permission: Permission):
        self.role.permissions.remove(permission)

    def __str__(self):
        return f"Role: {self.role.name} with permissions: {[p.name for p in self.role.permissions]}"
    
    
class SportEventService:
    def create_event(self, home_team, away_team, start_time, end_time, home_team_odds, away_team_odds, draw_odds):
        return SportEvent(home_team, away_team, start_time, end_time, home_team_odds, away_team_odds, draw_odds)
    
    def delete_event(self, event: SportEvent):
        del event
        
    def __str__(self):
        return f"SportEvent: {self.home_team} vs {self.away_team} on {self.start_time}"
    