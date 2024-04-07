class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deduct_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def add_balance(self, amount):
        self.balance += amount


class BettingAgent:
    def __init__(self, commission_rate):
        self.commission_rate = commission_rate
        self.users = {}

    def register_user(self, user):
        self.users[user.name] = user

    def take_bet(self, user_name, amount, outcome):
        user = self.users.get(user_name)
        if user and user.deduct_balance(amount):
            user.add_balance(-amount)  # Deduct the bet amount
            self.bets.append((user_name, amount, outcome))

    def settle_bets(self, winning_outcome):
        total_winnings = 0
        for user_name, amount, outcome in self.bets:
            if outcome == winning_outcome:
                total_winnings += amount * 2  # Assuming even odds
        commission = total_winnings * self.commission_rate
        total_winnings -= commission
        self.bets = []  # Reset bets after settling
        return total_winnings


# Example usage:
agent = BettingAgent(0.05)  # Commission rate of 5%

# Register users
user1 = User("Alice", 1000)
user2 = User("Bob", 2000)
agent.register_user(user1)
agent.register_user(user2)

# Users place bets
agent.take_bet("Alice", 100, "A")
agent.take_bet("Bob", 200, "B")
agent.take_bet("Alice", 150, "A")

# Settle bets
winnings = agent.settle_bets("A")
print("Total winnings after commission:", winnings)
