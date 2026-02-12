from app.models.model_job import Job
 
def create_job(db, job,employee_id):
    db_job = Job(**job.dict(),employee_id = employee_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
