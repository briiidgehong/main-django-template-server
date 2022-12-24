FROM python:3.8-alpine

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /app/
USER root

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev bash
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt 

COPY ./entrypoint.sh /app/entrypoint.sh
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . /app/
ENTRYPOINT ["./entrypoint.sh"]