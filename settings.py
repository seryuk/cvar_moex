from pydantic import ConfigDict, SecretStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(
    BaseSettings,
):
    model_config = ConfigDict(extra="ignore", validate_default=False)

    DB_DSN_ASYNC: SecretStr


settings = Settings()
