from database import Session
from fastapi_mail import MessageSchema
from datetime import datetime
from . import schame,utils,crud

fast_mail = utils.get_fastmail_connection_config()

def send_email(email_notification:schame.emailnotification_db, db:Session):
    message = MessageSchema(
        subject=email_notification.subject,
        recipients=[email_notification.email_to],
        body=email_notification.email_body,
        subtype='html',
    )

    fast_mail.send_message(message,template_name='pattern.html')
    update_email_notification = schame.UpdateEmailNotification(
        status=True,
        updated_at=datetime.now()
    )

    crud.update_notification(db, email_notification, update_email_notification)