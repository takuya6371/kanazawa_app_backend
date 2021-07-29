#!/bin/bash
docker-compose run --rm -T --name `uuidgen` batch python /batch/src/handler/CollectNews.py