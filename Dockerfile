# set base image (host OS)
FROM python:3.12.2-slim


RUN apt-get update \
    && apt-get -y install libpq-dev gcc


# set the working directory in the container
WORKDIR /code

ENV FLASK_APP api
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development

# copy env file
COPY .env .env

# copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
