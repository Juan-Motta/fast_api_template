import hashlib
import binascii

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin
from app.config.settings import settings


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    password = Column(String, nullable=False, index=True)
    
    profile_id = Column(Integer, ForeignKey("users_profiles.id"))
    user_profiles = relationship("UserProfile", back_populates="users")
    
    @property
    def password(self) -> None:
        raise AttributeError('password is not a readable attribute')
    
    def set_password(self, password: str) -> None:
        dk = hashlib.pbkdf2_hmac(
            "sha256", 
            password.encode("utf-8"), 
            settings.SECRET_KEY.encode("utf-8"), 
            100000
        )
        hashed_password = binascii.hexlify(dk).decode("utf-8")
        self.password = f"pbkdf2_sha256$100000${hashed_password}"

    def check_password(self, password: str) -> bool:
        dk = hashlib.pbkdf2_hmac(
            "sha256", 
            password.encode("utf-8"), 
            settings.SECRET_KEY.encode("utf-8"), 
            100000
        )
        hashed_password = binascii.hexlify(dk).decode("utf-8")
        return self.password == f"pbkdf2_sha256$100000${hashed_password}"
    
    def __repr__(self) -> str:
        return f"<User id={self.id} active={self.active}>"


class UserProfile(Base, TimestampMixin):
    __tablename__ = "users_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    
    users = relationship("User", back_populates="user_profiles")
    
    def __repr__(self) -> str:
        return f"<UserProfile id={self.id} active={self.active}>"
    
    