from pydantic import BaseModel
from typing import Optional


class UserDTO(BaseModel):
    id: Optional[int] = None
    username: str
    email: str

    class Config:
        from_attributes = True
