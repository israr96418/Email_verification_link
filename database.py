from sqlmodel import create_engine, SQLModel, Session
import utils
from config import setting
import urllib

db_password = urllib.parse.quote_plus('dawar96418')
print("database password: ",db_password)
connection_string = f"mysql+mysqldb://{setting.database_username}:{db_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"

engine = create_engine(connection_string, echo=True)
session = Session(engine)


def create_bd_table():
    SQLModel.metadata.create_all(engine)


# def main():
#     create_bd_table()


# Dependency:
def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()


# if __name__ == '__main__':
#     main()
