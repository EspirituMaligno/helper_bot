from pydantic import Field
from pydantic_settings import SettingsConfigDict, BaseSettings


class SettingsBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


class AppSettings(SettingsBase):
    BOT_TOKEN: str = Field(..., alias="BOT_TOKEN")
    LOG_PATH: str = Field(..., alias="LOG_PATH")
    CHAT_ID: str = Field(..., alias="CHAT_ID")
    VPN_THREAD_ID: int = Field(..., alias="VPN_THREAD_ID")


settings = AppSettings()
