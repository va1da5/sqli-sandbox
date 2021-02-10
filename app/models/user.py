from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.db.base_class import Base


class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=False, unique=True, nullable=False)
    created = Column(DateTime, index=False, unique=False, nullable=False)
    admin = Column(Boolean, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<User {}>".format(self.username)
