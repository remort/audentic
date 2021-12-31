FROM python:3.9-alpine

COPY ./requirements.txt ./requirements.txt
RUN apk add --no-cache gcc musl-dev postgresql-dev postgresql-client
RUN pip install --no-cache-dir --requirement requirements.txt --target /requirements/ --upgrade

ENV \
    PATH=$PATH:/requirements/bin/ \
    PYTHONPATH=/requirements/:/app

WORKDIR /app/

COPY run.py alembic.ini ./
COPY docker-entrypoint.sh /usr/local/bin/
COPY ./audentic_api/ ./audentic_api/

ENTRYPOINT ["docker-entrypoint.sh"]
