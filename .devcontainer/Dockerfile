# # See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3/.devcontainer/base.Dockerfile

# # [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
# ARG VARIANT="3.10-bullseye"
# FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# # Define the path to the virtualenv to work with
# ARG VENV_PATH="/home/vscode/venv"

# COPY requirements.txt /tmp/pip-tmp/
# RUN su vscode -c "python -m venv /home/vscode/venv" \
#    && su vscode -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt" \
#    && rm -rf /tmp/pip-tmp

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}


# Install Docker
USER root
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io

# Define the path to the virtualenv to work with
ARG VENV_PATH="/home/vscode/venv"

 

COPY requirements.txt /tmp/pip-tmp/
RUN su vscode -c "python -m venv /home/vscode/venv" \
&& su vscode -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt" \
&& rm -rf /tmp/pip-tmp