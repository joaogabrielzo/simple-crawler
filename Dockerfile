FROM python:3.6-slim

RUN apt-get update \
    && apt-get install -y gcc \
    ca-certificates \
    wget \
    unzip \
    gnupg gnupg1 gnupg2 \
    && apt-get clean

ENV PYTHONUNBUFFERED 1
ENV DISPLAY=:99

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get -y update \
    && apt-get install -y google-chrome-stable

RUN wget --no-check-certificate https://chromedriver.storage.googleapis.com/80.0.3987.16/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin \
    && rm chromedriver_linux64.zip

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app/

RUN pip3 install -r requirements.txt

ADD . /app/

CMD 'python3' 'simple-crawler.py'
