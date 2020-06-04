FROM ubuntu:bionic

WORKDIR /usr/local/GrubMenuScraper
COPY . .

ENV TZ=US/Eastern

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update
RUN apt-get -y install procps git xvfb python3 vim python3-pip \
fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
curl unzip wget firefox

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements

RUN chmod a+x /usr/local/bin/geckodriver
