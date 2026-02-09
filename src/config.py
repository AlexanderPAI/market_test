# mypy: disable-error-code="call-arg"
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    """Config for getting environment variables"""

    test_env: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


class AppConfig(BaseSettings):
    """Main app configuration"""

    pass


envs = EnvConfig()
