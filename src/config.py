# mypy: disable-error-code="call-arg"
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    """Config for getting environment variables"""

    # Database env vars
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def postgres_url(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=self.postgres_user,
                password=self.postgres_password,
                host=self.postgres_host,
                port=self.postgres_port,
                path=f"{self.postgres_db}",
            )
        )


class AppConfig(BaseSettings):
    """Main app configuration"""

    pass


envs = EnvConfig()
