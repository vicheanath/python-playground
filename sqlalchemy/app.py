

from models import User, session

# Create a user
user1 = User(username="user1")
user2 = User(username="user2")
user3 = User(username="user3")

user1.following.append(user2)
user2.following.append(user3)
user3.following.append(user1)

session.add_all([user1, user2, user3])
session.commit()

# Get all users
print(f"{user1.following=}")
print(f"{user2.following=}")
print(f"{user3.following=}")

