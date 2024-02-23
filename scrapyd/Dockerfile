FROM python:3-alpine AS builder
WORKDIR /app/scrapy
EXPOSE 6800
COPY scrapyd.conf /etc/scrapyd/scrapyd.conf
COPY requirements.txt /app/scrapy/requirements.txt
RUN apk add build-base \
    libffi-dev && \
    pip install -r requirements.txt && \
    pip install scrapyd
CMD [ "scrapyd" ]
