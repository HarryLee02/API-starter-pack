#!/bin/bash

# Daily scraper cron job
# Add this to your crontab: 0 2 * * * /app/cron-job.sh

cd /app

# Run the scraper
python scraper.py

# Log the execution
echo "$(date): Scraper completed with exit code $?" >> /app/cron.log 