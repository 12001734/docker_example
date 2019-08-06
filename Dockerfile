FROM ubuntu:latest

MAINTAINER Rodney J

RUN apt-get update -y && apt-get install python3.6 -y

WORKDIR /app

COPY . /app

RUN apt-get install -y python3-pip
RUN pip3 install flask requests

EXPOSE 80

CMD python3 app.py
