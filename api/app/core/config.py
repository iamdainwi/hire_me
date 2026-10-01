import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL: str = os.getenv("POSTGRES_DATABASE_URL", "")


settings = Settings()
