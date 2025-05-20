from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, auth

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.post("/", response_model=schemas.ProfileOut)
def create_or_update_profile(
    profile: schemas.ProfileCreate,
    db: Session = Depends(auth.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    existing = db.query(models.Profile).filter_by(user_id=current_user.id).first()
    if existing:
        for field, value in profile.dict().items():
            setattr(existing, field, value)
        db.commit()
        db.refresh(existing)
        return existing
    
    new_profile = models.Profile(**profile.dict(), user_id=current_user.id)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.get("/", response_model=schemas.ProfileOut)
def get_profile(
    db: Session = Depends(auth.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    profile = db.query(models.Profile).filter_by(user_id=current_user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
