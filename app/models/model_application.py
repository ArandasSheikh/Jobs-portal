from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Application(Base):
    __tablename__ = "application"
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"))
    candidate_id = Column(Integer, ForeignKey("users.id"))

