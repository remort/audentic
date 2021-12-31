import logging

from aiohttp.web import Response, json_response

from audentic_api.handlers.base import BaseHandler

log = logging.getLogger(__name__)


class PlaylistHandler(BaseHandler):
    async def get(self) -> Response:
        tags = self.request.query.getall('tag', None)
        if not tags:
            return json_response(status=self._error_status, data={'error': 'NO_TAGS_SENT'})

        playlist = await self._playlist_manager.get(tags)
        if not playlist:
            return json_response({})

        log.info('Got meta list: %s.', playlist)
        return json_response(playlist.dict())
