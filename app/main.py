from fastapi import FastAPI
from app.database import Base, engine
from app.router import router_user, router_job, router_application

app = FastAPI(title="Job Portal API")

Base.metadata.create_all(bind=engine)

app.include_router(router_user.router)
app.include_router(router_job.router)
app.include_router(router_application.router)


@app.get('/')
def read_root():
    return {'message': 'Welcome to the Job Portal'}