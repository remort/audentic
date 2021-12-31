import typing as t

from pydantic import BaseSettings, PostgresDsn, root_validator


class Configuration(BaseSettings):
    logging_level: str = 'INFO'
    db_pool_min_size: int = 1
    db_pool_max_size: int = 5
    listen_host: str = '0.0.0.0'
    listen_port: int = 8080

    db_username: str
    db_password: str
    db_host: str
    db_port: str
    db_database: str

    db_connection_uri: t.Optional[PostgresDsn]

    @root_validator
    def construct_db_connection_uri(cls, v):
        v['db_connection_uri'] = PostgresDsn(
            url='postgresql+asyncpg://{}:{}@{}:{}/{}'.format(
                v.get('db_username'),
                v.get('db_password'),
                v.get('db_host'),
                v.get('db_port'),
                v.get('db_database'),
            ),
            scheme='postgres',
            host=v.get('db_host'),
        )

        return v


configuration = Configuration()
