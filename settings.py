from pydantic import BaseSettings

class Settings(BaseSettings):
    giphy_api_key: str = None
    discord_bot_token: str = None
    target_voice_room: str = None

    class Config:
        env_prefix = "HANS_"


SETTINGS = Settings()