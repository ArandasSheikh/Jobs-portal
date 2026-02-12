from app.models.model_application import Application


def apply_job(db, job_id, candidate_id):
    db_application = Application(job_id=job_id, candidate_id=candidate_id)
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application