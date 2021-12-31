import sqlalchemy as sa
from sqlalchemy import MetaData, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base(metadata=MetaData())


class GenreModel(Base):
    __tablename__ = 'genre'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)


class RecordLabelModel(Base):
    __tablename__ = 'record_label'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)

    releases = relationship('ReleaseModel', back_populates='record_label')


class TagModel(Base):
    __tablename__ = 'tag'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)


class ArtistModel(Base):
    __tablename__ = 'artist'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)

    releases = relationship('ReleaseModel', back_populates='artist')


class ReleaseModel(Base):
    __tablename__ = 'release'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)
    year = sa.Column(sa.Integer)
    artist_id = sa.Column(sa.Integer, sa.ForeignKey('artist.id'))
    record_label_id = sa.Column(sa.Integer, sa.ForeignKey('record_label.id'))

    artist = relationship('ArtistModel', back_populates='releases')
    record_label = relationship('RecordLabelModel', back_populates='releases')


class ReleaseTagModel(Base):
    __tablename__ = 'release_tag'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    release_id = sa.Column(sa.Integer, sa.ForeignKey('release.id'))
    tag_id = sa.Column(sa.Integer, sa.ForeignKey('tag.id'))

    __table_args__ = (
        UniqueConstraint('release_id', 'tag_id', name='release_tag_uq'),
    )


class ReleaseGenreModel(Base):
    __tablename__ = 'release_genre'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    release_id = sa.Column(sa.Integer, sa.ForeignKey('release.id'))
    genre_id = sa.Column(sa.Integer, sa.ForeignKey('genre.id'))

    __table_args__ = (
        UniqueConstraint('release_id', 'genre_id', name='release_genre_uq'),
    )


class TrackModel(Base):
    __tablename__ = 'track'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)
    release_id = sa.Column(sa.Integer, sa.ForeignKey('release.id'))


class MoodModel(Base):
    __tablename__ = 'mood'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)


class PlaylistModel(Base):
    __tablename__ = 'playlist'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    name = sa.Column(sa.String)
    mood_id = sa.Column(sa.Integer, sa.ForeignKey('mood.id'))
    record_label_id = sa.Column(sa.Integer, sa.ForeignKey('record_label.id'))
    artist_id = sa.Column(sa.Integer, sa.ForeignKey('artist.id'))


class PlaylistGenreModel(Base):
    __tablename__ = 'playlist_genre'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    playlist_id = sa.Column(sa.Integer, sa.ForeignKey('playlist.id'))
    genre_id = sa.Column(sa.Integer, sa.ForeignKey('genre.id'))

    __table_args__ = (
        UniqueConstraint('playlist_id', 'genre_id', name='playlist_genre_uq'),
    )


class PlaylistTagModel(Base):
    __tablename__ = 'playlist_tag'

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    playlist_id = sa.Column(sa.Integer, sa.ForeignKey('playlist.id'))
    tag_id = sa.Column(sa.Integer, sa.ForeignKey('tag.id'))

    __table_args__ = (
        UniqueConstraint('playlist_id', 'tag_id', name='playlist_tag_uq'),
    )
