# pull base image
FROM python:3.10

# set envorenment variables
ENV PYTHONDONTWRITEBYTCODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /code
WORKDIR /code

# install dependencies
COPY ./requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

# collect static files
RUN python manage.py collectstatic --noinput

# run
CMD daphne config.asgi:application --port $PORT --bind 0.0.0.0 -v2
