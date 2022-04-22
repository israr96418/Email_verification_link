# import urllib
# from dotenv import load_dotenv
from config import setting
from fastapi_mail import ConnectionConfig,FastMail
# def database_url():
#     db_password =  urllib.parse.quote_plus('dawar96418')
#     connection_string =  f"mysql+mysqldb://{setting.database_username}:{db_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
# #     return connection_string

def get_fastmail_connection_config():
    fast_mail = FastMail(
        ConnectionConfig(
            MAIL_USERNAME=setting.mail_username,
            MAIL_PASSWORD=setting.mail_password,
            MAIL_FROM=setting.mail_from,
            MAIL_PORT=setting.mail_port,
            MAIL_SERVER=setting.mail_server,
            MAIL_FROM_NAME=setting.mail_from_name,
            MAIL_TLS=setting.mail_tls,
            MAIL_SSL=setting.mail_ssl,
            USE_CREDENTIALS=True,
            TEMPLATE_FOLDER='./template'
        )
    )
    return fast_mail