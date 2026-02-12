from pydantic import BaseModel

class ApplicationOut(BaseModel):
    id: int
    job_id: int
    candidate_id: int

    class Config:
        orm_mode = True
