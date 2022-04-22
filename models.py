from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import datetime
# sqlmodel design just like pydantic


class EmailNotification(SQLModel, table=True):
    __tablename__ = "email_notification"
    id:Optional[int] = Field(default=None, primary_key=True)
    subject: str
    email_to: str
    email_body: str
    status: bool = Field(default=True)
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())
