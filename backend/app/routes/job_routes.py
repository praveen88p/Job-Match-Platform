from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=schemas.JobOut)
def create_job(job: schemas.JobCreate, db: Session = Depends(database.get_db)):
    db_job = models.Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/", response_model=list[schemas.JobOut])
def get_jobs(db: Session = Depends(database.get_db)):
    return db.query(models.Job).all()


# app/routes/job_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Job, User
import requests
import json
from app.auth import get_current_user
from app.schemas import JobRecommendationRequest

router = APIRouter()

OPENROUTER_API_KEY = "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"

@router.post("/recommend-jobs")
def recommend_jobs(request: JobRecommendationRequest, db: Session = Depends(get_db)):
    jobs = db.query(Job).all()

    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found in database.")

    job_list = "\n".join([f"- {job.title} at {job.company}, {job.location} (Skills: {job.skills})" for job in jobs])


    prompt = f"""
You are an intelligent job-matching assistant.

User Profile:
- Skills: {', '.join(request.skills)}
- Experience: {request.experience}
- Preferences: {request.preferences}

Here is the list of available jobs:
{job_list}

Based on the user profile, select the 3 most relevant jobs and explain why.
Return ONLY the job titles and reasons in a clean format.
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer <OPENROUTER_API_KEY>",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "meta-llama/llama-3.3-8b-instruct:free",
            "messages": [{"role": "user", "content": prompt}]
        })
    )

    try:
        content = response.json()["choices"][0]["message"]["content"]
        return {"recommendations": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail="LLM response error")