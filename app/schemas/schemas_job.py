from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str


class JobOut(BaseModel):
    id: int

    class Config:
        orm_mode = True