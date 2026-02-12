from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas_application import ApplicationOut
from app.crud.crud_application import apply_job
from app.security.token import get_current_user


router = APIRouter(prefix='/application',tags=['application'])


@router.post('/', response_model=ApplicationOut)
def apply(job_id: int,db: Session = Depends(get_db),user = Depends(get_current_user)):
    if user.role != "candidate":
        raise HTTPException(status_code=403, detail="You are not authorized to apply for a job")
    return apply_job(db, job_id, user.id)

