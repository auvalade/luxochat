FROM python:3.6.1

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
#ADD docker-entry.sh /code/
RUN pip install -r requirements.txt

ADD . /code/

# RUN python manage.py makemigrations
# RUN python manage.py migrate
#RUN docker-entry.sh
#CMD ["bash -c","docker-entry.sh"]

