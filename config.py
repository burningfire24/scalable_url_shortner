from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    port:int = 8000
    rhost1:str = 'localhost'
    rhost2:str = 'localhost'
    rhost3:str = 'localhost'
    rport1:int = 6379
    rport2:int = 6380
    rport3:int = 6381

    model_config=SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )

Config = Settings()    