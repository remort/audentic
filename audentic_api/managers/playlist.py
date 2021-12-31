import logging
import typing as t

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from audentic_api.db.model.models import ReleaseModel, ReleaseTagModel, TagModel, TrackModel
from audentic_api.managers.schemas import PlaylistByTagsCollectionSchema, PlaylistByTagsSchema

log = logging.getLogger(__name__)


class PlaylistManager:
    def __init__(self, db_session: AsyncSession) -> None:
        self.__db_session = db_session

    async def get(self, tags: t.List[str]) -> PlaylistByTagsCollectionSchema:
        results = await self.__db_session.execute(
            select(
                TrackModel.name.label('track_name'),
                ReleaseModel.name.label('release_name'),
            )
            .join(ReleaseModel, TrackModel.release_id == ReleaseModel.id)
            .join(ReleaseTagModel, ReleaseModel.id == ReleaseTagModel.release_id)
            .join(TagModel, ReleaseTagModel.tag_id == TagModel.id)
            .where(TagModel.name.in_(tags))
        )
        tracks = [PlaylistByTagsSchema(track_name=r.track_name, release_name=r.release_name) for r in results]
        return PlaylistByTagsCollectionSchema(tracks=tracks)
