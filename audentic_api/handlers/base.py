from aiohttp.web import Request, View

from audentic_api.managers.playlist import PlaylistManager

REST_API_ERROR_STATUS = 442


class BaseHandler(View):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        playlist_manager = self.request.app['playlist_manager']
        self._playlist_manager: PlaylistManager = playlist_manager

        # Unique, unused by others status to determine business logic errors on front end.
        # Must be used in HTTP-handlers for returning business logic errors to front-end only.
        self._error_status = REST_API_ERROR_STATUS
