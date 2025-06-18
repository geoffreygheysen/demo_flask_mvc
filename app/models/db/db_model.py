from flask_login import UserMixin
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=True)

    # Relation avec Task
    tasks = relationship('Task', back_populates="user")
    
    def get_id(self):
        return str(self.id)

class Task(UserMixin, Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=True)
    
    # Relation avec User
    user = relationship("User", back_populates="tasks")
    # Relation avec Category
    category = relationship("Category", back_populates="tasks")


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    # Relation avec Task
    tasks = relationship('Task', back_populates="category")