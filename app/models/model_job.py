from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True, index=True)
    description = Column(String(255))
    employee_id = Column(Integer, ForeignKey("users.id"))
    