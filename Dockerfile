FROM python:2.7.11

# install lessc..
# FIXME!! 実行環境にnodejsとlesscをインストールするのは避けたい
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g less@1.3.3

# アプリの用意
RUN mkdir -p /app; mkdir -p /var/log/pyconjp
WORKDIR /app
VOLUME /app

COPY . /app
RUN pip install -U pip; pip install -r /app/requirements/production.txt -f /app/wheelhouse --no-index

ENV DJANGO_SETTINGS_MODULE=pyconjp.settings
ENV ENVIRONMENT=dev
ENV DEBUG=True
ENV DB_ENGINE=""
ENV DB_NAME="<YOUR_DB_NAME>"
ENV DB_HOST=localhost
ENV DB_PORT=
ENV DB_USER="<YOUR_DB_USER>"
ENV DB_PASSWORD="<YOUR_DB_PASSWORD>"
ENV MEDIA_ROOT=
ENV EMAIL_HOST=
ENV EMAIL_FROM=
ENV ALLOWED_HOSTS="localhost, 0.0.0.0"
ENV SECRET_KEY="<YOUR_SECRET_KEY>"
ENV LANG=ja_JP.UTF-8
ENV TWITTER_CONSUMER_KEY="<YOUR_CONSUMER_KEY>"
ENV TWITTER_CONSUMER_SECRET="<YOUR_CONSUMER_SECRET>"
ENV FACEBOOK_APP_ID="<YOUR_APP_ID>"
ENV FACEBOOK_API_SECRET="<YOUR_API_SECRET>"
ENV LOG_PATH="/var/log/pyconjp/pyconjp_website.log"
ENV ERROR_LOG_PATH="/var/log/pyconjp/pyconjp_website.error.log"
ENV LOG_LEVEL="DEBUG"

CMD ["bash", "/app/scripts/run-docker-website.sh"]

