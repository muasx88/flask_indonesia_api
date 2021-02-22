import logging
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = os.getenv("DB_URL")

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
