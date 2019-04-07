#!/usr/bin/env bash

docker network create --attachable --scope swarm --driver overlay play-kong-net

docker stack deploy -c gateway.stack.yml play_kong_gateway
docker stack deploy -c services.stack.yml play_kong_services
