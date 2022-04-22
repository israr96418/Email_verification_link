from fastapi import FastAPI, Depends, BackgroundTasks
import email
import schame,crud
from database import get_db, Session

app = FastAPI()


@app.get("/")
def get_info():
    return {"message": "Email Notification"}


@app.post("/")
def create_email_notification(email_notification: schame.EmailNotification, background_task: BackgroundTasks,
                              db: Session = Depends(get_db)):
    data_store_int_database = crud.create_notification(db, email_notification)
    background_task.add_task(email.send_email,data_store_int_database,db)
