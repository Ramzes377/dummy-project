from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    HOST: str = '0.0.0.0'
    PORT: int = 8000

    CLUSTER_NAME: str


Config = BaseConfig()
