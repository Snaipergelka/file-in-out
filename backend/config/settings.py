from os import environ

from pydantic import BaseSettings


class DefaultSettings(BaseSettings):

    ENV: str = environ.get("ENV", "local")
    DB_NAME: str = environ.get("POSTGRES_DATABASE", 'postgres')
    DB_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    DB_PORT: int = int(environ.get("POSTGRES_PORT", 5432))
    DB_USER: str = environ.get("POSTGRES_USER", "postgres")
    DB_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "postgres")
    DB_POOL_SIZE: int = int(environ.get("DB_POOL_SIZE", 15))
    DB_CONNECT_RETRY: int = int(environ.get("DB_CONNECT_RETRY", 20))

    REDIS_PORT: int = int(environ.get("REDIS_PORT", 6379))
    REDIS_HOST: str = environ.get("REDIS_HOST", "localhost")

    TEST_DIRECTORY: str = environ.get("TEST_DIRECTORY",
                                      "/Users/snaipergelka/workspace/file-in-out/tests/test-images")

    @property
    def database_settings(self) -> dict:
        """
        Get all settings for connection with database.
        """
        return {
            "database": self.DB_NAME,
            "user": self.DB_USER,
            "password": self.DB_PASSWORD,
            "host": self.DB_HOST,
            "port": self.DB_PORT,
        }

    @property
    def database_uri(self) -> str:
        """
        Get uri for connection with database.
        """
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )

    @property
    def redis_config(self) -> list:
        """
        Get redis host and port
        :return:
        """
        return [self.REDIS_HOST, self.REDIS_PORT]
