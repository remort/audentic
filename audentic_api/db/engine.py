import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from audentic_api.config import configuration

log = logging.getLogger(__name__)

async_engine = create_async_engine(configuration.db_connection_uri, echo=False)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)()
