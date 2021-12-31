"""initial

Revision ID: d7ad306c967a
Revises: 03895e8d2cb1
Create Date: 2021-11-27 11:20:37.531718

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd7ad306c967a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('genre',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='genre_pkey'),
    postgresql_ignore_search_path=False
    )

    op.create_table('record_label',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='record_label_pkey')
    )

    op.create_table('tag',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='tag_pkey')
    )

    op.create_table('artist',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='artist_pkey')
    )

    op.create_table('release',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('year', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='artist_release_id_fkey'),
    sa.Column('record_label_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['record_label_id'], ['record_label.id'], name='record_label_release_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='release_pkey')
    )

    op.create_table('release_tag',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('release_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['release_id'], ['release.id'], name='release_tag_release_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name='release_tag_tag_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='release_tag_pkey')
    )
    op.create_index('frelease_tag_id_idx', 'release_tag', ['id'], unique=False)
    op.create_unique_constraint('release_tag_uq', 'release_tag', ['release_id', 'tag_id'])

    op.create_table('release_genre',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('release_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['release_id'], ['release.id'], name='release_genre_release_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='release_genre_genre_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='release_genre_pkey')
    )
    op.create_index('frelease_genre_id_idx', 'release_genre', ['id'], unique=False)
    op.create_unique_constraint('release_genre_uq', 'release_genre', ['release_id', 'genre_id'])

    op.create_table('track',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('release_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['release_id'], ['release.id'], name='track_release_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='track_pkey')
    )

    op.create_table('mood',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='mood_pkey')
    )

    op.create_table('playlist',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('mood_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['mood_id'], ['mood.id'], name='mood_playlist_id_fkey'),
    sa.Column('record_label_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['record_label_id'], ['record_label.id'], name='record_label_playlist_id_fkey'),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='artist_playlist_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='playlist_pkey')
    )

    op.create_table('playlist_genre',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('playlist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlist.id'], name='playlist_genre_playlist_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='playlist_genre_genre_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='playlist_genre_pkey')
    )
    op.create_index('playlist_genre_id_idx', 'playlist_genre', ['id'], unique=False)
    op.create_unique_constraint('playlist_genre_uq', 'playlist_genre', ['playlist_id', 'genre_id'])

    op.create_table('playlist_tag',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('playlist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlist.id'], name='playlist_tag_playlist_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name='playlist_tag_tag_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='playlist_tag_pkey')
    )
    op.create_index('playlist_tag_id_idx', 'playlist_tag', ['id'], unique=False)
    op.create_unique_constraint('playlist_tag_uq', 'playlist_tag', ['playlist_id', 'tag_id'])


def downgrade():
    op.drop_table('playlist_tag')
    op.drop_table('playlist_genre')
    op.drop_table('playlist')
    op.drop_table('playlist_track')
    op.drop_table('playlist')
    op.drop_table('mood')
    op.drop_table('track')
    op.drop_table('release_genre')
    op.drop_table('release_tag')
    op.drop_table('release')
    op.drop_table('artist')
    op.drop_table('tag')
    op.drop_table('record_label')
    op.drop_table('genre')
