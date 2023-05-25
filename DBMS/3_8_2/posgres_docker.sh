#!/bin/bash
docker run -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust -d --name postgres -v $(pwd):/workspace postgres:9.6
sleep 5
docker run --rm  --name psql --link postgres:postgres -v $(pwd):/workspace postgres:9.6 psql -h postgres -U postgres -f /workspace/task2-public.sql
