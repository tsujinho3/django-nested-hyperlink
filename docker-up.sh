#!/bin/sh

export COMPOSE_PROJECT_ID=$(date  '+%Y%m%d')
export COMPOSE_PROJECT_NAME=$(basename `pwd`)
export COMPOSE_PROJECT_PORT=8000

lsof -i:${COMPOSE_PROJECT_PORT} > /dev/null

if [ $? -eq 0 ]
then
    echo "port:${COMPOSE_PROJECT_PORT} is occupied." $1
    echo "set another port number as COMPOSE_PROJECT_PORT."
    exit 1
fi

cd config

case $1 in
    -n | --no-build)
        OPT="-d"
    ;;
    *)
        OPT="--build -d --remove-orphans"
    ;;
esac

docker-compose up ${OPT}
docker-compose exec app /bin/zsh
docker-compose down
