import os

from dotenv import load_dotenv

load_dotenv()

#Host
HOST = os.getenv("HOST", default="127.0.0.1")
PORT = int(os.getenv("PORT", default=8001))

# database
DB_HOST = os.getenv("DB_HOST", default="localhost")
DB_USER = os.getenv("DB_USER", default="postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="docker")
DB_PORT = os.getenv("DB_PORT", default="5432")
DB_NAME = os.getenv("DB_NAME", default="testfast")
DB_SSLMODE = os.getenv("DB_SSLMODE", default="disable")
DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


IS_DEBUG = bool(os.getenv("IS_DEBUG", default="FALSE"))