#!/bin/sh

echo "Starting up nginx to serve at :8088"
docker run --rm --name isat-slides -dv $(pwd):/usr/share/nginx/html -p 8088:80 nginx:alpine
sleep 2
echo "Listening at :8088"