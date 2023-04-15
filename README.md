# Fast API Template

FastAPI blank template created to start any new project

## Setup

1. Define environment varaibles by creating a .env file based on .env.example
```
cp .env.example .env
```

## Run using docker-compose
```
docker-compose -f ./compose/develop/docker-compose.yml up --build
```

## Run using poetry
```
poetry install
```
```
poetry run sh ./scripts/start-dev.sh
```