FROM python:3.9.6-bullseye

ARG USER="devops-user"
ARG APP_NAME="devops-challenge"
ARG APP_PATH=/usr/src/app

RUN mkdir -p ${APP_PATH}

COPY . ${APP_PATH}/

WORKDIR ${APP_PATH}/devops-challenge

RUN pip install --no-cache-dir -r ../requirements.txt


RUN groupadd -g 888 ${USER} && \
    useradd -m -u 888 -g ${USER} -m ${USER} && \
    chown -R ${USER}:${USER} ${APP_PATH}


CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "2", "app:app"]
