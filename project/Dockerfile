# pull official base image
FROM python:3.9.6-slim-buster


ENV HOME=/home/app
ENV APP_HOME=${HOME}/web

# create the app user
RUN addgroup --system app 
RUN adduser --system --group app

# set working directory
ENV HOME=/home/app
ENV APP_HOME=${HOME}/web

# create the appropriate directories
# RUN mkdir $APP_HOME
WORKDIR $HOME
RUN chown app:app -R ${HOME}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

USER app
ENV PATH "${HOME}/.local/bin:${HOME}:${APP_HOME}:${PATH}"

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .