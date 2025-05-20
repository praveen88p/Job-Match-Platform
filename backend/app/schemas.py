from pydantic import BaseModel, EmailStr
from typing import List, Optional
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str



class ProfileCreate(BaseModel):
    location: str
    years_of_experience: int
    skills: List[str]
    preferred_job_type: str 

class ProfileOut(ProfileCreate):
    id: int
    user_id: int

    class Config:
       from_attributes = True

from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    company: str
    location: str
    skills: str

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    id: int

    class Config:
        from_attributes = True


from pydantic import BaseModel
from typing import List

class JobRecommendationRequest(BaseModel):
    skills: List[str]
    experience: str
    preferences: str
