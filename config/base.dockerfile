FROM python:3.10-slim

ENV DOCKER true

# Installed apps
USER root
RUN apt update \
    && apt install -y \
    zsh \
    vim \
    exa \
    bat
ENV SHELL /bin/zsh

WORKDIR /root
COPY ./requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Logging in as a rootless user
ARG UID=1001
ARG GID=1001
RUN useradd -u $UID -o -m rootless
RUN groupmod -g $GID -o rootless
USER rootless


WORKDIR /home/rootless
COPY ./base.zshenv .zshenv
COPY ./base.zshrc .zshrc

WORKDIR /home/rootless/src
