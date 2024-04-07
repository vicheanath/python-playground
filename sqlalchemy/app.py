

from models import User, session, Address

# Create a user
user = User(name="John", age=30)
user2 = User(name="Jane", age=25)

# Create an address
address = Address(street="123 Main St", city="New York", state="NY", zip="10001")
address2 = Address(street="456 Elm St", city="Los Angeles", state="CA", zip="90001")
address3 = Address(street="789 Oak St", city="Chicago", state="IL", zip="60007")
# Add the address to the user
user.addresses.extend([address, address2])
user2.addresses.append(address3)

# Add the user to the session
session.add(user)
session.add(user2)
session.commit()

print(f"User: {user.addresses = }")
print(f"User: {user2.addresses = }")


print(f"Address: {address.user = }")