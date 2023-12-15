import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    photo: str


class CreateUser(UserBase):
    password: constr(min_length=8)
    passwordConfirm: str
    role: str = "user"
    verified: bool = False


class LoginUser(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponse(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class FilteredUserResponse(UserBase):
    id: uuid.UUID


class PostBase(BaseModel):
    title: str
    content: str
    category: str
    image: str
    user_id: Optional[uuid.UUID] = None


class PostResponse(PostBase):
    id: uuid.UUID
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime


class UpdatePost(PostBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ListPostResponse(BaseModel):
    status: str
    results: int
    posts: List[PostResponse]
