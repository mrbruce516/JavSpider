FROM python:3-slim
WORKDIR /app/scrapy
VOLUME /app/scrapy
EXPOSE 6800
COPY scrapyd.conf /etc/scrapyd/scrapyd.conf
COPY requirements.txt /app/scrapy/requirements.txt
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    pip install -r requirements.txt && \
    pip install scrapyd \
    && apt-get update && apt-get install -y wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /root/.cache/pip

CMD [ "scrapyd" ]
