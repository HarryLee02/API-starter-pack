FROM python:3.12-alpine

WORKDIR /app

# Install cron and other dependencies
RUN apk add --no-cache dcron

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scraper.py .
COPY cron-job.sh .
COPY .env .

RUN mkdir -p docs logs

# Make cron job executable
RUN chmod +x cron-job.sh

# Create crontab file
RUN echo "0 2 * * * /app/cron-job.sh" > /etc/crontabs/root

# Create startup script
RUN echo '#!/bin/sh' > /app/start.sh && \
    echo 'crond -f -d 8 &' >> /app/start.sh && \
    echo 'python scraper.py' >> /app/start.sh && \
    chmod +x /app/start.sh

CMD ["/app/start.sh"] 