import models
from database import Session
from schame import EmailNotification
from models import EmailNotification
import schame


def create_notification(db:Session,email_notification:EmailNotification):
    db_Email_notification = models.EmailNotification(
        subject = email_notification.subject.title(),
        email_to = email_notification.email_to.lower(),
        email_body = email_notification.email_body,
    )
    db.add(db_Email_notification)
    db.commit()
    db.refresh(db_Email_notification)
    return db_Email_notification

def update_notification(db: Session, db_email_notification, email_notification_data: schame.UpdateEmailNotification):
    for key, value in email_notification_data.dict(exclude_unset=True).items():
        setattr(db_email_notification, key, value)
    db.add(db_email_notification)
    db.commit()
    db.refresh(db_email_notification)
    return db_email_notification
