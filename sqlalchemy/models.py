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

    id = Column(Integer, primary_key=True, autoincrement=True)


class Address(BaseModel):
    __tablename__ = "address"

    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"<Address(street={self.street}, city={self.city}, state={self.state}, zip={self.zip})>"


class User(BaseModel):
    __tablename__ = "user"

    name = Column(String)
    age = Column(Integer)
    addresses: Mapped[list["Address"]] = relationship()

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"


Base.metadata.create_all(engine)
