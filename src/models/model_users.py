from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Create_user_model(BaseModel):
    name: str
    email: str
    birth_date: Optional[datetime] = None
    phone_n: Optional[str] = None