#!/bin/bash

# Run Project
docker-compose --env-file .env up --build -d
sleep 5

# Query results
curl 127.0.0.1:5001/secret | jq '.secret_code'
curl 127.0.0.1:5001/health | jq '.'

# Destroy 
docker-compose down

