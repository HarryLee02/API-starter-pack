#!/bin/bash

# change this to your project absolute path for cronjob to work
cd /home/harrylee/API-starter-pack/

source .env

docker run -d --rm \
  -v scraper-logs:/app/logs \
  -v docs-volume:/app/docs \
  -e OPENAI_API_KEY="$OPENAI_API_KEY" \
  -e SUPPORT_URL="$SUPPORT_URL" \
  -e OPENAI_VECTOR_STORE_ID="$OPENAI_VECTOR_STORE_ID" \
  --name scraper-run \
  scraper:latest
