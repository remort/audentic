import logging

from aiohttp import web

from audentic_api.config import configuration
from audentic_api.db.engine import async_session
from audentic_api.handlers.playlist import PlaylistHandler
from audentic_api.managers.playlist import PlaylistManager

log = logging.getLogger(__name__)


async def on_startup(app):
    log.info('DB is set up and connected.')
    app['db_session'] = async_session
    app['playlist_manager'] = PlaylistManager(db_session=async_session)


async def on_shutdown(app):
    log.warning('Shutting down...')
    await app['db_session'].close()


def start_service():
    logging.basicConfig(level=configuration.logging_level)
    log.info('Starting up on %s:%s ...', configuration.listen_host, configuration.listen_port)

    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    app.router.add_route('GET', '/playlist', PlaylistHandler)

    web.run_app(app, host=configuration.listen_host, port=configuration.listen_port)
