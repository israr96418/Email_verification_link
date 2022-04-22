from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class EmailNotification(BaseModel):
    id: Optional[int] = None
    subject: str
    email_to: str
    email_body: str
    status: bool = False

    class Config:
        orm_mode = True


class emailnotification_db(EmailNotification):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UpdateEmailNotification(BaseModel):
    status: bool = False
    updated_at: datetime