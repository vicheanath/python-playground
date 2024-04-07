
from sqlalchemy.orm import sessionmaker

from models import User, engine

# Create a session
Session = sessionmaker(bind=engine)

session = Session()

users = session.query(User).all()

for user in users:
    print(user)
