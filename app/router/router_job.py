from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas_job import JobCreate, JobOut
from app.crud.crud_job import create_job
from app.security.token import get_current_user

router = APIRouter(prefix='/job',tags=['job'])

@router.post('/', response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db),user = Depends(get_current_user)):
    if user.role != "employee":
        raise HTTPException(status_code=403, detail="You are not authorized to create a job")
    return create_job(db, job)


