from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship,
    Mapped,
    mapped_column,
)


DB_URL = "sqlite:///database.db"

engine = create_engine(DB_URL)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)


class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"

    user_id = Column(Integer, ForeignKey("users.id"))
    following_id = Column(Integer, ForeignKey("users.id"))


class User(BaseModel):
    __tablename__ = "users"

    username = Column(String)

    following = relationship(
        "User",
        secondary="following_association",
        primaryjoin=("User.id==FollowingAssociation.user_id"),
        secondaryjoin=("User.id==FollowingAssociation.following_id"),
    )

    def __repr__(self):
        return f"<User(username={self.username}, following={self.following})>"


Base.metadata.create_all(engine)
