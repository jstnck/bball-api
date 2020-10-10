FROM python:3

WORKDIR /items-rest

ADD . /items-rest

RUN pip install -r requirements.txt

CMD ["uwsgi", "uwsgi.ini"]