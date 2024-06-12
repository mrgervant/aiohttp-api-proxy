FROM python:3.12.3-slim

WORKDIR /usr/src/app
RUN pip install --no-cache-dir poetry

COPY ./app ./
WORKDIR /usr/src/

COPY poetry.lock pyproject.toml README.md ./
RUN poetry config virtualenvs.create false && poetry install

ENTRYPOINT python3 -m app
