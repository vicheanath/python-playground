from sqlalchemy import Column,String,Integer, create_engine
from sqlalchemy.orm import declarative_base


DB_URL = "sqlite:///database.db"

engine = create_engine(DB_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"


Base.metadata.create_all(engine)
