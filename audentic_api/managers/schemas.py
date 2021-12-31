import typing as t

from pydantic import BaseModel


class PlaylistByTagsSchema(BaseModel):
    track_name: str
    release_name: str


class PlaylistByTagsCollectionSchema(BaseModel):
    tracks: t.List[PlaylistByTagsSchema]
