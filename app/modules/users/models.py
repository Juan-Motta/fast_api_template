from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String, nullable=False, index=True)
    
    profile_id = Column(Integer, ForeignKey("users_profiles.id"))
    user_profiles = relationship("UserProfile", back_populates="users")
    
    def __repr__(self) -> str:
        return f"<User id={self.id} active={self.active}>"


class UserProfile(Base, TimestampMixin):
    __tablename__ = "users_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    
    users = relationship("User", back_populates="user_profiles")
    
    def __repr__(self) -> str:
        return f"<UserProfile id={self.id} active={self.active}>"
    
    