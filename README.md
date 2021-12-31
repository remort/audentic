# audentic
Example API for generating playlists based on tags, genres, artists and labels, using new asynchronous SQLAlchemy.

# run and test

    docker-compose up -d
    curl -X GET http://localhost:8000/playlist?tag=stomp&tag=experimental

# lint

    make lint
