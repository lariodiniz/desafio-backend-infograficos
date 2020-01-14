FROM python:3
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY sd}ap)i237hd(jodf45AS-VAWC>asp@SDFDS
RUN mkdir /infograficoApp
WORKDIR /infograficoApp

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev

RUN pip install -U pip setuptools

COPY requirements.txt /infograficoApp/

RUN pip install -r /infograficoApp/requirements.txt

ADD . /infograficoApp/
# Django service
EXPOSE 8000