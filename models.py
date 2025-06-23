from sqlalchemy import Column, Integer, String, Boolean, Date
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    due_date = Column(Date)
    is_important = Column(Boolean, default=False)
    is_urgent = Column(Boolean, default=False)
    is_completed = Column(Boolean, default=False)